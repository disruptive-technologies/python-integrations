

FLASK = 'flask'
GCLOUD = 'gcloud'
LAMBDA = 'lambda'
AZURE = 'azure'
PROVIDERS = [
    FLASK,
    GCLOUD,
    LAMBDA,
    AZURE,
]


class Flask():

    name: str = FLASK

    @staticmethod
    def get_headers_dict(request):
        # Flask uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in request.headers:
            header_dict[key] = value
        return header_dict

    @staticmethod
    def get_body_bytes(request):
        # Flask has an attribute for body bytes.
        return request.data


class Gcloud():

    name: str = GCLOUD

    @staticmethod
    def get_headers_dict(request):
        # gcloud uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in request.headers:
            header_dict[key] = value
        return header_dict

    @staticmethod
    def get_body_bytes(request):
        # gcloud has a convenience function for getting body bytes.
        return request.get_data()


class Lambda():

    name: str = LAMBDA

    @staticmethod
    def get_headers_dict(request):
        # Lambda headers can simply be returned.
        return request['headers']

    @staticmethod
    def get_body_bytes(request):
        # Lambda body is a string, to it must be encoded.
        return request['body'].encode('utf-8')


class Azure():

    name: str = AZURE

    @staticmethod
    def get_headers_dict(request):
        # Azure headers can simply be returned.
        return request.headers

    @staticmethod
    def get_body_bytes(request):
        # Azure has a convenience function for getting body bytes.
        return request.get_body()
