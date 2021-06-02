

class Request(object):

    name: str = ''

    def __init__(self, request):
        # Set parameter attributes.
        self.request = request


class Flask(Request):

    name: str = 'flask'

    def __init__(self, request):
        # Inherit Request parent class.
        super().__init__(request)

    def get_headers(self):
        # Flask uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in self.request.headers:
            header_dict[key] = value
        return header_dict

    def get_body(self):
        # Flask has an attribute for body bytes.
        return self.request.data


class Gcloud(Request):

    name: str = 'gcloud'

    def __init__(self, request):
        # Inherit Request parent class.
        super().__init__(request)

    def get_headers(self):
        # gcloud uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in self.request.headers:
            header_dict[key] = value
        return header_dict

    def get_body(self):
        # gcloud has a convenience function for getting body bytes.
        return self.request.get_data()


class Lambda(Request):

    name: str = 'lambda'

    def __init__(self, request):
        # Inherit Request parent class.
        super().__init__(request)

    def get_headers(self):
        # Lambda headers can simply be returned.
        return self.request['headers']

    def get_body(self):
        # Lambda body is a string, to it must be encoded.
        return self.request['body'].encode('utf-8')


class Azure(Request):

    name: str = 'azure'

    def __init__(self, request):
        # Inherit Request parent class.
        super().__init__(request)

    def get_headers(self):
        # Azure headers can simply be returned.
        return self.request.headers

    def get_body(self):
        # Azure has a convenience function for getting body bytes.
        return self.request.get_body()


FLASK = Flask.name
GCLOUD = Gcloud.name
LAMBDA = Lambda.name
AZURE = Azure.name


PROVIDERS = [
    Flask,
    Gcloud,
    Lambda,
    Azure,
]


def _get_provider(name: str):
    # Iterate all known providers.
    for provider in PROVIDERS:
        # if name matches independent of casing, return provider.
        if provider.name == name.lower():
            return provider

    # If not match is found, raise an exception.
    raise ValueError(f'Unknown provider {name}.')
