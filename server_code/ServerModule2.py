# In Server Module (e.g., Server Code)

import anvil.server
from anvil import app_tables

@anvil.server.callable
def get_dashboard_stats():
    """Retrieve statistics for the dashboard"""
    total_bookings = len(app_tables.bookings.search())
    active_drivers = len(app_tables.staff.search(role="driver", is_active=True))
    pending_invoices = len(app_tables.invoices.search(status="pending"))
    
    return {
        "total_bookings": total_bookings,
        "active_drivers": active_drivers,
        "pending_invoices": pending_invoices
    }
