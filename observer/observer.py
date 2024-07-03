class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(self, *args, **kwargs)

class Observer:
    def update(self, observable, *args, **kwargs):
        pass



class WeatherStation(Observable):
    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

class PhoneDisplay(Observer):
    def update(self, observable, *args, **kwargs):
        if isinstance(observable, WeatherStation):
            temperature = observable.temperature
            print(f"Temperature in the Phone Display: {temperature} degrees Celsius")


class TVDisplay(Observer):
    def update(self, observable, *args, **kwargs):
        if isinstance(observable, WeatherStation):
            temperature = observable.temperature
            print(f"Temperature in the TV Display: {temperature} degrees Celsius")



weather_station = WeatherStation()
phone_display = PhoneDisplay()
tv_display = TVDisplay()

weather_station.add_observer(phone_display)
weather_station.add_observer(tv_display)
weather_station.set_temperature(25)