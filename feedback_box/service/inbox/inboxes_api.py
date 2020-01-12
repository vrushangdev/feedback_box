import json
from flask import Response
from flask_restful import Resource

from feedback_box.service.database import db
from feedback_box.application.inbox.queries import get_all
from feedback_box.serializers.inbox_json_serializer import InboxJsonEncoder


class InboxesApi(Resource):

    def get(self) -> Response:
        query = get_all.GetAllInboxesQuery(db)
        result = query.execute()

        return Response(
            json.dumps(result, cls=InboxJsonEncoder),
            mimetype='application/json',
            status=200
        )
