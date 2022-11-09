FROM python:3.10.7
WORKDIR /application
COPY . ./
VOLUME /application/data
RUN pip install -r requirements.txt
CMD python /application/src/app.py
