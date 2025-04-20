FROM python:3.12-slim

WORKDIR /urbancart

COPY ./user_service/requirements.txt /urbancart/user_service/

RUN pip install --no-cache-dir -r /urbancart/user_service/requirements.txt

COPY ./common /urbancart/common/

COPY ./user_service /urbancart/user_service/

ENV PYTHONPATH="/urbancart:${PYTHONPATH}"

WORKDIR /urbancart/user_service/

CMD ["python", "run.py"]
