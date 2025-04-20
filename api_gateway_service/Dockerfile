FROM python:3.12-slim

WORKDIR /urbancart/

COPY ./api_gateway_service/requirements.txt /urbancart/api_gateway_service/

RUN pip install --no-cache-dir -r /urbancart/api_gateway_service/requirements.txt

COPY ./common /urbancart/common/

COPY ./api_gateway_service /urbancart/api_gateway_service/

ENV PYTHONPATH="/urbancart:${PYTHONPATH}"

WORKDIR /urbancart/api_gateway_service/

CMD ["python", "run.py"]
