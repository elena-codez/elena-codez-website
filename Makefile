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

lint:
	flake8 elena_codez/
	black --check elena_codez/

format:
	black elena_codez/

test:
	pytest elena_codez/ --ds=config.settings.test

.PHONY=build
