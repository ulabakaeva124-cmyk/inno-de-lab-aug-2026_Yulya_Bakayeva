class Trainee:
    def __init__(self, name: str, surname: str, score: int=0, passing_grade: int=10):
        self.name = name
        self.surname = surname
        self.passing_grade = passing_grade
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if type(value) is not int:
            raise ValueError(f'"Expected value of type int, got {type(value)}')
        elif value < 0:
            raise ValueError(f"The score shouldn't be less than 0!")
        else:
            self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score += 1
        return None

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1
        return None

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1
        return None

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1
        return None

    def is_passing(self) -> bool:
        if self.score >= self.passing_grade:
            return True
        else:
            return False

#testing 1
trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)
print('=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===')
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")

class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2
        return None

class  AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        return True

class Cohort:

    def __init__(self,title : str):
        self.title = title
        self.trainees : list[Trainee] = []

    def add_trainee(self, trainee: Trainee) -> None:
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        return [trainee for trainee in self.trainees if trainee.is_passing()]

#testing 2
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)

cohort.conduct_lecture()
hard_trainee.do_homework()
passing_students = cohort.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")
print("\nУспешно зачислены на следующий модуль:")
for student in passing_students:
    print(f"- {student.name} {student.surname}")