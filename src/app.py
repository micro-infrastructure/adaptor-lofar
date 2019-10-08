from http import HTTPStatus
from os import environ

from flask import Flask, request
from requests import post

from helpers import json_respone

### Config

proxy_host = environ['PROXY_HOST']
main_host = environ['MAIN_HOST']

### Flask

app = Flask(__name__)

@app.route('/lta2hpc', methods=['POST'])
def lta2hpc():
    payload = request.get_json()

    # Save original payload
    # ...

    # Overwrite webhook
    payload['webhook']['url'] = main_host + '/callback'

    # Call 'lofar-stage' service
    stage_endpoint = f'{proxy_host}/api/v1/function/lofar/stage'
    response = post(stage_endpoint, json=payload)

    # Save correlation id
    # ...
    
    result = {}
    return json_respone(result, HTTPStatus.ACCEPTED)

@app.route('/callback', methods=['POST'])
def callback():
    payload = request.get_json()

    # Retreive original payload
    # ..

    # Call 'srm2local' service
    stage_endpoint = f'{proxy_host}/api/v1/function/srm2local/execute'
    response = post(stage_endpoint, json=payload)
    
    result = {}
    return json_respone(result, HTTPStatus.OK)


### Main

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
