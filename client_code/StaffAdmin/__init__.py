from ._anvil_designer import StaffAdminTemplate
from anvil import *

class StaffAdmin(StaffAdminTemplate, BaseAdminForm):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    # Load staff data
    self.load_staff_data()
    
  def load_staff_data(self):
    """Load all staff members from the database"""
    # Query staff table
    staff = app_tables.staff.search()
    # Display in repeating panel
    self.staff_panel.items = staff
    
  def add_staff_click(self, **event_args):
    """Open form to add new staff member"""
    open_form('AddStaffMember')
    
  def check_document_expiry(self):
    """Check for documents nearing expiry and send notifications"""
    # This would implement the document tracking functionality
    # Simplified for example purposes
    staff_with_expiring_docs = []
    
    for staff in app_tables.staff.search():
      # Check license expiry
      if staff['license_expiry'] and (staff['license_expiry'] - datetime.now()).days < 30:
        staff_with_expiring_docs.append({
          'staff': staff,
          'document': 'Driving License',
          'expiry': staff['license_expiry']
        })
        
      # Check other documents similarly
      
    # Send notifications for expiring documents
    for doc in staff_with_expiring_docs:
      # In real implementation, would send actual notifications
      print(f"Document expiring: {doc['document']} for {doc['staff']['name']}")