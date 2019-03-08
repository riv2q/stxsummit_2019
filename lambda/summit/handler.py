import json

import requests


def hello(event, context):
    stxnext_response = requests.get("https://stxnext.com")

    body = {
        "message": "Hello Summit 2019!",
        "stxnext_webpage_status": stxnext_response.status_code
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
