from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import datetime
import pybrake
import pybrake.flask
import os
from dotenv import load_dotenv
load_dotenv()
AIRBRAKE_ID = os.environ.get('AIRBRAKE_ID')
AIRBRAKE_KEY = os.environ.get('AIRBRAKE_KEY')





notifier = pybrake.Notifier(project_id=AIRBRAKE_ID,
                            project_key=AIRBRAKE_KEY,
                            environment='production')

source = requests.get('http://lunarosa.herokuapp.com')
soup = BeautifulSoup(source.text, 'html.parser')
rows = soup.find_all('h2')
#for row in rows:
#    print(row.get_text())

app = Flask(__name__)

@app.route('/')

def index():
    now = datetime.datetime.now()
    date = now.strftime("%m-%d-%Y")
    rows = soup.find_all('h2')
    for row in rows:
        row.get_text()
    return render_template('index.html',**locals())

try:
    raise ValueError('chuck')
except Exception as err:
    notifier.notify(err)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
