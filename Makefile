build:
	docker compose build --pull --no-cache

up:
	docker compose up

down:
	docker compose down --remove-orphans

tag:
	docker image tag bf4-stats-prometheus-exporter-app skkay/bf4-stats-prometheus-exporter:$(major)
	docker image tag bf4-stats-prometheus-exporter-app skkay/bf4-stats-prometheus-exporter:$(major).$(minor)
	docker image tag bf4-stats-prometheus-exporter-app skkay/bf4-stats-prometheus-exporter:$(major).$(minor).$(patch)
	docker image tag bf4-stats-prometheus-exporter-app skkay/bf4-stats-prometheus-exporter:latest

push:
	docker image push skkay/bf4-stats-prometheus-exporter:$(major)
	docker image push skkay/bf4-stats-prometheus-exporter:$(major).$(minor)
	docker image push skkay/bf4-stats-prometheus-exporter:$(major).$(minor).$(patch)
	docker image push skkay/bf4-stats-prometheus-exporter:latest
