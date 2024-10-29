from abc import ABC
from typing import Iterable

from domains.test1 import Record

class IRepository(ABC):
    async def get_all_params(self) -> Iterable[AirQualityRecord] | None: 
        pass
