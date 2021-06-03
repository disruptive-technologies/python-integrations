

class Event():

    def __init__(self, headers: dict, body_bytes: bytes, body: dict):
        self.headers: dict = headers
        self.body_bytes: bytes = body_bytes
        self.body: dict = body


touch = Event(
    headers={
        'x-dt-signature': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGVja3N1bSI6ImE4OTUyNGM3YzVlZDVmYjIyYzM4N2MxY2U3ODhlYzY3OGY2NDZiMzciLCJleHAiOjE2MjI3MTc0MTksImlhdCI6MTYyMjcxMzgxOSwianRpIjoiYzJzYWJtbzE3djI1c3ZlcHBlYTAifQ.fefieBRAcPs2w8_QdtomyWP2yUiIvpUU1CYVTw6NJV8'  # noqa
    },
    body_bytes='{"event":{"eventId":"c2sabmqhed3n71nk63dg","targetName":"projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg","eventType":"touch","data":{"touch":{"updateTime":"2021-06-03T09:50:19.216064Z"}},"timestamp":"2021-06-03T09:50:19.216064Z"},"labels":{"name":"touch"}}',  # noqa
    body={'event': {'eventId': 'c2sabmqhed3n71nk63dg', 'targetName': 'projects/c14u9p094l47cdv1o3pg/devices/emuc17m6d7lq0bgk44smcqg', 'eventType': 'touch', 'data': {'touch': {'updateTime': '2021-06-03T09:50:19.216064Z'}}, 'timestamp': '2021-06-03T09:50:19.216064Z'}, 'labels': {'name': 'touch'}}  # noqa
)
