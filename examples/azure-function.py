import os
import logging

import azure.functions as func
from dtintegrations import data_connector, provider

DT_SIGNATURE_SECRET = os.getenv('DT_SIGNATURE_SECRET')


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Use the provider-specific validation function.
    payload = data_connector.HttpPush.from_provider(
        request=req,
        provider=provider.AZURE,
        secret=DT_SIGNATURE_SECRET,
    )

    # Log the event data.
    logging.info(payload)

    # If all is well, return 200 response.
    return func.HttpResponse(
        "ruccess",
        status_code=200,
    )
