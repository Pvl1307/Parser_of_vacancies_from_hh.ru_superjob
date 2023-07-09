from abc import ABC, abstractmethod
import json


class JSON(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_range):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass

