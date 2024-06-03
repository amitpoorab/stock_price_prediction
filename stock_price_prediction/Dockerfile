FROM python:3.9.5

# set up location of code
WORKDIR /
ENV PYTHONPATH=/src

# install cron
RUN apt-get update && apt-get install cron -y

# install requirements
COPY ./stock_price_prediction/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY ./ /
 
# Run cron
CMD cron && tail -f /var/log/cron.log

# Command to fetch the data
#CMD ["python", "your_main_script.py"]