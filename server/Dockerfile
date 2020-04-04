FROM python:alpine3.10
WORKDIR /bookStore
COPY requirements.txt .
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;
COPY . /bookStore
ENV PYTHONPATH "${PYTHONPATH}:/BookStore"
CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--py-autoreload=1", "--protocol=http", "-w", "wsgi:application"]