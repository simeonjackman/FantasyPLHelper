FROM python:3.8 

# set workdir to /app
WORKDIR /app

# copy everything
ADD . ./app
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# deploy
CMD ["python","main.py"]


