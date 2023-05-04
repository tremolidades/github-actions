FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
USER root

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
WORKDIR /code

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers" , "--workers", "1"]
