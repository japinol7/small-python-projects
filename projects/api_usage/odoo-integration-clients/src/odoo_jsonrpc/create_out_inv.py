"""Example create_out_inv."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Creates two out invoices for some given customers.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.create(
        'account.move',
        vals=[
            {'partner_id': 25, 'move_type': 'out_invoice'},
            {'partner_id': 27, 'move_type': 'out_invoice'},
            ],
        )


if __name__ == '__main__':
    main()
