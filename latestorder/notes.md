RUN python -m pip install --upgrade pip




FROM python:3-slim
# FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./order.py ./
CMD [ "python", "./order.py" ]




maybe can try this: https://www.architect.io/blog/2021-01-19/rabbitmq-docker-tutorial/