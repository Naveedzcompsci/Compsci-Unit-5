from ._anvil_designer import BookingsAdminTemplate
from anvil import *

class BookingsAdmin(BookingsAdminTemplate, BaseAdminForm):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    # Load bookings data when form opens
    self.load_bookings_data()
    
  def load_bookings_data(self):
    """Load all bookings data from the database"""
    # Query bookings table
    bookings = app_tables.bookings.search()
    # Display in repeating panel
    self.bookings_panel.items = bookings
    
  def newbtn_click(self, **event_args):
    """This method is called when the New Booking button is clicked"""
    open_form('CreateBookingsAdmin')