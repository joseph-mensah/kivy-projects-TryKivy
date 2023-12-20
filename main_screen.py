from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainScreen (BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Welcome to the main screen!')
        self.add_widget(self.label)

        self.button = Button(text='Click me!')
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

    def on_button_press(self):
        self.label.text = 'Button clicked!'
