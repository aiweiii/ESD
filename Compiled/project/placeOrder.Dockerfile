FROM python:3-slim
WORKDIR /usr/src/app
ENV PYTHONPATH "${PYTHONPATH}:/app/"
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./invokes.py ./amqp_setup.py ./place_order.py ./
CMD [ "python", "./place_order.py" ]
