from uuid import UUID
from datetime import datetime

from feedback_box.domain.tripcode import Tripcode


class Message:
    def __init__(
            self,
            inbox_id: UUID,
            tripcode: str,
            content: str,
            timestamp: datetime,

    ) -> None:
        self.inbox_id = inbox_id
        self.tripcode = Tripcode(tripcode)
        self.content = content
        self.timestamp = timestamp

    @property
    def author(self) -> str:
        return self.tripcode.owner
