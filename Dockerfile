# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.3-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# add os dependecies
RUN apk add --no-cache python3 python3-dev \
    py3-cffi zlib-dev gcc jpeg-dev \
    linux-headers libressl-dev \
    libxml2-dev libxslt-dev \
    musl-dev postgresql-dev \
    libffi-dev openssl-dev mariadb-dev \
    g++ unixodbc-dev

# Install pip requirements
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn psycopg2

WORKDIR /app
ADD . /app

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "asapi.wsgi:application", "--reload"]