FROM python:3.9-slim AS prod

COPY ./requirements.lock /opt/fastapi_k8s/
RUN pip install pip --upgrade \
    && pip install -r /opt/fastapi_k8s/requirements.lock

COPY ./app/ /opt/fastapi_k8s/app/

WORKDIR /opt/fastapi_k8s
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
