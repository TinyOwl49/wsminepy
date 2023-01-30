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