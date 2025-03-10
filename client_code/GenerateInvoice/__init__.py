GenerateInvoice Form - New form to generate invoices
from ._anvil_designer import GenerateInvoiceTemplate  # Would need to be created
from anvil import *

class GenerateInvoice(GenerateInvoiceTemplate, BaseAdminForm):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    # Load completed bookings
    self.load_completed_bookings()
    
  def load_completed_bookings(self):
    """Load all completed bookings not yet invoiced"""
    # Query bookings table
    bookings = app_tables.bookings.search(
      status="Completed",
      invoiced=False
    )
    # Display in repeating panel
    self.bookings_panel.items = bookings
    
  def generate_invoice_click(self, **event_args):
    """Generate invoice from selected bookings"""
    selected_bookings = [b for b in self.bookings_panel.items if b['selected']]
    
    if not selected_bookings:
      alert("Please select at least one booking")
      return
      
    # Calculate total amount
    total_amount = sum(booking['fare'] for booking in selected_bookings)
    
    # Create invoice
    invoice = app_tables.invoices.add_row(
      customer=selected_bookings[0]['customer_name'],  # Assuming same customer
      date=datetime.now(),
      amount=total_amount,
      status="pending"
    )
    
    # Link bookings to invoice
    for booking in selected_bookings:
      booking['invoiced'] = True
      booking['invoice'] = invoice
      booking.update()
    
    # In real implementation, would generate PDF invoice
    
    # Return to invoices admin
    open_form('InvoicesAdmin')