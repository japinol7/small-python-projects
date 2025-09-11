"""Example search_read_out_invs."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG



def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the names of the five most recent out invoices created
    that are not canceled and have been validated.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    out_invoices_vals = odoo.env["account.move"].search_read([
        ('move_type', '=', 'out_invoice'),
        ('state', 'not in', ('draft', 'cancel')),
        ],
        fields=['name', 'state', 'partner_id'],
        order='id desc',
        limit=5,
        )

    for inv_vals in out_invoices_vals:
        print(f"{inv_vals['name']}, "
              f"state: {inv_vals['state']}, "
              f"Customer: {inv_vals['partner_id'][1]}")


if __name__ == '__main__':
    main()
