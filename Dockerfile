FROM python:3.12.0-slim

# Install python and kafka dependencies

WORKDIR /scripts

RUN pip install confluent-kafka

COPY ./create_topic.py /scripts/create_topic.py

ENTRYPOINT ["python3", "/scripts/create_topic.py"]