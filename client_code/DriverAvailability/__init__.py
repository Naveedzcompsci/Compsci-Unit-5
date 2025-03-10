from ._anvil_designer import DriverAvailabilityTemplate  # Would need to be created
from anvil import *

class DriverAvailability(DriverAvailabilityTemplate):
  def __init__(self, driver, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.driver = driver
    # Load current availability
    self.load_current_availability()
    
  def load_current_availability(self):
    """Load driver's current availability settings"""
    # Query availability table
    availability = app_tables.driver_availability.search(driver=self.driver)
    # Display in repeating panel
    self.availability_panel.items = availability
    
  def save_availability_click(self, **event_args):
    """Save driver availability settings"""
    start_date = self.start_date_picker.date
    end_date = self.end_date_picker.date
    start_time = self.start_time_picker.time
    end_time = self.end_time_picker.time
    is_available = self.availability_dropdown.selected_value == "Available"
    
    # Validate dates and times
    if not (start_date and end_date and start_time and end_time):
      alert("Please fill all required fields!")
      return
      
    if end_date < start_date:
      alert("End date cannot be before start date!")
      return
      
    # Create availability record
    app_tables.driver_availability.add_row(
      driver=self.driver,
      start_date=start_date,
      end_date=end_date,
      start_time=start_time,
      end_time=end_time,
      is_available=is_available
    )
    
    # Refresh display
    self.load_current_availability()
    
  def back_to_home_click(self, **event_args):
    """Return to driver home"""
    open_form('DriverHome')
