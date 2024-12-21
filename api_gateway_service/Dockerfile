FROM python:3.12-slim

WORKDIR /urbancart/app

COPY ./api_gateway_service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./common /urbancart/app/common

COPY ./api_gateway_service .

CMD [ "python", "app.py" ]
