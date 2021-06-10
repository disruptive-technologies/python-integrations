import os
import logging

import azure.functions as func
from dtintegrations import data_connector, provider

DT_SIGNATURE_SECRET = os.getenv('DT_SIGNATURE_SECRET')


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Use the provider-specific validation function.
    event, labels = data_connector.http_push.decode_request(
        req,
        provider=provider.AZURE,
        secret=DT_SIGNATURE_SECRET,
    )

    # Log the event data.
    logging.info(event)

    # If all is well, return 200 response.
    return func.HttpResponse(
        "ruccess",
        status_code=200,
    )
