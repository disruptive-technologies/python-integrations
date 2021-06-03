import os
from flask import Flask, request  # pip install flask

from dtintegrations import data_connector, provider

app = Flask(__name__)


@app.route('/', methods=['POST'])
def print_request_contents():
    # Use the provider-specific validation function.
    event = data_connector.http_push.validate(
        request,
        provider_name=provider.FLASK,
        secret=os.getenv('DT_SIGNATURE_SECRET'),
    )

    # Print the event data.
    print(event)

    # If all is well, return 200 response.
    return 'Success'
