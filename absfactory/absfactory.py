from abc import ABC, abstractmethod

# Productos
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Window(ABC):
    @abstractmethod
    def open(self):
        pass

class WindowsButton(Button):
    def click(self):
        return "Windows Button Clicked"

class WindowsWindow(Window):
    def open(self):
        return "Windows Window Opened"

class MacButton(Button):
    def click(self):
        return "Mac Button Clicked"

class MacWindow(Window):
    def open(self):
        return "Mac Window Opened"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_window(self) -> Window:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_window(self) -> Window:
        return WindowsWindow()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_window(self) -> Window:
        return MacWindow()

# Uso
def create_ui(factory: GUIFactory):
    button = factory.create_button()
    window = factory.create_window()
    print(button.click())  # Salida depende de la fábrica usada
    print(window.open())  # Salida depende de la fábrica usada

windows_factory = WindowsFactory()
mac_factory = MacFactory()

create_ui(windows_factory)
# Salida: "Windows Button Clicked"
#         "Windows Window Opened"

create_ui(mac_factory)
# Salida: "Mac Button Clicked"
#         "Mac Window Opened"
