# In a separate module, such as `BaseAdminForm` or in the same module
# that you are importing this in.

class BaseAdminForm:
    def __init__(self, **properties):
        # Initialize the form properties and data bindings
        self.init_components(**properties)
        
    def home_click(self, **event_args):
        """Navigate to HomeAdmin form when home button is clicked."""
        open_form('HomeAdmin')
    
    def bookings_click(self, **event_args):
        """Navigate to BookingsAdmin form when bookings button is clicked."""
        open_form('BookingsAdmin')

    def staff_click(self, **event_args):
        """Navigate to StaffAdmin form when staff button is clicked."""
        open_form('StaffAdmin')

    def invoices_click(self, **event_args):
        """Navigate to InvoicesAdmin form when invoices button is clicked."""
        open_form('InvoicesAdmin')
