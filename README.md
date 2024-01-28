# WikiPedia_scraper_Django

## Installing
Step by step commands on how to run this project on your computer.

1)- Install Virtualenv
```
pip install virtualenv
```
2)- Create Virtualenv
```
virtualenv venv
```
3)- Activate virtual env
```
source env/bin/activate
```
4)- Install requirements
```
pip install -r requirements.txt
```
Note: Above lines are required for first time installation.
5)- Execute below commands
```
python manage.py makemigrations
python manage.py migrate
```
Note: Above commands should be executed if there is any db level changes

6)- Create superuser for admin access and follow instruction, if not created one
```
python manage.py createsuperuser
```
## Running the server
```
python manage.py runserver
```
And the project is ready for use on your computer!.
## ScreenShot of the project
# api page:
<img width="1440" alt="Screenshot 2023-06-30 at 11 46 53 PM" src="https://github.com/Ajyrajput-2811/WikiPedia_scraper_Django/assets/119350384/1f1bb0ff-3871-4676-8bd7-a7e98322505a">

# home page:
<img width="1440" alt="Screenshot 2023-06-30 at 11 45 11 PM" src="https://github.com/Ajyrajput-2811/WikiPedia_scraper_Django/assets/119350384/248640e1-c2b2-4954-80e2-52d79e6d36b4">

# Django Admin:
<img width="1440" alt="Screenshot 2023-06-30 at 11 47 07 PM" src="https://github.com/Ajyrajput-2811/WikiPedia_scraper_Django/assets/119350384/6fc69777-0907-4f31-8136-ae11b7d8d7fc">

# Scrap Data:
<img width="1440" alt="Screenshot 2023-06-30 at 11 48 41 PM" src="https://github.com/Ajyrajput-2811/WikiPedia_scraper_Django/assets/119350384/418ce4d3-41be-4825-8ad9-7c3a77b61ee7">




