Collecting information on projects in the extractives industry

Planning/info at https://docs.google.com/document/d/1B9pZnaIlD9c3LUTO2B4oSJsT_pN8UDMm9gSm3npNd5U/edit

# Server setup

```
sudo apt-get install python3-pip virtualenvwrapper git
bash ## start a new shell for virtualenvwrapper to start up
mkvirtualenv --python=/usr/bin/python3 resourcehulk
git clone https://github.com/danohuiginn/resourcehulk.git
cd resourcehulk
pip install -r requirements.txt
python manage.py runserver
```
