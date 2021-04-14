FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTOCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8002

CMD ./manage.py runserver 0.0.0.0:8002
