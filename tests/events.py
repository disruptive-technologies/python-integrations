

class Event():

    def __init__(self,
                 headers: dict,
                 body_str: str,
                 body: dict,
                 payload: dict):

        self.headers: dict = headers
        self.body_str: str = body_str
        self.body: dict = body
        self.payload: dict = payload


touch = Event(
    headers={
        'X-Dt-Signature': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGVja3N1bSI6ImYyYjVkYzA0OTY0MzcyMDFkM2NlZTE1NmMyMzNhMTMzNTYwM2Q0NjUiLCJjaGVja3N1bV9zaGEyNTYiOiJhZmQ4MWExNmJiOWMwNzZlNTdmOTI3MjhmMjg0ZmY1NTgzMWJmZGYxZDNjMmMxMGI4MzM1NjdmNTIxZDc4MmRlIiwiZXhwIjoxNjQ0NTAwNTMzLCJpYXQiOjE2NDQ0OTY5MzMsImp0aSI6ImM4MmdnOTloZ2EzNWpjMmFma2VnIn0.gm8m_HrhlOnAyS08CfR_RNYdZQIpGV6E8bk3UiAR3uo'  # noqa
    },
    body_str='{"event":{"eventId":"c82gg9catj3vmh4248og","targetName":"projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg","eventType":"touch","data":{"touch":{"updateTime":"2022-02-10T12:42:13.313949Z"}},"timestamp":"2022-02-10T12:42:13.313949Z"},"labels":{"name":"touch"},"metadata":{"deviceId":"emuc17m6d7lq0bgk44smcqg","projectId":"c14u9p094l47cdv1o3pg","deviceType":"touch","productNumber":""}}',  # noqa
    body={'event': {'eventId': 'c82gg9catj3vmh4248og', 'targetName': 'projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg', 'eventType': 'touch', 'data': {'touch': {'updateTime': '2022-02-10T12:42:13.313949Z'}}, 'timestamp': '2022-02-10T12:42:13.313949Z'}, 'labels': {'name': 'touch'}, 'metadata': {'deviceId': 'emuc17m6d7lq0bgk44smcqg', 'projectId': 'c14u9p094l47cdv1o3pg', 'deviceType': 'touch', 'productNumber': ''}},  # noqa
    payload={'checksum': 'f2b5dc0496437201d3cee156c233a1335603d465', 'checksum_sha256': 'afd81a16bb9c076e57f92728f284ff55831bfdf1d3c2c10b833567f521d782de', 'exp': 1644500533, 'iat': 1644496933, 'jti': 'c82gg99hga35jc2afkeg'},  # noqa
)

metadata = {
    'deviceId': 'test-device',
    'projectId': 'test-project',
    'deviceType': 'testDevice',
    'productNumber': 'testProductNumber',
}
