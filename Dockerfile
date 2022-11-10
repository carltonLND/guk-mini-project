FROM python:3.10.7
COPY . ./
VOLUME /data
RUN pip install -r requirements.txt
CMD python /src/app.py
