.PHONY: build_ui
build_ui:
	docker build --tag ddl2-ui ui

.PHONY: run_ui
run_ui:
	docker run --name ddl2-ui --detach --publish 5050:80 ddl2-ui
	docker ps -a

.PHONY: test_ui
test_ui:
	curl --silent http://localhost:5050 | grep 'Welcome to ddl2'

.venv/timestamp: api/requirements.txt
	/usr/bin/virtualenv --python=/usr/bin/python3.4 .venv
	.venv/bin/pip install -r api/requirements.txt
	touch $@

.PHONY: run_api
run_api:
	.venv/bin/python api/manage.py runserver
