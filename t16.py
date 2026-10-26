class Person:
    def __init__(self, name, age, gender) -> None:
        self._name = name
        self._age = age
        self._gender = gender

    def personinfo(self) -> None:
        print(f"Name:{self._name}")
        print(f"Age:{self._age}")
        print(f"Gender:{self._gender}")


class Student(Person):
    def __init__(self, name, age, gender, _college, class_name) -> None:
        super().__init__(name, age, gender)
        self._college = _college
        self._class = class_name

    def personinfo(self) -> None:
        super().personinfo()
        print(f"College:{self._college}")
        print(f"class:{self._class}")

    def __str__(self) -> str:
        return (
            f"Name:{self._name}\n"
            f"Age:{self._age}\n"
            f"Gender:{self._gender}\n"
            f"College:{self._college}\n"
            f"class:{self._class}"
        )

if __name__ =="__main__":
    a=Student("Ziqian Pan",20,"male","电信学部","计算机2406")
    print(a)
