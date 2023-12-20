# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger

from login_screen import LoginScreen
from main_screen import MainScreen


class MyApp (App):
    def __init__(self):
        super().__init__()
        self.main_screen = None
        self.login_screen = None

    def build(self):
        # Load the KV file for the login screen with error handling
        try:
            Builder.load_file('login_screen.kv')
        except Exception as exception:
            Logger.error(f"Error loading KV file: {exception}")
            return None

        # Initialize the LoginScreen with a reference to the app
        self.login_screen = LoginScreen(app=self)
        return self.login_screen

    def switch_to_main(self):
        # Check if main_screen already exists to avoid re-creation
        if not hasattr(self, 'main_screen'):
            self.main_screen = MainScreen()

        # Switch to the main screen
        self.root.clear_widgets()
        self.root.add_widget(self.main_screen)


if __name__ == '__main__':
    try:
        MyApp().run()
    except Exception as e:
        Logger.error(f"Application failed: {e}")
