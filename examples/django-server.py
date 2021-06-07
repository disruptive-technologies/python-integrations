import os
from django.http import HttpResponse  # pip install django
from django.views.decorators.csrf import csrf_exempt

from dtintegrations import data_connector, provider


@csrf_exempt
def index(request):
    # Use the provider-specific validation function.
    event = data_connector.http_push.decode_request(
        request,
        provider=provider.DJANGO,
        secret=os.getenv('DT_SIGNATURE_SECRET'),
    )

    # Print the event data.
    print(event)

    # If all is well, return 200 response.
    return HttpResponse('success')
