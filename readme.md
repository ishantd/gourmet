LIVE DEMO : https://ishant.aadhaarmitr.tech/

# SETUP


## Setup Docker for LOCAL SETUP

- Clone the repository <br/>
  `git clone https://github.com/ishantd/gourmet.git`

- Verify that your docker service is running and configured <br/>
  `docker-compose run hello-world`

- Start development server for all services <br/>
  `docker-compose up`

- Build the containers and processes required to start Docker (NOTE: This command should be used only once, when retrying to build the docker image/container please use `docker-compose up --build`)<br/>
  `docker-compose build`

NOTE: PLEASE ASK FOR .env FILE  CREDENTIALS TO RUN THE CODE

#### Clone
- [x] `git clone https://github.com/ishantd/portfolio.git`

- [x] `cd gourmet`

- [x] Install required libraries and dependencies <br/>
        `sudo apt-get update -y && sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib python3-venv nginx -y`

### Create Virtual Env (Preferred)
bash/shell
- [x] `python3 -m venv env` or `virtualenv env`
switch to virtual environment 
- [x] `source env/bin/activate`
##### Install dependencies 
- [x] `pip3 install -r requirements.txt`

### Django setup

##### To run dev server
- [x] `python3 manage.py runserver`

To setup up database go to `settings.py` 

- [x] modify this code with your username (Linux/Mac)

```
if 'Your Username' in os.getcwd():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            # 'NAME': os.path.join(BASE_DIR, 'serverdb.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': os.path.join(BASE_DIR, 'serverdb.sqlite3'),
        }
    }
```

- [x] Navigate to http://127.0.0.1:8000 to view dev server


Server Setup:


sudo nano /etc/systemd/system/main.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ishant
Group=www-data
WorkingDirectory=/home/ishant/gourmet/main
ExecStart=/home/ishant/gourmet/main/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ishant/gourmet/main.sock gourmet.wsgi:application

[Install]
WantedBy=multi-user.target

sudo nano /etc/nginx/sites-available/gourmet

server {
    listen 80;
    server_name ishant.aadhaarmitr.tech ;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ishant/gourmet/main;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ishant/gourmet/main.sock;
    }

    location /media/ {
        alias /home/ishant/gourmet/main/media/;
    }
}

sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled

#### To restart server
sudo pkill gunicorn
sudo systemctl daemon-reload
sudo systemctl start gourmet
sudo systemctl restart nginx
sudo systemctl restart gourmet.service




python3 manage.py collectstatic --no-input