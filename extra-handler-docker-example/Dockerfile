FROM jupyterhub/jupyterhub

RUN pip3 install notebook

RUN useradd -ms /bin/bash hubadmin
RUN echo hubadmin:password | chpasswd

RUN useradd -ms /bin/bash hubuser
RUN echo hubuser:password | chpasswd

#COPY ./jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py


CMD ["jupyterhub"]

