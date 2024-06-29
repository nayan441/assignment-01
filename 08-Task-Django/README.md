# Django API fetching data

This project is a Django-based REST API that provides migration of excel data in database and listing it through rest api.


## Setup



1. Create virtual environment and activate:

   ```bash
   virtualenv venv
   source venv/bin/activate (for Ubuntu)
   or
   .\venv\Script\activate  (for Windows)

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate

3. Run script:

   ```bash
   python3 manage.py runserver 8000

The API will be accessible at http://127.0.0.1:8000/.

## Migration API

Endpoint: /api/upload/

Method: POST

Request Payload: None

## Latest 10 record fetching  API

Endpoint: /api/latest-records/

Method: GET


