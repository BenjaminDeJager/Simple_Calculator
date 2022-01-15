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
        self.label = Label(font_size='30sp')
        self.maxSize = maxSize

    def __str__(self):
        return "\n".join(self)


class MemoryButton(Button):
    def __init__(self, newName, theMemory, **kwargs):
        super().__init__(**kwargs)
        self.theMemory = theMemory
        self.text = newName


class OperatorButton(MemoryButton):
    def __init__(self, theName, theMemory, theOperation, **kwargs):
        super().__init__(theName, theMemory, **kwargs)
        self.operation = theOperation

    def on_press(self):
        try:
            newValue = self.operation(self, self.theMemory)
            if newValue is not None:
                self.theMemory.append(str(newValue))
            self.theMemory.label.text = str(self.theMemory)
        except IndexError:
            print("IndexError")
        except TypeError:
            print("TypeError")


class CalculatorApp(App):
    def __init__(self):
        super(CalculatorApp, self).__init__()
        self.memory = Memory()
        self.display = BoxLayout(orientation='horizontal')
        self.display.add_widget(self.memory.label)
        self.display.add_widget(
            OperatorButton("CLEAR", theMemory=self.memory,
                           theOperation=lambda _self, _memory: _memory.clear(), size_hint=(0.25, 0.5)))

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
                string_counter = str(counter)
                button = OperatorButton(str(counter), theMemory=self.memory,
                                        theOperation=lambda _self, _memory: _self.text)
                buttons.append(button)
                row.add_widget(button)
                counter = counter - 1
            buttonBox.add_widget(row)

        row_4 = BoxLayout(orientation='horizontal')
        row_4.add_widget(OperatorButton("0", theMemory=self.memory,
                                        theOperation=lambda _self, _memory: _self.text))
        row_4.add_widget(Button(disabled=True, size_hint=(2, 1)))
        buttonBox.add_widget(row_4)

        row_operators = BoxLayout(orientation='horizontal')

        row_operators.add_widget(OperatorButton("+", theMemory=self.memory,
                                                theOperation=lambda _self, _memory: float(_memory[-1]) + float(
                                                    _memory[-2])
                                                ))
        row_operators.add_widget(OperatorButton("-", theMemory=self.memory,
                                                theOperation=lambda _self, _memory: float(_memory[-1]) - float(
                                                    _memory[-2])
                                                ))
        row_operators.add_widget(OperatorButton("*", theMemory=self.memory,
                                                theOperation=lambda _self, _memory: float(_memory[-1]) * float(
                                                    _memory[-2])
                                                ))
        row_operators.add_widget(OperatorButton("/", theMemory=self.memory,
                                                theOperation=lambda _self, _memory: float(_memory[-1]) / float(
                                                    _memory[-2])
                                                ))
        buttonBox.add_widget(row_operators)

        main.add_widget(buttonBox)

        return main


if __name__ == '__main__':
    CalculatorApp().run()
