FROM fnndsc/ubuntu-python3

RUN apt-get update && \
    apt install -y curl && \
    mkdir temp && \
    curl https://bootstrap.pypa.io/get-pip.py -o temp/get-pip.py && \
    python temp/get-pip.py && \
    rm -rf temp && \
    pip install Flask && \
    pip install pykafka

COPY . /app

ENTRYPOINT [ "python", "app/app.py" ]