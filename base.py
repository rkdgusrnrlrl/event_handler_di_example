import abc
from typing import TypeVar, Generic


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    async def find_by(filter: dict) -> list:
        raise NotImplemented()


class AbstractUnitOfWork(abc.ABC):
    @abc.abstractmethod
    async def commit(self):
        raise NotImplemented()


T = TypeVar("T")


class Require(abc.ABC, Generic[T]):

    @abc.abstractmethod
    def set_dependency_inject(self, dependencies: T):
        raise NotImplemented()
