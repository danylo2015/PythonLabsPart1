class Student:
    def __init__(self, name: str, rank: float, height: float, age: int, hometown: str):
        self.__name = name
        self.__rank = rank
        self.__height = height
        self.age = age
        self.hometown = hometown

    def get_name(self):
        return self.__name

    def get_rank(self):
        return self.__rank

    def get_height(self):
        return self.__height

    def __str__(self):
        return (f"Student's name: {self.get_name()}, student's rank: {self.get_rank()}, "
                f"student's height: {self.get_height()}, student's age {self.age}, student's hometown {self.hometown}")

    def __repr__(self):
        return f"{self.get_name()}, {self.get_rank()}, {self.get_height()}, {self.age}, {self.hometown}"

    def __del__(self):
        print(f"Deleting object {self.get_name()}")
