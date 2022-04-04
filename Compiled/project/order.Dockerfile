FROM python:3-slim
# FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN pip install pika
RUN python -m pip install pika
COPY ./order.py ./
CMD [ "python", "./order.py" ]
