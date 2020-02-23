FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter
COPY . /code/
RUN apt -y update && apt -y install cron

# Copy hello-cron file to the cron.d directory
RUN cp ./update-services-cron /etc/cron.d/update-services-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/update-services-cron

# Apply cron job
RUN crontab /etc/cron.d/update-services-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

#Initial migrations 
CMD python ./manage.py migrate
