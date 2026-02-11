class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            ):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            points: int,
            ):
        super().__init__(name, height, age, color)
        self.points = points


class GardenManager:
    gardens = []

    class GardenStats:
        @staticmethod
        def total_growth(plants: list[Plant]) -> int:
            total = 0
            for plant in plants:
                total += 1
            return total

        @staticmethod
        def count_type(plants: list[Plant]) -> tuple[int, int, int]:
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
        self.owner = owner
        self.plants: list[Plant] = []
        GardenManager.gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        if not GardenManager.validate_height(plant.height):
            print(f"{plant.name} has invalid height")
            return
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
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
        return height > 0

    @classmethod
    def create_garden_network(cls) -> dict[str, int]:
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
