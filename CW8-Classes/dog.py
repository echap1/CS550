class Dog:
    def __init__(self, name):
        self.name, self.energy, self.weight, self.hunger, self.happiness = name, 0.5, 50, 0.5, 0.5

    def eat(self, amount):
        self.energy = min(1, self.energy + amount * 0.05)
        self.weight += amount * 0.5
        self.hunger = max(0, self.hunger - amount * 0.1)
        self.happiness = min(1, amount * 0.05)

    def get_status(self):
        res = []

        if self.energy > 0.9:
            res += ["Energetic"]
        if self.energy < 0.2:
            res += ["Very Tired"]

        if self.weight > 55:
            res += ["Overweight"]
        if self.weight < 40:
            res += ["Underweight"]

        if self.hunger > 0.8:
            res += ["Starving"]

        if self.happiness > 0.8:
            res += ["Overjoyed"]
        if self.happiness < 0.2:
            res += ["Depressed"]

        if len(res) == 0:
            return "Normal"

        return ", ".join(res)

    def __str__(self):
        return (f"{self.name}:\n"
                f"  Hunger: {int(self.hunger * 100)}%\n"
                f"  Energy: {int(self.energy * 100)}%\n"
                f"  Happiness: {int(self.happiness * 100)}%\n"
                f"  Weight: {self.weight}lb\n"
                f"  \n"
                f"  Status: {self.get_status()}")

d = Dog("John")
print(d)