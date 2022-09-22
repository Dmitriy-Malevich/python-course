class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты написания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
   
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    
    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре.
        При попытке обратной прокрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size = 70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximalety " + str(range)
        message += " miles on a full charge."
        print(message)



class ElectricCar(Car):
    """Представляет аспекты машины, спкцифические для электромобилей."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """У элктромобиля нет бака."""
        print("\tThis car doesn't need a gas tank!")


#my_new_car = Car('audi', 'a4', 2016)
#print(my_new_car.get_descriptive_name())

#my_new_car.update_odometer(44)
#my_new_car.read_odometer()

#my_used_cars = Car('subaru', 'outback', 2013)
#print("\n" + my_used_cars.get_descriptive_name())
#my_used_cars.update_odometer(23500)
#my_used_cars.read_odometer()
#my_used_cars.increment_odometer(100)
#my_used_cars.read_odometer()

