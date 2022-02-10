import os
from flask import Flask, request  # pip install flask

from dtintegrations import data_connector, provider

app = Flask(__name__)


@app.route('/', methods=['POST'])
def print_request_contents():
    # Use the provider-specific validation function.
    payload = data_connector.HttpPush.from_provider(
        request=request,
        provider=provider.FLASK,
        secret=os.getenv('DT_SIGNATURE_SECRET'),
    )

    # Print the payload data.
    print(payload)

    # If all is well, return 200 response.
    return 'Success'
