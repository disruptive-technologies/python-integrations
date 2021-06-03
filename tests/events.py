

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
        'x-dt-signature': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGVja3N1bSI6ImE4MTA3ODRkMTNkMThkN2M5ZDU5MzdkNDZlYWM4Nzc0OTZhMTQxOTMiLCJleHAiOjE2MjI3MjI5MjksImlhdCI6MTYyMjcxOTMyOSwianRpIjoiYzJzYm1vOTU2ODNpaWt1dThzdmcifQ.wAhA56Z9YovhvHHU017qDLrcHT2IjzTwTPQL-b3VIlc'  # noqa
    },
    body_str='{"event":{"eventId":"c2sbmoahed3n71nk69sg","targetName":"projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg","eventType":"touch","data":{"touch":{"updateTime":"2021-06-03T11:22:09.431599Z"}},"timestamp":"2021-06-03T11:22:09.431599Z"},"labels":{"name":"touch"}}',  # noqa
    body={'event': {'eventId': 'c2sbmoahed3n71nk69sg', 'targetName': 'projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg', 'eventType': 'touch', 'data': {'touch': {'updateTime': '2021-06-03T11:22:09.431599Z'}}, 'timestamp': '2021-06-03T11:22:09.431599Z'}, 'labels': {'name': 'touch'}},  # noqa
    payload={'checksum': 'a810784d13d18d7c9d5937d46eac877496a14193', 'exp': 1622722929, 'iat': 1622719329, 'jti': 'c2sbmo95683iikuu8svg'},  # noqa
)
