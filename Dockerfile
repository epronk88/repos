# start by pulling the python image
FROM python:3

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["test.py" ]












# apt 
#RUN apt-get update
#RUN apt-get -y install cron

# copy the requirements file into the image
#COPY ./requirements.txt /app/requirements.txt

# Setup cron to run every minute to print (you can add/update your cron here)
#RUN touch /var/log/cron-1.log
#RUN touch /var/log/cron-2.log

# cron >> /var/log/cron-1.log 2>&1
#RUN (crontab -l ; echo "* * * * * /usr/local/bin/python3 /app/test.py >> /var/log/cron-1.log 2>&1") | crontab

# switch working directory
#WORKDIR /app

# install the dependencies and packages in the requirements file
#RUN pip install -r requirements.txt

# copy every content from the local file to the image
#COPY . /app


# entrypoint.sh
#RUN chmod +x entrypoint.sh
#RUN chmod +x repeat.sh
#RUN chmod +x test.py

#CMD ["bash","entrypoint.sh"]


