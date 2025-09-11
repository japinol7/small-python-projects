"""Example read_out_invs."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the name and state of some invoices.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    out_invoices_vals = odoo.env['account.move'].read(
        [2, 1],
        fields=['name', 'state'],
        )

    for inv_vals in out_invoices_vals:
        print(f"{inv_vals['name']}, state: {inv_vals['state']}")


if __name__ == '__main__':
    main()
