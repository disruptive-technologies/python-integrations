

class Request(object):

    def __init__(self, request):
        # Set parameter attributes.
        self.request = request


class Flask(Request):

    name = 'flask'

    @staticmethod
    def get_headers(request):
        # Flask uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in request.headers:
            header_dict[key] = value
        return header_dict

    def get_body(request):
        # Flask has an attribute for body bytes.
        return request.data


class Gcloud(Request):

    name = 'gcloud'

    @staticmethod
    def get_headers(request):
        # gcloud uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in request.headers:
            header_dict[key] = value
        return header_dict

    def get_body(request):
        # gcloud has a convenience function for getting body bytes.
        return request.get_data()


class Lambda(Request):

    name = 'lambda'

    @staticmethod
    def get_headers(request):
        # Lambda headers can simply be returned.
        return request['headers']

    def get_body(request):
        # Lambda body is a string, to it must be encoded.
        return request['body'].encode('utf-8')


FLASK = Flask.name
GCLOUD = Gcloud.name
LAMBDA = Lambda.name


PROVIDERS = [
    Flask,
    Gcloud,
    Lambda,
]


def _get_provider(name: str):
    # Iterate all known providers.
    for provider in PROVIDERS:
        # if name matches independent of casing, return provider.
        if provider.name == name.lower():
            return provider

    # If not match is found, raise an exception.
    raise ValueError(f'Unknown provider {name}.')
