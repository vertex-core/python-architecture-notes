class cat:
    name = None
    sleep = None
    hungry = None
    happy = None
    age = None

    def set_data(self, name, sleep, hungry, happy, age):
        self.name = name
        self.sleep = sleep
        self.hungry = hungry
        self.happy = happy
        self.age = age

    def get_data(self):
        print(
            f"Name is {self.name}, age is {self.age}, hungry is {self.hungry},happy is {self.happy},sleep is {self.sleep}"
        )


cat_1 = cat()
cat_1.set_data("Barsik", True, True, None, 2)


cat_2 = cat()
cat_2.set_data("Silver", True, True, True, 1)

cat_1.get_data()
cat_2.get_data()
