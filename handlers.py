import abc

from events import Event, UserCreated
from infrastructure.base import RequireInternalService


class AbstractHandler(abc.ABC):

    @abc.abstractmethod
    async def __call__(self, event: Event):
        raise NotImplemented


class SyncUserDateHandler(AbstractHandler, RequireInternalService):
    async def __call__(self, event: Event):
        assert isinstance(event, UserCreated)
        print(event.user_id)
        user = await self.internal_service.find_user(event.user_id)
        print(user)
