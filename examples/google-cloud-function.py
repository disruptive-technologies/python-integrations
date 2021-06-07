import os

from dtintegrations import data_connector, provider

DT_SIGNATURE_SECRET = os.getenv('DT_SIGNATURE_SECRET')


def endpoint(request):
    # Use the provider-specific validation function.
    event = data_connector.http_push.decode_request(
        request,
        provider_name=provider.GCLOUD,
        secret=DT_SIGNATURE_SECRET,
    )

    # Print the event data.
    print(event)

    # If all is well, return 200 response.
    return ('OK', 200)
