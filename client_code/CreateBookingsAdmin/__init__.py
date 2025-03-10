from ._anvil_designer import CreateBookingsAdminTemplate
from anvil import *
from datetime import datetime

class CreateBookingsAdmin(CreateBookingsAdminTemplate, BaseAdminForm):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    # Initialize driver dropdown
    self.load_available_drivers()
    
  def load_available_drivers(self):
    """Load all available drivers for the booking assignment"""
    # Query drivers table for available drivers
    drivers = app_tables.staff.search(role="driver", is_active=True)
    # Populate dropdown
    self.driver_dropdown.items = [(f"{d['name']} (ID: {d['id']})", d) for d in drivers]
  
  def create_click(self, **event_args):
    """This method is called when the Create button is clicked"""
    # Validate form data
    if not self.validate_booking_form():
      return
      
    # Check for booking conflicts
    if self.check_booking_conflicts():
      alert("This booking conflicts with the selected driver's schedule!")
      return
      
    # Create the booking
    app_tables.bookings.add_row(
      date=self.date_picker.date,
      time=self.time_picker.time,
      pickup=self.pickup_location.text,
      dropoff=self.dropoff_location.text,
      fare=self.fare_input.text,
      customer_name=self.customer_name.text,
      customer_phone=self.customer_phone.text,
      driver=self.driver_dropdown.selected_value,
      status="Scheduled",
      created_at=datetime.now()
    )
    
    # Notify driver about new assignment
    self.notify_driver(self.driver_dropdown.selected_value)
    
    # Return to bookings admin
    open_form('BookingsAdmin')
    
  def validate_booking_form(self):
    """Validate all booking form fields"""
    # Check required fields
    if not (self.date_picker.date and self.time_picker.time and 
            self.pickup_location.text and self.dropoff_location.text):
      alert("Please fill all required fields!")
      return False
    return True
    
  def check_booking_conflicts(self):
    """Check if booking conflicts with existing driver schedule"""
    driver = self.driver_dropdown.selected_value
    booking_date = self.date_picker.date
    booking_time = self.time_picker.time
    
    # Query existing bookings for this driver on same date/time range
    driver_bookings = app_tables.bookings.search(
      driver=driver,
      date=booking_date
    )
    
    # Calculate if there's a time conflict (would need more complex logic in real implementation)
    # This is simplified for example purposes
    for booking in driver_bookings:
      # Check if booking times overlap
      if abs((booking['time'] - booking_time).total_seconds()) < 1800:  # 30 minute buffer
        return True
    
    return False
    
  def notify_driver(self, driver):
    """Send notification to driver about new booking"""
    # In a real implementation, this would integrate with a notification system
    print(f"Notification sent to driver {driver['name']}")