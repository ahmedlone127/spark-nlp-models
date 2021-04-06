FROM ubuntu:latest
ENV   LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN apt update \
   
	&& apt install -y software-properties-common nano \
  
  	&& add-apt-repository ppa:deadsnakes/ppa \
    
	&& apt update -y \
  
	&& apt install -y python3.6 \
 
	&& apt install -y python3-pip 
    
RUN echo 'alias python=python3.6'  ~.bashrct 

ENV PYSPARK_PYTHON=usrbinpython3.6

RUN  apt-get install wget
RUN  apt-get install curl -y

# install selenium
RUN python3.6 -m pip install selenium
# Firefox browser to run the tests
RUN apt-get install -y firefox
 
# Gecko Driver
ENV GECKODRIVER_VERSION 0.23.0
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
  && rm -rf /opt/geckodriver \
  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \
  && chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \
  && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver \
  && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/wires

COPY . . 
CMD ["python3.6", "test.py"]