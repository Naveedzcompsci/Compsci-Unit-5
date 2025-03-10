from ._anvil_designer import DriverHomeTemplate  # Would need to be created
from anvil import *

class DriverHome(DriverHomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Get current user
    self.current_driver = anvil.users.get_user()
    # Load assigned bookings
    self.load_assigned_bookings()
    
  def load_assigned_bookings(self):
    """Load all bookings assigned to the current driver"""
    # Query bookings for this driver
    driver_bookings = app_tables.bookings.search(
      driver=self.current_driver,
      status=q.any_of("Scheduled", "In Progress")
    )
    # Display in repeating panel
    self.bookings_panel.items = driver_bookings
    
  def update_status_click(self, booking, status, **event_args):
    """Update the status of a booking"""
    # Update booking status
    booking['status'] = status
    booking.update()
    
    # If status is "Completed", calculate payment
    if status == "Completed":
      self.calculate_driver_payment(booking)
    
    # Refresh bookings display
    self.load_assigned_bookings()
    
  def set_availability_click(self, **event_args):
    """Set driver availability"""
    # Open availability form
    open_form('DriverAvailability', driver=self.current_driver)
    
  def calculate_driver_payment(self, booking):
    """Calculate payment for completed booking"""
    # In real implementation, would have complex payment calculation
    # Simplified for example purposes
    payment_amount = booking['fare'] * 0.8  # Driver gets 80% of fare
    
    # Record payment
    app_tables.driver_payments.add_row(
      driver=self.current_driver,
      booking=booking,
      amount=payment_amount,
      date=datetime.now()
    )