import abc
from typing import NewType


class ICommandQuery(abc.ABC):

    @abc.abstractmethod
    def execute(self, *args):
        pass


CommandQuery = NewType('CommandQuery', ICommandQuery)
