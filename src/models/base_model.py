import json
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, asdict


@dataclass
class BaseModel(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs):
        pass

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, default=lambda x: str(x))
