from kivy.app import App
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from collections import deque
from kivy.uix.widget import Widget

class Memory(deque):
    def __init__(self, maxSize=5):
        super().__init__(maxlen=maxSize)
        self.label = Label()
        self.maxSize = maxSize

    def __str__(self):
        return "\n".join(self)


class AddButton(Button):
    def __init__(self, theMemory, **kwargs):
        super().__init__(**kwargs)
        self.text = "+"
        self.theMemory = theMemory

    def on_press(self):
        try:
            self.theMemory.append(str(float(self.theMemory[-1]) + float(self.theMemory[-2])))
            self.theMemory.label.text = str(self.theMemory)
        except IndexError:
            print("cannot add, not enough inputs")
        except TypeError:
            print("values cannot both be converted")


class ValueButton(Button):
    def __init__(self, text, theMemory, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.theMemory = theMemory
        size_hint = (1, 1)

    def on_press(self):
        self.theMemory.append(self.text)
        self.theMemory.label.text = str(self.theMemory)

class CalculatorApp(App):

    def __init__(self):
        super(CalculatorApp, self).__init__()
        self.memory = Memory()
        self.display = self.memory.label

    def build(self):
        main = BoxLayout(orientation='vertical', size=(50, 30))

        main.add_widget(self.display)

        buttons = []
        numRows = 3
        numCols = 3
        counter = 9
        buttonBox = BoxLayout(orientation='vertical')
        for i in range(numRows):
            row = BoxLayout(orientation='horizontal')
            for j in range(numCols):
                button = ValueButton(str(counter), theMemory=self.memory)
                buttons.append(button)
                row.add_widget(button)
                counter = counter - 1
            buttonBox.add_widget(row)

        row_4 = BoxLayout(orientation='horizontal')
        row_4.add_widget(ValueButton('0', theMemory=self.memory))
        row_4.add_widget(AddButton(theMemory=self.memory))
        buttonBox.add_widget(row_4)

        main.add_widget(buttonBox)

        return main


if __name__ == '__main__':
    CalculatorApp().run()
