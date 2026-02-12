class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant instance.

        :param name: The common name of the plant.
        :param height: Starting height in centimeters.
        :param age: Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """Increase the plant's height by 1cm and log the growth."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Represents a plant that produces flowers, inheriting from Plant."""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            ) -> None:
        """
        Initialize a FloweringPlant.

        :param color: The color of the flowers.
        """
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    """A high-value flowering plant that carries competition points."""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            points: int,
            ) -> None:
        """
        Initialize a PrizeFlower.

        :param points: Competitive points assigned to this flower.
        """
        super().__init__(name, height, age, color)
        self.points = points


class GardenManager:
    """Manages collections of plants across multiple gardens."""
    # Class-level list to track all GardenManager instances
    gardens = []

    class GardenStats:
        """Utility class for calculating plant statistics."""

        @staticmethod
        def total_growth(plants: list[Plant]) -> int:
            """
            Calculate the total growth instances of all plants.
            :param plants: List of Plant objects.
            :return: The sum of individual plant growth events.
            """
            total = 0
            for plant in plants:
                total += 1
            return total

        @staticmethod
        def count_type(plants: list[Plant]) -> tuple[int, int, int]:
            """
            Count occurrences of each plant class type in a list.

            :param plants: List of Plant objects.
            :return: A tuple of (regular_count, flowering_count, prize_count).
            """
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def __init__(self, owner: str) -> None:
        """
        Initialize a GardenManager for a specific owner.

        :param owner: Name of the person who owns the garden.
        """
        self.owner = owner
        self.plants: list[Plant] = []
        GardenManager.gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        """
        Validate and add a plant to the owner's garden.

        :param plant: The Plant object to be added.
        """
        if not GardenManager.validate_height(plant.height):
            print(f"{plant.name} has invalid height")
            return
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """Trigger the grow method for every plant in the garden."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        """
        Print a detailed status report of all plants

        and garden statistics.
        """
        print(f"==={self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming),"
                      f"Prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm,"
                      f"{plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")

        growth = GardenManager.GardenStats.total_growth(self.plants)
        regular, flowring, prize = (
            GardenManager.GardenStats.count_type(self.plants))

        print()
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {growth}cm")
        print(f"Plant types: {regular} regular, {flowring} flowering, "
              f"{prize} prize flowers")

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Check if a given height is valid for a plant.

        :param height: The height value to check.
        :return: True if height is positive, False otherwise.
        """
        return height > 0

    @classmethod
    def create_garden_network(cls) -> dict[str, int]:
        """
        Calculate competitive scores for all managed gardens.

        :return: A dictionary mapping owner names to their total garden score.
        """
        scores: dict[str, int] = {}
        for garden in cls.gardens:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            scores[garden.owner] = score
        return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    alice.add_plant(Plant("Oak Tree", 100, 365))
    alice.add_plant(FloweringPlant("Rose", 25, 120, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 90, "yellow", 10))

    print()
    alice.grow_all()
    print()
    alice.report()
    print()

    print("Height validation test:", GardenManager.validate_height(10))
    scores = GardenManager.create_garden_network()
    print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
    print("Total gardens managed:", len(GardenManager.gardens))
