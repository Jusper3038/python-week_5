# python-week_5
# Smartphone Class

## Description
This Python class represents a Smartphone. The `Smartphone` class includes attributes like brand, model, battery life, and operating system. It also includes methods to display the details of the smartphone, turn the phone on or off, and check the battery level.

## Features
- Display smartphone details
- Turn the phone on or off
- Check battery level and alert when battery is low

## How to Use
1. **Create a Smartphone object** by passing the following parameters to the constructor:
   - `brand` (e.g., "Apple")
   - `model` (e.g., "iPhone 13")
   - `battery_life` (e.g., 85 for 85% battery)
   - `os` (e.g., "iOS")
   
2. **Display smartphone details** using the `display_details()` method.
3. **Turn the smartphone on or off** using `turn_on()` and `turn_off()` methods.
4. **Check the battery level** using the `check_battery()` method.

## Example Usage

```python
my_phone = Smartphone("Apple", "iPhone 13", 85, "iOS")
my_phone.display_details()  # Display details of the smartphone
my_phone.turn_on()          # Turn on the phone
my_phone.check_battery()    # Check battery level
my_phone.turn_off()         # Turn off the phone


Assignment 2
# Vehicle Polymorphism Challenge

## Description
This Python program demonstrates polymorphism through multiple vehicle classes (Car, Plane, and Boat) that share the same `move()` method. Each class implements the `move()` method differently to showcase how polymorphism works in object-oriented programming.

## Features
- Each vehicle (Car, Plane, Boat) has its own implementation of the `move()` method.
- The program uses a list of different vehicle objects to demonstrate polymorphism.

## How to Use
1. **Create different vehicle objects** (Car, Plane, Boat) and add them to a list.
2. **Call the `move()` method on each object**. The appropriate method for each type of vehicle will be called automatically.

## Example Usage

```python
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
