FROM python:3.8

EXPOSE 5009

WORKDIR /flasklogin-tutorial

COPY requirements.txt /flasklogin-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flasklogin-tutorial

CMD python routes.py