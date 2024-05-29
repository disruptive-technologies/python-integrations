

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

temperature = Event(
    headers={
        'X-Dt-Signature': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGVja3N1bSI6IjBmNzUzOTM5YTEzNzdhM2M5NGFiZDJjZmViZGMyY2I0NzU2YzNmYzMiLCJjaGVja3N1bV9zaGEyNTYiOiI1YjVmYzJlN2M3NjM3YWIzN2RiNDJiNzQ1YmY2ZjEyOWZhZTk3ODJmOTUzZWQzZGM2NDM1YzMyMTQ4ZjQxNWQ0IiwiZXhwIjoxNzE2OTgyNDQzLCJpYXQiOjE3MTY5Nzg4NDMsImp0aSI6ImNwYmc5NnQxaXNqbHIydmRvcmMwIn0.A4r91SKDW4IqYtb1eXuTQCUxM6GnouPbt94Ywd-vCpU' # noqa
    },
    body_str='{"event":{"eventId":"cpbg96qngr7ai7ldarrg","targetName":"projects/ccol8iuk9smqiha4e8l0/devices/emucdd6ef2eu277bo8f52vg","eventType":"temperature","data":{"temperature":{"value":27,"updateTime":"2024-05-29T10:34:03.970415Z","samples":[{"value":27,"sampleTime":"2024-05-29T10:34:03.970415Z"}],"isBackfilled":false}},"timestamp":"2024-05-29T10:34:03.970415Z"},"labels":{"name":"test temp"},"metadata":{"deviceId":"emucdd6ef2eu277bo8f52vg","projectId":"ccol8iuk9smqiha4e8l0","deviceType":"temperature","productNumber":""}}', # noqa
    body={'event':{'eventId':'cpbg96qngr7ai7ldarrg','targetName':'projects/ccol8iuk9smqiha4e8l0/devices/emucdd6ef2eu277bo8f52vg','eventType':'temperature','data':{'temperature':{'value':27,'updateTime':'2024-05-29T10:34:03.970415Z','samples':[{'value':27,'sampleTime':'2024-05-29T10:34:03.970415Z'}],'isBackfilled':False}},'timestamp':'2024-05-29T10:34:03.970415Z'},'labels':{'name':'test temp'},'metadata':{'deviceId':'emucdd6ef2eu277bo8f52vg','projectId':'ccol8iuk9smqiha4e8l0','deviceType':'temperature','productNumber':''}}, # noqa
    payload={'checksum': '0f753939a1377a3c94abd2cfebdc2cb4756c3fc3', 'checksum_sha256': '5b5fc2e7c7637ab37db42b745bf6f129fae9782f953ed3dc6435c32148f415d4', 'exp': 1716982443, 'iat': 1716978843, 'jti': 'cpbg96t1isjlr2vdorc0'}, # noqa
)

metadata = {
    'deviceId': 'test-device',
    'projectId': 'test-project',
    'deviceType': 'testDevice',
    'productNumber': 'testProductNumber',
}
