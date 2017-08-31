.PHONY: build_ui
build_ui:
	docker build --tag ddl2-ui ui

.PHONY: run_ui
run_ui:
	docker run --rm --name ddl2-ui --detach --publish 5050:80 ddl2-ui
	docker ps -a

.PHONY: test_ui
test_ui:
	curl --silent http://localhost:5050 | grep 'Welcome to ddl2'

.venv/timestamp: api/requirements.txt
	/usr/bin/virtualenv --python=/usr/bin/python3.4 .venv
	.venv/bin/pip install -r api/requirements.txt
	touch $@

build_api:
	docker build --tag ddl2-api api

.PHONY: run_api
run_api:
	docker run --rm --name ddl2-api --publish 8000:8000 ddl2-api
	docker ps -a

run_dev_api: .venv/timestamp
	.venv/bin/python api/manage.py runserver
