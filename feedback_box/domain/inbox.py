from typing import Optional
from uuid import UUID, uuid4

from feedback_box.domain.tripcode import Tripcode


class Inbox:
    def __init__(
            self, owner: str,
            question: str,
            password: Optional[str] = None,
            id: Optional[str] = None,
            tripcode: Optional[Tripcode] = None
    ) -> None:
        self.id = UUID(id) if id else uuid4()
        self.owner = owner
        self.question = question
        self.tripcode = Tripcode(tripcode)

        if not self.tripcode.code:
            self.tripcode.generate_code(owner=owner, password=password)

    @classmethod
    def from_dict(cls, adict: dict):
        return cls(
            owner=adict['owner'],
            password=adict['password'],
            question=adict['question']
        )

    @classmethod
    def from_record(cls, record):
        return cls(
            id=record['id'],
            owner=record['owner'],
            tripcode=record['tripcode'],
            question=record['question']
        )

    def check_password(self, password: str) -> bool:
        return self.tripcode.check_password(password)
