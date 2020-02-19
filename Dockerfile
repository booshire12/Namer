# Docker file to create HTTP server for namer.py
FROM alpine:latest

RUN apk add --update py3-pip
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
COPY namer.py /usr/src/app/
COPY run_first.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Need to download all of the words
RUN python3 /usr/src/app/run_first.py

# Need to grab the nouns and adjectives
RUN python3 /usr/src/app/namer.py

EXPOSE 9977

CMD ["python3", "/usr/src/app/app.py"]
