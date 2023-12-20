from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class LoginScreen (BoxLayout):
    app = ObjectProperty(None)
    username_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    error_label = ObjectProperty(None)

    def validate_user(self):
        username = self.username_input.text
        password = self.password_input.text

        # Basic input validation
        if not username or not password:
            self.error_label.text = 'Username and password are required'
            return

        # TODO: Replace with secure authentication logic
        if username == 'admin' and password == 'password':
            self.app.switch_to_main()
        else:
            self.error_label.text = 'Invalid username or password'


# Example usage in MyApp
class MyApp (App):
    def __init__(self):
        super().__init__()
        self.login_screen = None

    def build(self):
        self.login_screen = LoginScreen()
        self.login_screen.app = self
        return self.login_screen
