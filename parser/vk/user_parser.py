from parser.vk.auth.session import VkSession
from parser.vk.schemas.candidate_schema import CandidateSchema


class VkCandidateParser:
    vk_session = VkSession
    vk = vk_session.session()

    def __init__(self, name: str, surname: str, age: int, city: str) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

    def get_candidate(self) -> CandidateSchema:
        ...