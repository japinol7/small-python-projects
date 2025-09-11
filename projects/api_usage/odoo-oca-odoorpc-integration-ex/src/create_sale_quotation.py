"""Example create_sale_quotation."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Creates a sale quotation for a given customer.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    odoo.env['sale.order'].create({
        'partner_id': 27,
        })


if __name__ == '__main__':
    main()
