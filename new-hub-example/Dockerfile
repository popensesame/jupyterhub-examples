FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

# Make some users
RUN useradd -ms /bin/bash hubadmin
RUN echo hubadmin:password | chpasswd
RUN useradd -ms /bin/bash hubuser
RUN echo hubuser:password | chpasswd

# Install dependencies
RUN apt update && \
		apt install -y \
			curl \
			nodejs \
			npm \
			python3 \
			python3-distutils

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
		python3 get-pip.py && \
		rm get-pip.py

# Install jupyterhub dependencies
RUN npm install -g configurable-http-proxy

# Install StochSS dependencies
RUN pip install \ 
			jupyterhub \
			notebook \
			gillespy2

CMD ["jupyterhub"]

