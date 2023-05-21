# local 環境の設定

install:
	poetry install

requirements:
	poetry run pip freeze > requirements.lock
# todo: docker内でpip installしてfreezeするようにする

build:
	docker build --no-cache --target=prod -t fastapi_k8s:latest .

run:
	docker-compose up

build_k8s:
	minikube delete
	minikube start
	minikube image load fastapi_k8s:latest
	kubectl apply -f manifests
# todo: 名前ちゃんと考える
#	kill -KILL -f "minikube tunnel"

check_k8s:
	kubectl config get-contexts
	kubectl get secrets
	kubectl get configmaps
	kubectl get pods
	kubectl get svc
	kubectl get ep
# todo: 名前ちゃんと考える

curl:
	curl http://localhost:8000
