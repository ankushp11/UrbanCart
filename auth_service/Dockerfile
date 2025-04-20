FROM python:3.12-slim

WORKDIR /urbancart

COPY ./auth_service/requirements.txt /urbancart/auth_service/

RUN pip install --no-cache-dir -r /urbancart/auth_service/requirements.txt

COPY ./common /urbancart/common/

COPY ./auth_service /urbancart/auth_service/

ENV PYTHONPATH="/urbancart:${PYTHONPATH}"

WORKDIR /urbancart/auth_service/

RUN chmod +x /urbancart/common/commands/run_migrations.sh

CMD ["sh", "-c", "/urbancart/common/commands/run_migrations.sh && python run.py"]
