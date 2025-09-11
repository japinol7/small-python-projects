"""Example search_read_out_invs."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the names of the five most recent out invoices created
    that are not canceled and have been validated.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    out_invoices_vals = odoo.search_read(
        'account.move',
        domain=[[
            ('move_type', '=', 'out_invoice'),
            ('state', 'not in', ('draft', 'cancel')),
            ]],
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
