from ._anvil_designer import AddStaffMemberTemplate  # Would need to be created
from anvil import *

class AddStaffMember(AddStaffMemberTemplate, BaseAdminForm):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    
  def save_staff_click(self, **event_args):
    """Save new staff member to database"""
    # Validate form data
    if not self.validate_staff_form():
      return
      
    # Create the staff member
    app_tables.staff.add_row(
      name=self.name_input.text,
      contact=self.contact_input.text,
      role=self.role_dropdown.selected_value,
      license_number=self.license_number_input.text,
      license_expiry=self.license_expiry_date.date,
      vehicle_type=self.vehicle_type_dropdown.selected_value,
      special_capabilities=self.special_capabilities.text,
      is_active=True,
      created_at=datetime.now()
    )
    
    # Return to staff admin
    open_form('StaffAdmin')
    
  def validate_staff_form(self):
    """Validate all staff form fields"""
    # Check required fields
    if not (self.name_input.text and self.contact_input.text and 
            self.role_dropdown.selected_value):
      alert("Please fill all required fields!")
      return False
    
    # Additional validation as needed
    
    return True