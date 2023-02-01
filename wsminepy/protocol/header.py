class Header(object):
    def __init__(self, messagePurpose: str, requestId: str, version: int) -> None:
        self.messagePurpose = messagePurpose
        self.requestId = requestId
        self.version = version


def to_header(data: dict) -> Header:
    h = Header.__new__(Header)
    h.__dict__.update(data)
    return h


if __name__ == '__main__':
    d = {'messagePurpose': 'commandResponse',
         'requestId': '5766998a-6e26-41db-a21a-c42cdb5630ad', 'version': 16973824}
    h = to_header(d)
    print(h.messagePurpose)
    print(h.requestId)
    print(h.version)
