import tests.events as events


class GcloudRequestEmulator():

    def __init__(self, event: events.Event):

        self.headers = self.unpack_headers(event.headers)
        self.body_bytes = event.body_bytes.encode('utf-8')

    def unpack_headers(self, headers):
        header_list = []
        for key in headers:
            header_list.append((key, headers[key]))
        return header_list

    def get_data(self):
        return self.body_bytes


class HttpPushMock():

    def __init__(self, mocker):
        self._mocker = mocker

        self.event = None

        self.jwt_decode_patcher = self._mocker.patch(
            'jwt.decode',
            side_effect=self._patched_jwt_decode,
        )

    def _patched_jwt_decode(self, token: str, secret: str, algorithms: list):
        return self.event.payload
