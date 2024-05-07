
from dataclasses import dataclass
import datetime
import os
import json
import random
import uuid as uuid_module
import time

import kafka.admin as kafka_admin
import kafka.producer as kafka_producer

@dataclass
class GenderSharedData:
    GENDER_ID: int
    GENDER_NAME: str 

@dataclass
class MovieSharedData:
    MOVIE_ID: int 
    TITLE_NAME: str
    GENDER_ID: int

@dataclass
class PersonSharedData:
    NAME: str 
    ID: str
    
@dataclass
class SharedData:
    GENDER: list[GenderSharedData]
    MOVIE: list[MovieSharedData]
    PERSON: list[PersonSharedData]
    
@dataclass
class TicketSale:
    uuid: str 
    movie_id: int
    ticket_value: float 
    number_of_seats: int 
    room: str 
    cinema: str
    date: str

class DataHandler:
    
    def __init__(self, shared_data: SharedData):
        self.shared_data = shared_data
        
    def _get_random_gender(self) -> GenderSharedData:
        return random.choice(self.shared_data.GENDER)

    def _get_random_movie(self) -> MovieSharedData:
        return random.choice(self.shared_data.MOVIE)

    def _get_random_person(self) -> PersonSharedData:
        return random.choice(self.shared_data.PERSON)    
    
    def generate_ticket_sale(self):
        uuid = str(uuid_module.uuid4())
        movie_id = self._get_random_movie().MOVIE_ID
        ticket_value = random.uniform(10, 50)
        number_of_seats = random.randint(1, 10)
        room = random.choice(['A', 'B', 'C', 'D'])
        cinema = random.choice(['Cinema 1', 'Cinema 2', 'Cinema 3'])
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       
        return TicketSale(uuid, movie_id, ticket_value, number_of_seats, room, cinema, date) 
    
    @staticmethod
    def read_shared_data(filepath: str = None) -> SharedData:
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


class ConnectionNotInitialized(Exception):
    pass 

class CannotInitializeConnection(Exception):
    pass

class KafkaHandler:
    
    def __init__(self, topic_name: str, host: str) -> None:
        self.topic_name = topic_name
        self.host = host
        self.kakfa_admin_client: kafka_admin.KafkaAdminClient = None
        self.kafka_producer: kafka_producer.KafkaProducer = None
        
    def connect_admin_client(self) -> None | Exception:
        for _ in range(5):
            try: 
                self.kakfa_admin_client = kafka_admin.KafkaAdminClient(bootstrap_servers=[self.host], retry_backoff_ms=1000)
                return 
            
            except Exception as e: 
                print('error occurred when trying to connect to kafka admin client: ', e, 'retrying in 10 seconds...')
                time.sleep(10)
                continue
            
        return CannotInitializeConnection('could not connect to kafka admin client')


    def close_admin_client(self) -> None:
        if self.kakfa_admin_client is not None:
            self.kakfa_admin_client.close()
            self.kakfa_admin_client = None

    def connect_producer_client(self) -> None | Exception:
        for _ in range(5):
            try: 
                self.kafka_producer = kafka_producer.KafkaProducer(bootstrap_servers=[self.host])
                return 
            
            except Exception as e: 
                print('error occurred when trying to connect to kafka producer client: ', e, 'retrying in 10 seconds...')
                time.sleep(10)
                continue
            
        return CannotInitializeConnection('could not connect to kafka producer client')
        
    def close_producer_client(self) -> None:
        if self.kafka_producer is not None:
            self.kafka_producer.close()
            self.kafka_producer = None
            
    def send_ticket_sale(self, message: TicketSale) -> None | Exception:
        if self.kafka_producer is None:
            return ConnectionNotInitialized('kafka producer connection not initialized')
        
        message = json.dumps(message.__dict__).encode('utf-8')
        self.kafka_producer.send(self.topic_name, message)
        
    def create_topic_if_not_exists(self) -> None | Exception:
        if self.kakfa_admin_client is None:
            return ConnectionNotInitialized('kafka admin client connection not initialized')
        
        topics = self.kakfa_admin_client.list_topics()
        
        if self.topic_name in topics:
            return 
        
        topic_to_create = kafka_admin.NewTopic(name=self.topic_name, num_partitions=1, replication_factor=1)
        self.kakfa_admin_client.create_topics(new_topics=[topic_to_create], validate_only=False)


def main():
    TOPIC_NAME = "ticket_sales"
    KAFKA_HOST = "kafka:29092"
    
    shared_data = DataHandler.read_shared_data()
    data_handler = DataHandler(shared_data)
    kafka_handler = KafkaHandler(TOPIC_NAME, KAFKA_HOST)
    

    err = kafka_handler.connect_admin_client()
    if err:
        print('cannot connect admin client: ', err)
        return
    err = kafka_handler.create_topic_if_not_exists()
    if err:
        print('cannot create topic: ', err)
        return
    kafka_handler.close_admin_client()

    err = kafka_handler.connect_producer_client()
    if err:
        print('cannot connect producer client: ', err)
        return
    while True:
        ticket_sale = data_handler.generate_ticket_sale()
        err = kafka_handler.send_ticket_sale(ticket_sale)
        if err: 
            print('cannot send ticket sale: ', err)
            return
        
        print(f'ticket sale sent: {ticket_sale.__dict__}')
        time.sleep(5)
    


if __name__ == "__main__":
    main()