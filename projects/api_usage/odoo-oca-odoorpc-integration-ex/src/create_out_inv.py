"""Example create_out_inv."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Creates an out invoice for a given customer.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    odoo.env['account.move'].create({
        'partner_id': 27,
        'move_type': 'out_invoice',
        })


if __name__ == '__main__':
    main()
