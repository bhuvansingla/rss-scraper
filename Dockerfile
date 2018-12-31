FROM python:3
WORKDIR /myapp
ADD . /myapp
RUN pip install -r requirements.txt
CMD [ "python3", "code.py" ]
