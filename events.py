from dataclasses import dataclass


class Event:
    ...


@dataclass
class UserCreated(Event):
    user_id: int
