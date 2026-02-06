print("=== Garden Plant Registry ===")


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def test():
    plants = [
        ["Rose", 25, 30],
        ["Sunflower", 80, 42],
        ["Cactus", 15, 120],
    ]

    for plant in plants:
        p = Plant(plant[0], plant[1], plant[2])
        print(f"{p.name}: {p.height}cm, {p.age} days old")


test()
