"""Example odoo_client_ex_read."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the name and state of some invoices.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    out_invoices_vals = odoo.client.read(
        'account.move',
        ids=[2, 1],
        fields=['name', 'state'],
        )

    for inv_vals in out_invoices_vals:
        print(f"{inv_vals['name']}, state: {inv_vals['state']}")


if __name__ == '__main__':
    main()
