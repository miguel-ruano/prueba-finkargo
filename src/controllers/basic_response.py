from flask import jsonify, abort, make_response
import json


class BasicResponse:
    error: str
    status: int

    def __init__(self, data=None, status: int = 200, error=None):
        super().__init__()
        self.data = data
        self.status = status
        self.error = error

    def to_json(self):
        obj_json = json.dumps(self.__dict__)
        return json.loads(obj_json)

    def to_json_response(self):
        return jsonify(self.to_json())

    @staticmethod
    def abort(status: int, error: Exception):
        abort(
            make_response(
                BasicResponse(
                    status=status,
                    error=error.args[0] if len(error.args) > 0 else str(error),
                ).to_json_response(),
                status,
            )
        )
