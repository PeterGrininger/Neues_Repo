from src.testing_course.exploration.person_service import PersonService
from src.testing_course.exploration.person import Person


class HalfRepositiory:
    def create_person(selfself, person: Person) -> None:
        return None

service = PersonService(HalfRepositiory())
service.register("Alice")