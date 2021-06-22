FROM python:3.9

ENV PATH="/scripts:${PATH}"

ADD . /code
WORKDIR /code

COPY poetry.lock pyproject.toml /tmp/


RUN pip install poetry
RUN cd /tmp && poetry export -f requirements.txt --output /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN  adduser --disabled-password user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user


CMD ["entrypoint.sh"]