class Smartphone:
    def __init__(self, brand, model, battery_life, os):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
        self.os = os
        self.is_on = False
    
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Operating System: {self.os}")
        print(f"Battery Life: {self.battery_life}%")
        print(f"Phone is {'on' if self.is_on else 'off'}")
    
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")
    
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")
    
    def check_battery(self):
        print(f"Battery Level: {self.battery_life}%")
        if self.battery_life < 20:
            print("Warning: Battery is low!")
