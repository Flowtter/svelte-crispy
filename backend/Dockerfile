FROM python:3.8.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 1337

CMD [ "uvicorn", "src.app:app", "--reload", "--host", "0.0.0.0", "--port", "1337" ]
