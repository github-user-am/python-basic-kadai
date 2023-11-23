# 名前と年齢の属性を持つHumanクラスを作成
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です")
        else:
            print(f"{self.name}は大人ではありません")

persons = []

person_one = Human("侍太郎", 20)
persons.append(person_one)

person_two = Human("侍一郎", 35)
persons.append(person_two)

person_three = Human("侍二郎", 10)
persons.append(person_three)

for person in persons:
    person.check_adult()