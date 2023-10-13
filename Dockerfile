FROM python:3.8.0

# set the working environment
WORKDIR /app

# install dependecies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the scripts to the folder
COPY . /app

# start the server 
CMD ["uvicorn","API:app","--host","0.0.0.0", "--port","80"]
# CMD ["uvicorn","API:app", "--port","80"]