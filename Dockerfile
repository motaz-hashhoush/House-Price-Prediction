FROM python:3.9-slim-buster
# make a Dir for the app
WORKDIR /flask-app

# install requirments
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy source code
COPY /flask-app .

# port
EXPOSE 8081

# run the app
CMD [ "python", "main.py"]