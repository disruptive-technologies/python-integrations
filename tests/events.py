

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
        'X-Dt-Signature': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGVja3N1bSI6IjVlM2ExZGRiNTE2ZTU1ZTdlMjc2MWYxNmE3ZWI2OGY3MWMwNmE4MmQiLCJleHAiOjE2NDE5ODQwNzIsImlhdCI6MTY0MTk4MDQ3MiwianRpIjoiYzdmYTRlNzdnZjg3ZWlmNmozdGcifQ.sAGby82i5uWE58Ce8QgeNZt50nvZoxb1wEjBJUBNEIM'  # noqa
    },
    body_str='{"event":{"eventId":"c7fa4e34fet12rl646l0","targetName":"projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg","eventType":"touch","data":{"touch":{"updateTime":"2022-01-12T09:41:12.108482Z"}},"timestamp":"2022-01-12T09:41:12.108482Z"},"labels":{"name":"touch"},"metadata":{"deviceId":"emuc17m6d7lq0bgk44smcqg","projectId":"c14u9p094l47cdv1o3pg","deviceType":"touch","productNumber":""}}',  # noqa
    body={'event': {'eventId': 'c7fa4e34fet12rl646l0', 'targetName': 'projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg', 'eventType': 'touch', 'data': {'touch': {'updateTime': '2022-01-12T09:41:12.108482Z'}}, 'timestamp': '2022-01-12T09:41:12.108482Z'}, 'labels': {'name': 'touch'}, 'metadata': {'deviceId': 'emuc17m6d7lq0bgk44smcqg', 'projectId': 'c14u9p094l47cdv1o3pg', 'deviceType': 'touch', 'productNumber': ''}},  # noqa
    payload={'checksum': '5e3a1ddb516e55e7e2761f16a7eb68f71c06a82d', 'exp': 1641984072, 'iat': 1641980472, 'jti': 'c7fa4e77gf87eif6j3tg'},  # noqa
)
