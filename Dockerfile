FROM python:3-alpine
EXPOSE 5000
WORKDIR /srv
ADD Procfile requirements.txt src/ /srv/
RUN pip install -r requirements.txt
ENTRYPOINT ["honcho", "start"]
