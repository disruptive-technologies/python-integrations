import tests.events as events


class GcloudRequestMock():

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
