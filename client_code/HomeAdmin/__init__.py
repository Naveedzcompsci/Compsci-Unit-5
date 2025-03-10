# Ensure BaseAdminForm is imported
from .base_admin_form import BaseAdminForm  # Correct import path based on where BaseAdminForm is located

from ._anvil_designer import HomeAdminTemplate
from anvil import *
import anvil.server

class HomeAdmin(HomeAdminTemplate, BaseAdminForm):
    def __init__(self, **properties):
        super().__init__(**properties)
        # Load dashboard statistics
        self.load_dashboard_stats()

    def load_dashboard_stats(self):
        """Load statistics for the admin dashboard"""
        try:
            # Call server function to get dashboard stats
            stats = anvil.server.call('get_dashboard_stats')
            self.total_bookings_label.text = str(stats["total_bookings"])
            self.active_drivers_label.text = str(stats["active_drivers"])
            self.pending_invoices_label.text = str(stats["pending_invoices"])
        except Exception as e:
            alert(f"Error loading dashboard stats: {str(e)}")

    def home_click(self, **event_args):
        """This method is called when the home button is clicked"""
        open_form('HomeAdmin')

    def bookings_click(self, **event_args):
        """This method is called when the bookings button is clicked"""
        open_form('BookingsAdmin')

    def staff_click(self, **event_args):
        """This method is called when the staff button is clicked"""
        open_form('StaffAdmin')

    def invoices_click(self, **event_args):
        """This method is called when the invoices button is clicked"""
        open_form('InvoicesAdmin')

    def signout_link_click(self, **event_args):
        """This method is called when the signout link is clicked"""
        anvil.users.logout()
        open_form('Logout')
