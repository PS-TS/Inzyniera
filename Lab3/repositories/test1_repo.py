import aiohttp

from typing import Iterable

from utils import consts
from domains.test1 import Record
from repositories.itest1_repo import IRepository

class Repository(IRepository):
    async def get_all_params(self) -> Iterable[Record] | None: 
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        return parsed_params
    
    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_SENSOR_URL.format()) as response:
                if response.status != 200:
                    return None
            return await response.json()
    
    async def _parse_params(self, params: Iterable[dict]) -> Iterable[Record]:
        return [Record(event_time=record.get("date"), value=record.get("value")) for record in params["values"]]
    