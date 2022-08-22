FROM python



RUN mkdir -p /home/flask-app
WORKDIR /home/flask-app
COPY . /home/flask-app
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1




CMD ["flask","run"]