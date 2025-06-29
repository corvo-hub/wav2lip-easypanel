
FROM python:3.8-slim

RUN apt update && apt install -y ffmpeg git wget &&     apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install flask gdown

COPY . .

RUN mkdir -p static
RUN gdown https://drive.google.com/uc?id=1rwXWo6zH3Z4TxhGOa8vvdYUxAvbQ_C3A -O Wav2Lip.pth && \
    gdown https://drive.google.com/uc?id=1_0sVbZfhYg3AJ1FlYgKDoLRo3fqBzZbq -O face_detection/detection/s3fd.pth

CMD ["python", "app.py"]
