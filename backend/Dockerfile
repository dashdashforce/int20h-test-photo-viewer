FROM python:3.7-slim
RUN apt-get update \
    && apt-get install -y make

COPY . /backend
WORKDIR /backend

RUN pip install -r requirements/prod.txt

EXPOSE 8888

ENTRYPOINT ["python3", "run.py"]