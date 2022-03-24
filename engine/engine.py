from abc import ABC, abstractmethod
from asyncio import AbstractEventLoop

class Engine(AbstractEventLoop):
    @abstractmethod
    def needs_service(self):
        pass