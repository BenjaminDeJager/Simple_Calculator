from kivy.app import App
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class valueButton(Button):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        size_hint = (.7, 1)

    def on_release(self):
        print(self.text)


class CalculatorApp(App):

    def build(self):
        buttons = []
        for i in range(10):
            buttons.append(valueButton(str(i)))
        main = BoxLayout(orientation='horizontal')

        for button in buttons:
            main.add_widget(button)
        return main


if __name__ == '__main__':
    CalculatorApp().run()
