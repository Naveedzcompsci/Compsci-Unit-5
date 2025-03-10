from ._anvil_designer import HomeAdminTemplate  # Ensure you have this import
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class HomeAdmin(HomeAdminTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def home_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('HomeAdmin')

    def bookings_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('BookingsAdmin')

    def staff_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('StaffAdmin')

    def invoices_click(self, **event_args):  # Added missing method for "Invoices_click"
        """This method is called when the button is clicked"""
        open_form('InvoicesAdmin')

    def signout_link_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('Logout')
