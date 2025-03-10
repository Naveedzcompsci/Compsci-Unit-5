from ._anvil_designer import HomeAdminTemplate
from anvil import *

class HomeAdmin(HomeAdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    # Load dashboard statistics
    self.load_dashboard_stats()
    
  def load_dashboard_stats(self):
    """Load statistics for the admin dashboard"""
    # Count total bookings
    total_bookings = len(app_tables.bookings.search())
    self.total_bookings_label.text = str(total_bookings)
    
    # Count active drivers
    active_drivers = len(app_tables.staff.search(role="driver", is_active=True))
    self.active_drivers_label.text = str(active_drivers)
    
    # Count pending invoices
    pending_invoices = len(app_tables.invoices.search(status="pending"))
    self.pending_invoices_label.text = str(pending_invoices)
    
  def signout_link_click(self, **event_args):
    """This method is called when the signout link is clicked"""
    anvil.users.logout()
    open_form('Logout')