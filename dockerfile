FROM python:3.11-alpine
WORKDIR /tasker_multithreading
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/producer_consumer.py"]