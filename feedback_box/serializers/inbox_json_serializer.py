import json


class InboxJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                'id': str(o.id),
                'owner': o.owner,
                'tripcode': str(o.tripcode),
                'question': o.question
            }
            return to_serialize
        except AttributeError:
            super().default(o)
