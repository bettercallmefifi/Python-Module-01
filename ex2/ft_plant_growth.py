class Plant:
    def __init__(self, name: str, height: int, Age: int):
        self.name = name
        self.initial = height
        self.height = height
        self.Age = Age

    def grow(self):
        self.height = self.height + 1

    def age(self):
        self.Age = self.Age + 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.Age} days old")

    def growth(self):
        return self.height - self.initial


def main():
    plant_info = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    plant_info.get_info()

    for _ in range(6):
        plant_info.grow()
        plant_info.age()

    print("=== Day 7 ===")
    plant_info.get_info()
    print(f"Growth this week: +{plant_info.growth()}cm")


main()
