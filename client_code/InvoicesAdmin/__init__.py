from ._anvil_designer import InvoicesAdminTemplate
from anvil import *

class InvoicesAdmin(InvoicesAdminTemplate, BaseAdminForm):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    # Load invoices data
    self.load_invoices_data()
    
  def load_invoices_data(self):
    """Load all invoices from the database"""
    # Query invoices table
    invoices = app_tables.invoices.search()
    # Display in repeating panel
    self.invoices_panel.items = invoices
    
  def generate_invoice_click(self, **event_args):
    """Generate a new invoice from completed bookings"""
    # Open invoice generation form
    open_form('GenerateInvoice')
    
  def send_invoice_click(self, **event_args):
    """Send selected invoice to customer"""
    if not self.selected_invoice:
      alert("Please select an invoice first")
      return
      
    # In real implementation, would send email with invoice
    self.selected_invoice['status'] = "sent"
    self.selected_invoice.update()
    alert("Invoice sent successfully")
    self.load_invoices_data()  # Refresh display