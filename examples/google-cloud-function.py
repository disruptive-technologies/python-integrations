import os
from dtintegrations import data_connector, provider

DT_SIGNATURE_SECRET = os.getenv('DT_SIGNATURE_SECRET')


def endpoint(request):
    # Validate and decode the incoming request.
    payload = data_connector.HttpPush.from_provider(
        request=request,
        provider=provider.GCLOUD,
        secret=DT_SIGNATURE_SECRET,
    )

    # Print the event data.
    print(payload)

    # If all is well, return 200 response.
    return ('OK', 200)
