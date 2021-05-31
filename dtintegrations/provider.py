

class Request(object):

    def __init__(self, request):
        # Set parameter attributes.
        self.request = request


class Flask(Request):

    name = 'flask'

    @staticmethod
    def get_headers(request):
        # Flask uses case-insensitive headers that needs no modification.
        return request.headers

    def get_body(request):
        # Flask has an attribute for body bytes.
        return request.data


class Gcloud(Request):

    name = 'gcloud'

    @staticmethod
    def get_headers(request):
        # gcloud uses case-insensitive headers that needs no modification.
        return request.headers

    def get_body(request):
        # gcloud has a convenience function for getting body bytes.
        return request.get_data()


FLASK = Flask.name
GCLOUD = Gcloud.name


PROVIDERS = [
    Flask,
    Gcloud,
]


def _get_provider(name: str):
    # Iterate all known providers.
    for provider in PROVIDERS:
        # if name matches independent of casing, return provider.
        if provider.name == name.lower():
            return provider

    # If not match is found, raise an exception.
    raise ValueError(f'Unknown provider {name}.')
