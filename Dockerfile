FROM python:3.9-slim AS prod

ARG WORKDIR=/opt/fastapi_k8s

COPY ./requirements.lock /opt/fastapi_k8s/
RUN pip install pip --upgrade \
    && pip install -r /opt/fastapi_k8s/requirements.lock

COPY ./app/ /opt/fastapi_k8s/app/

ENV PYTHONPATH $WORKDIR
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
