FROM python:3.9.4-slim

# Copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade setuptools pip
RUN pip3 install -r requirements.txt

# Use /app as a self-contained volume (unlike /usr/bin)
COPY . /app
VOLUME /app

# Any changes to docker-entrypoint.sh require rebuilding the container
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["prod"]
