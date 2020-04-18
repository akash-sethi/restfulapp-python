#setup

- python3 -m venv ~/project_location
- activate virtual environment
- git clone https://github.com/akash-sethi/restfulapp-python.git
- cd restfulapp
- pip install -r requirements.txt
- install/run postgres server
- update DATABASES config in settings.py with your preferences
- python manage.py runserver