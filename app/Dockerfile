FROM python:3.10.0-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
RUN apk add netcat-openbsd
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# COPY . .

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]

# COPY ./entrypoint.sh /
# ENTRYPOINT ["sh", "/entrypoint.sh"]

