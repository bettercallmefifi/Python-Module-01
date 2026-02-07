print("=== Garden Plant Registry ===")
"""
This program defines a Plant class used to store and display basic
information about plants in a community garden.
"""


class Plant:
    """Store basic information about a garden plant."""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with a name, age in days, and height in cm."""
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
        """Print a short summary of the plant's current details."""
        print(f"{p.name}: {p.height}cm, {p.age} days old")


test()
