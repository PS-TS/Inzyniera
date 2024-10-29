from abc import ABC


class IService(ABC):
    async def get_index(self) -> int:
        pass

    async def get_params(self) -> str:
        pass