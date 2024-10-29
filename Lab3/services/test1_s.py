from repositories.test1_repo import IRepository
from services.itest1_s import IService

class Service(IService):
    repository: IRepository

    def __init__(self, repository: IRepository) -> None:
        self.repository = repository

    async def get_params(self) -> str:
        all_quality_params