# 10kchallenge
Application to fetch data from SEC EDGAR

#Install

git clone https://github.com/superposition/10kchallenge.git

cd 10kchallenge/10k

source ./bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser 

python manage.py runserver
