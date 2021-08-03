FROM python:3.8

EXPOSE 5010

WORKDIR /flask_session_tutorial

COPY requirements.txt /flask_session_tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY ../.. /flask_session_tutorial

CMD python routes.py