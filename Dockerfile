FROM python:3.10.4-slim-buster

RUN useradd --create-home --shell /bin/bash app_user

# Working Directory
WORKDIR /home/app_user

COPY requirements.txt ./

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

USER app_user

# Copy source code to working directory
COPY . .

CMD [ "python", "cli.py"]
