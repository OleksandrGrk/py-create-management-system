from dataclasses import dataclass
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(student_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(student_group, file)
    if student_group:
        max_students = max([len(group.students) for group in student_group])
        return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        content = pickle.load(file)
        specialities = set([spec.specialty.name for spec in content])
        return specialities


def read_students_information() -> None:
    with open("students.pickle", "rb") as file:
        content = pickle.load(file)
        return content
