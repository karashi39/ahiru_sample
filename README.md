# ahiru_sample
ahiru no sample

## Usage

install:
- poetry
- docker
- minikube

run:
```
make install
make build
make build_k8s
```

run in another terminal:
```
minikube tunnel
```

back to original terminal:
```
make check_k8s
make curl
```

## Tips

### Run in docker-compose

k8s が不安になった時に Docker に問題がないことを切り分ける用

```
make build
make run
```

### browzer

jinja2 (template engine) を使って 裏では pokemon api を叩くサンプルを作った

```
http://localhost:8000/pokemon/{pokemon_id}
# pokemon_id は int
```
