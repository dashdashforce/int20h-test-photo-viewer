FROM python:3.7-slim
RUN apt-get update \
    && apt-get install -y make

COPY . /backend
WORKDIR /backend

RUN pip install -r requirements.txt

EXPOSE 8888

ENTRYPOINT ["python3", "run.py"]