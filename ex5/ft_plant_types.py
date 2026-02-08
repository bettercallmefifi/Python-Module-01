class Plant:
    """Store basic information about a garden plant."""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with a name, age in days, and height in cm."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flower, which is a type of plant."""
    def __init__(self, name: str, height: int, age: int, color: str):
        """Initialize a flower with its specific color."""
        super().__init__(name, height, age)
        self.color = color

    def Bloom(self):
        """Display a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Represents a tree, which is a type of plant"""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initialize a tree with its trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade_area: int):
        """Display the shade area produced by the tree"""
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    """Represents a vegetable, which is a type of plant."""
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str,
            ):
        """Initialize a vegetable with harvest season and nutrition."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def rish_of(self):
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Create plant objects and display their characteristics."""
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    print("=== Garden Plant Types ===")
    print()
    print(f"{rose.name} (Flower): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.Bloom()
    print()
    print(f"{oak.name} (Tree): {oak.height}cm, "
          f"{oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade(75)
    print()
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, "
          f"{tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
