"""Display basic information about a garden plant."""


def ft_garden_info(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")

    plant = "Rose"
    height = 25
    age = 30

    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")

    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_info()
