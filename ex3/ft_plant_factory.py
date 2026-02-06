class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = []
    plant_data = [
        ("Rose", 25, 30),
        ("Ook", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)

    print(f"Totale plants created: {len(plants)}")
