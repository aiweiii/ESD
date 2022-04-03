FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./place_order.py ./
COPY ./invokes.py ./
CMD [ "python", "./place_order.py" ]
