FROM python:3.12-slim

WORKDIR /urbancart

COPY ./auth_service/requirements.txt /urbancart/app/

RUN pip install --no-cache-dir -r /urbancart/app/requirements.txt

COPY ./common /urbancart/common

COPY ./auth_service /urbancart/app/

ENV PYTHONPATH="/urbancart:${PYTHONPATH}"

WORKDIR /urbancart/app

RUN chmod +x /urbancart/common/commands/run_migrations.sh

CMD ["sh", "-c", "/urbancart/common/commands/run_migrations.sh && python app.py"]
