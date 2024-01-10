
# Vehicle API And Notes API

This is a simple Vehicle API built with Django and Django Rest Framework


## Setup and Installation


Clone the repository:
git clone https://github.com/username/repository.git

Navigate into the project directory:
cd repository

Set up virtual environment and activate it:
For Windows:
`python -m venv venv`
`venv\Scripts\activate`

For Linux/Mac:
`python3 -m venv venv`
`source venv/bin/activate`

Install the required dependencies:
`pip install -r requirements.txt`

Apply migrations:
`python manage.py makemigrations`
`python manage.py migrate`

Run the server:
`python manage.py runserver`

Important URLs
`http://127.0.0.1:8000/swagger/`: This gives the entire list of urls and endpoints in swagger doc

`http://127.0.0.1:8000/api-vehicle/vehicles/`: Vehicle API
`http://127.0.0.1:8000/api/notes/`: Notes API
