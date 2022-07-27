FROM python:3.9

RUN mkdir -p /pytest_wix
WORKDIR      /pytest_wix

# ENV PYTHONPATH /pytest_wix

# install chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    unzip

# install chromedriver
#RUN CHROME_VERSION=$(google-chrome --product-version | head -c2) \
# && DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") \
# && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip
#RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# install requirements
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt