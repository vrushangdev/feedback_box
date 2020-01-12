import bcrypt
from typing import Optional


SEPARATOR = ','
TRIPCODE_OWNER_INDEX = 0
TRIPCODE_PASSWORD_INDEX = 1


class Tripcode:
    def __init__(self, code: Optional[str] = None) -> None:
        self.code = code

    def __str__(self) -> str:
        return str(self.code)

    def generate_code(self, owner: str, password: str) -> str:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        self.code = f'{owner}{SEPARATOR}{hashed_password}'

        return self.code

    def check_password(self, password: str) -> bool:
        hashed_password = self.code.split(SEPARATOR)[TRIPCODE_PASSWORD_INDEX]
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    @property
    def owner(self) -> str:
        return self.code.split(SEPARATOR)[TRIPCODE_OWNER_INDEX]
