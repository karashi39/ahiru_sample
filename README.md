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
