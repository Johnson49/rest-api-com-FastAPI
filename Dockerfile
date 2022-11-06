FROM python:alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./   

RUN chmod u+x script.sh

CMD [ "./script.sh" ]
