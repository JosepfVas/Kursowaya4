from abc import ABC, abstractmethod


class AbstractJobApi(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class ABCSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, criteria):
        pass
