Collecting information on projects in the extractives industry

Planning/info at https://docs.google.com/document/d/1B9pZnaIlD9c3LUTO2B4oSJsT_pN8UDMm9gSm3npNd5U/edit

# Server setup

```
sudo apt-get install python3-pip virtualenvwrapper git 
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev python-dev 
sudo apt-get install postgresql-server-dev-9.1

bash ## start a new shell for virtualenvwrapper to start up
mkvirtualenv --python=/usr/bin/python3 resourcehulk
git clone https://github.com/danohuiginn/resourcehulk.git
cd resourcehulk
pip install -r requirements.txt
python manage.py runserver
```

Database setup

[For production, we're using connect.io. For dev, here's the local version]

```
sudo su - postgres
createuser -P # & follow instructions to make resourcehulk user
psql
psql> create database resourcehulk
psql> grant all privileges on database resourcehulk to resourcehulk
```

You may also need to modify postgres settings to not require peer authentication

# Details of the serv
