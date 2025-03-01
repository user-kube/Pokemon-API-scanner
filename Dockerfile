FROM alpine:latest

RUN apk add --no-cache python3 py3-pip python3-dev

WORKDIR /app

COPY . .

RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt

CMD ["venv/bin/python", "main.py"]
