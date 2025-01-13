FROM python:3.9

RUN pip install pandas requests beautifulsoup4

WORKDIR /app

ENTRYPOINT ['python' 'scraper.py']