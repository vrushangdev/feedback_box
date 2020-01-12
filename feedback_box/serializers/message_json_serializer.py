import json


TIMESTAMP_FORMAT = '%m/%d/%Y, %H:%M:%S'


class MessageJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                'inbox_id': str(o.inbox_id),
                'tripcode': str(o.tripcode),
                'content': o.content,
                'timestamp': o.timestamp.strftime(TIMESTAMP_FORMAT)
            }
            return to_serialize
        except AttributeError:
            super().default(o)
