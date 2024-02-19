from abc import ABC, abstractmethod

class AbstractJobApi(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass
