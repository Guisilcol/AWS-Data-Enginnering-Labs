import dataclasses
import datetime
import typing
import sqlite3
import os
import random 
import json
import uuid

import fastapi

@dataclasses.dataclass
class GenderSharedData:
    GENDER_ID: int
    GENDER_NAME: str 

@dataclasses.dataclass
class MovieSharedData:
    MOVIE_ID: int 
    TITLE_NAME: str
    GENDER_ID: int

@dataclasses.dataclass
class PersonSharedData:
    NAME: str 
    ID: str
    
@dataclasses.dataclass
class SharedData:
    GENDER: typing.List[GenderSharedData]
    MOVIE: typing.List[MovieSharedData]
    PERSON: typing.List[PersonSharedData]
    
    def get_random_gender(self) -> GenderSharedData:
        return random.choice(self.GENDER)

    def get_random_movie(self) -> MovieSharedData:
        return random.choice(self.MOVIE)

    def get_random_person(self) -> PersonSharedData:
        return random.choice(self.PERSON)    
    
    @staticmethod
    def read_shared_data(filepath: str = None):
        """
        Reads the shared data from a json file 

        Args:
            filepath (str, optional): The path to the json file. If None, the function assumes that the file is in the same folder as this file. Defaults to None.

        Returns:
            SharedData: The shared data object (content of the json file as a dataclass object)
        """
        if filepath is None:
            folder_of_this_file = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(folder_of_this_file, 'shared_data.json')
        
        with open(filepath, 'r') as f:
            data = json.load(f)
            return SharedData(
                GENDER=[GenderSharedData(**x) for x in data['GENDER']],
                MOVIE=[MovieSharedData(**x) for x in data['MOVIE']],
                PERSON=[PersonSharedData(**x) for x in data['PERSON']]
            )

@dataclasses.dataclass
class DB:
    conn: sqlite3.Connection
    
    @staticmethod
    def get_db(filepath: str = None):
        if filepath is None:
            folder_of_this_file = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(folder_of_this_file, 'database.db')
        
        conn = sqlite3.connect(filepath)
        conn.row_factory = sqlite3.Row
        return DB(conn)
    
    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS 
                criticize (
                    uuid TEXT PRIMARY KEY,
                    movie_id INTEGER,
                    person_uuid TEXT,
                    person_name TEXT,
                    note INTEGER,
                    comment TEXT,
                    created_at DATE
                );
        ''')
        
    def generate_data(self, shared_data: SharedData):
        dates = [datetime.datetime.now().date() - datetime.timedelta(days=i) for i in range(0, 7)]
        for date in dates:
            cursor = self.conn.cursor()
            cursor.execute('SELECT COUNT(*) as COUNT FROM criticize WHERE created_at = ?', [date])
            row_count = cursor.fetchone()[0]
            
            if row_count != 0:
                continue 
            
            max_rows = random.randint(500, 1000)
            
            for _ in range(0, max_rows):
                data = {
                    'uuid': str(uuid.uuid4()),
                    'movie_id': shared_data.get_random_movie().MOVIE_ID,
                    'person_uuid': shared_data.get_random_person().ID,
                    'person_name': shared_data.get_random_person().NAME,
                    'note': random.randint(1, 5),
                    'comment': 'A random comment here! \n :)',
                    'created_at': date
                }
                
                cursor.execute('''
                    INSERT INTO criticize (uuid, movie_id, person_uuid, person_name, note, comment, created_at)
                    VALUES (:uuid, :movie_id, :person_uuid, :person_name, :note, :comment, :created_at)
                ''', data)
                
            self.conn.commit()
                

# API 
shared_data = SharedData.read_shared_data()

db = DB.get_db()
db.create_tables()
db.generate_data(shared_data)

app = fastapi.FastAPI()

@app.get('/criticize/{id}')
async def get_criticize(id: str, response: fastapi.Response):
    cursor = db.conn.cursor()
    cursor.execute('SELECT * FROM criticize WHERE uuid = ?', [id])
    data = cursor.fetchone()
    if data is None:
        response.status_code = 404 
        return None
    return data

@app.get('/criticize')
async def get_criticize(response: fastapi.Response, start_date: str, end_date: str, page: int = 1):
    
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError:
        response.status_code = 400
        return {
            'error': 'Invalid date format. Please use YYYY-MM-DD'
        }
        
    if str(page).isdigit() is False or page < 1:
        response.status_code = 400
        return {
            'error': 'Invalid page number. Must be a positive integer'
        }
    
    cursor = db.conn.cursor()
    cursor.execute('''
        SELECT COUNT(*) as COUNT FROM criticize 
        WHERE created_at BETWEEN ? AND ?
    ''', [start_date, end_date])
    count = cursor.fetchone()[0]
    
    total_pages = count // 100
    
    cursor.execute('''
        SELECT * FROM criticize 
        WHERE created_at BETWEEN ? AND ?
        ORDER BY created_at DESC
        LIMIT 100 OFFSET ?  
    ''', [start_date, end_date, (page - 1) * 100])
    
    return {
        'row_count': count,
        'total_pages': total_pages,
        'data': cursor.fetchall()
    }



    

