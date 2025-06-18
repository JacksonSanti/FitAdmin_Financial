FROM python:3.9-slim

WORKDIR /financial

COPY requirements.txt /financial/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50052

CMD ["python", "server_grpc.py"]
