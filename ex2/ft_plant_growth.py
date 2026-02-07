"""Simulate a week of growth for multiple garden plants."""


class Plant:
    """Track a plant's height and age as it grows."""
    def __init__(self, name: str, height: int, Age: int):
        """Initialize a plant with name, height in cm, and age in days."""
        self.name = name
        self.initial = height
        self.height = height
        self.Age = Age

    def grow(self):
        """Increase the plant's height by 1 cm."""
        self.height = self.height + 1

    def age(self):
        """Increase the plant's age by 1 day."""
        self.Age = self.Age + 1

    def get_info(self):
        """Print a summary of the plant's current state."""
        print(f"{self.name}: {self.height}cm, {self.Age} days old")

    def growth(self):
        """Print the how mush the plant grow up"""
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
