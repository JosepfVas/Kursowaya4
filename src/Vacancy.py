class Vacancy:
    def __init__(self, title, city, salary_from, salary_to, link, description, experience):
        self.id = id
        self.title = title
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.link = link
        self.description = description
        self.experience = experience

    @staticmethod
    def create_vacancy_objects(vacancies_data):
        vacancies = []
        for vacancy_data in vacancies_data:
            title = vacancy_data.get("name")
            city = vacancy_data.get("area").get("name")
            salary_info = vacancy_data.get("salary", {})
            salary_from = salary_info.get("from") if salary_info else 0
            salary_to = salary_info.get("to") if salary_info else 0
            link = vacancy_data.get("alternate_url")
            description = vacancy_data.get("snippet", {}).get("requirement", "")
            experience = vacancy_data.get("name")

            vacancy = Vacancy(title, city, salary_from, salary_to, link, description, experience)
            vacancies.append(vacancy)
        return vacancies

    def to_dict(self):
        return {
            "title": self.title,
            "city": self.city,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "link": self.link,
            "description": self.description,
            "experience": self.experience
        }

    def __repr__(self):
        return (f"{self.title}, {self.city}, зарплата от - {self.salary_from}руб., зарплата до -"
                f" {self.salary_to}руб., "
                f"ссылка на вакансию '{self.link}', "
                f"описание работы: {self.description}, "
                f"опыт: {self.experience}")

