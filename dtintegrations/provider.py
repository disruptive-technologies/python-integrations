

class Request(object):

    def __init__(self, request):
        # Set parameter attributes.
        self.request = request


class Flask(Request):

    name = 'flask'

    @staticmethod
    def get_header(request, name: str):
        # Iterate headers in request.
        for key, value in request.headers:
            # If the header name matches regardless of casing, return value.
            if key.lower() == name.lower():
                return request.headers[key]

        # If header does not exist, raise an exception.
        raise KeyError(f'Header {name} does not exist.')

    def get_body(request):
        # Flask comes with a convenient function for getting the body.
        return request.data


class Gcloud(Request):

    name = 'gcloud'

    @staticmethod
    def get_header(request, name: str):
        # Iterate headers in request.
        for key, value in request.headers:
            # If the header name matches regardless of casing, return value.
            if key.lower() == name.lower():
                return request.headers[key]

        # If header does not exist, raise an exception.
        raise KeyError(f'Header {name} does not exist.')

    def get_body(request):
        # Flask comes with a convenient function for getting the body.
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
