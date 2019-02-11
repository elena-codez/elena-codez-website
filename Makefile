build:
	docker-compose build

nocachebuild:
	docker-compose build --no-cache

run:
	docker-compose up -d

stop:
	docker-compose down

debug:
	docker-compose up

.PHONY=build
