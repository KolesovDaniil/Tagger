FROM python:3.7.9
COPY . /opt/tagger
WORKDIR /opt/tagger
EXPOSE 6060
RUN pip install -r requirements.txt
CMD ["python", "manage.py"]