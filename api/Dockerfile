FROM python:3.4

WORKDIR /ddl2

COPY requirements.txt /ddl2
RUN pip install -r requirements.txt

COPY . /ddl2
CMD python manage.py runserver 0.0.0.0:8000