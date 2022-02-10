import os
import json

from dtintegrations import data_connector, provider

DT_SIGNATURE_SECRET = os.getenv('DT_SIGNATURE_SECRET')


def lambda_handler(event, context):
    # Use the provider-specific validation function.
    payload = data_connector.HttpPush.from_provider(
        request=event,
        provider=provider.LAMBDA,
        secret=DT_SIGNATURE_SECRET,
    )

    # Print the payload data.
    print(payload)

    # If all is well, return 200 response.
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "OK",
            }
        ),
    }
