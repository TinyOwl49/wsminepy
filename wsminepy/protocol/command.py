import uuid
import json


def get_command_request(cmd: str) -> str:
    command_request = {
        "header": {
            "version": 1,
            "requestId": str(uuid.uuid4()),
            "messagePurpose": "commandRequest",
            "messageType": "commandRequest"
        },
        "body": {
            "version": 1,
            "origin": {
                "type": "player"
            },
            "commandLine": cmd
        }
    }
    return json.dumps(command_request)


class CommandResponce(object):
    def __init__(self, statusCode: int, statusMessage: str, wasSpawned=False) -> None:
        self.statusCode = statusCode
        self.statusMessage = statusMessage
        self.wasSpawned = wasSpawned


def to_commandResponce(data: dict):
    c = CommandResponce.__new__(CommandResponce)
    c.__dict__.update(data)
    return c

