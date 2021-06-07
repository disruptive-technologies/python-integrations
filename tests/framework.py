import tests.events as events


class FlaskRequestFormat():
    """
    Change event data to replicate Flask request format.

    """

    def __init__(self, event: events.Event):

        self.headers = self._unpack_headers(event.headers)
        self.data = event.body_str.encode('utf-8')

    def _unpack_headers(self, headers):
        header_list = []
        for key in headers:
            header_list.append((key, headers[key]))
        return header_list


class DjangoRequestFormat():
    """
    Change event data to replicate Django request format.

    """

    def __init__(self, event: events.Event):

        self.headers = event.headers
        self.body = event.body_str.encode('utf-8')


class GcloudRequestFormat():
    """
    Change event data to replicate Gcloud request format.

    """

    def __init__(self, event: events.Event):

        self.headers = self._unpack_headers(event.headers)
        self.body_bytes = event.body_str.encode('utf-8')

    def _unpack_headers(self, headers):
        header_list = []
        for key in headers:
            header_list.append((key, headers[key]))
        return header_list

    def get_data(self):
        return self.body_bytes


def lambda_request_format(event: events.Event):
    """
    Change event data to replicate Lambda request format.

    """

    return {
        'headers': event.headers,
        'body': event.body_str,
    }


class AzureRequestFormat():
    """
    Change event data to replicate Azure request format.

    """

    def __init__(self, event: events.Event):

        self.headers = event.headers
        self.body_bytes = event.body_str.encode('utf-8')

    def get_body(self):
        return self.body_bytes


class DecodeMock():

    def __init__(self, mocker):
        self._mocker = mocker

        self.event = None

        self.jwt_decode_patcher = self._mocker.patch(
            'jwt.decode',
            side_effect=self._patched_jwt_decode,
        )

    def _patched_jwt_decode(self, token: str, secret: str, algorithms: list):
        return self.event.payload
