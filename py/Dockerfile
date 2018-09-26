FROM python:3
RUN mkdir /usr/app
WORKDIR /user/app
RUN pip install flask gunicorn
COPY app.py app.py
ENTRYPOINT ["gunicorn","-w","1","app:app","-b","0.0.0.0:8000"]