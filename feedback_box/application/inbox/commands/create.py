from feedback_box.domain.inbox import Inbox
from feedback_box.application.interfaces.icommand_query import ICommandQuery
from feedback_box.application.interfaces.idatabase_service import DatabaseService


class CreateInboxCommand(ICommandQuery):
    def __init__(self, db: DatabaseService) -> None:
        self.db = db

    def execute(self, owner: str, password: str, question: str) -> Inbox:
        new_inbox = self.db.create_inbox(
            {
                'owner': owner,
                'password': password,
                'question': question
            }
        )
        return new_inbox
