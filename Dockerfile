FROM python:3.8

WORKDIR /owdb

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /owdb/requirements.txt
RUN pip install -r requirements.txt

COPY . /owdb

CMD [ "python3", "/owdb/app.py"]
