from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LoginPage(LoginPageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        anvil.users.login_with_form()

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('HomeAdmin')
