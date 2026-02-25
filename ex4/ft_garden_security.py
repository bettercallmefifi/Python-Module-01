"""Garden Security System: Validate plant data before updates."""


class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        """Initialize a secure plant and set validated attributes."""
        self.name = name
        self.__height = 0
        self.__age = 0

        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set the plant height if the value is non-negative."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm "
                  "[REJECTED]")
            print("Security: Negative height rejected\n")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set the plant age if the value is non-negative."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days old"
                  "[REJECTED]")
            print("Security: Negative age rejected\n")
            return
        self.__age = age
        print(f"Age updated: {self.__age} days [OK]\n")

    def get_info(self) -> None:
        """Print the plant's current status."""
        print(f"Current plant: {self.name} ({self.__height}cm,"
              f" {self.__age} days)")


def main():
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
#    rose.set_age(-2)
    rose.get_info()


if __name__ == "__main__":
    main()
