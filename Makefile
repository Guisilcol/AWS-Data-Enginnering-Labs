start-source-infra:
	docker-compose up
	
stop-source-infra:
	docker compose down 

recreate-source-infra:
	docker compose down
	docker compose up --build

