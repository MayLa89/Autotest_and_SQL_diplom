import string

import data
import configuration
import requests


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def order_creation(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


def get_order_track():
    response = order_creation(data.order_body)
    return response.json().get('track')


def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.PICK_ORDER + str(track))
