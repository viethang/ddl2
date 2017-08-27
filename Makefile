build_ui:
	docker build --tag ddl2-ui ui

run_ui:
	docker run --name ddl2-ui --detach --publish 5050:80 ddl2-ui

test_ui:
	curl --silent http://localhost:5050 | grep 'Welcome to ddl2'