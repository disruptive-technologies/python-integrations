import os
import json

from dtintegrations import data_connector, provider

DT_SIGNATURE_SECRET = os.getenv('DT_SIGNATURE_SECRET')


def lambda_handler(event, context):
    # Use the provider-specific validation function.
    e = data_connector.http_push.decode_request(
        event,
        provider_name=provider.LAMBDA,
        secret=DT_SIGNATURE_SECRET,
    )

    # Print the event data.
    print(e)

    # If all is well, return 200 response.
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "OK",
            }
        ),
    }
