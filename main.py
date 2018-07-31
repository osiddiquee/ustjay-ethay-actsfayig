import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    request_url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    fact = get_fact()

    response = requests.post(request_url,
                             data = {'input_text': fact},
                             allow_redirects = False)

    if response.status_code != 302:
        print('Oops. There is an error in your request.')

    location_header = response.headers['Location']

    return location_header


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
