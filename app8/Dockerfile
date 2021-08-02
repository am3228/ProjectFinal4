FROM python:3.9

EXPOSE 5007

WORKDIR /app8

COPY requirements.txt /app8
RUN pip install  -r requirements.txt --upgrade pip

COPY . /app8

CMD python app.py