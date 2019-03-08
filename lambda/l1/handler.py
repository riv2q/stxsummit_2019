import json

import requests


def hello(event, context):
    stx_status = requests.get('https://stxnext.com').status_code
    body = {
        "message": "STX Web Page status: {status}".format(status=stx_status),
        "event": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
