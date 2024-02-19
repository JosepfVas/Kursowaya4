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

    def __repr__(self):
        return (f"{self.title}, {self.city}, зарплата от - {self.salary_from}руб., зарплата до -"
                f" {self.salary_to}руб., "
                f"ссылка на вакансию '{self.link}', "
                f"description='{self.description}', "
                f"{self.experience}")

    def to_dict(self):
        return {
            "title": self.title,
            "city": self.city,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "link": self.link,
            "description": self.description
        }
