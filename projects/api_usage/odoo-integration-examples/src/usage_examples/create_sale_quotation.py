"""Example create_sale_quotation."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Creates a sale quotation for a given customer.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.create(
        'sale.order',
        values={
            'partner_id': 27,
            },
        )


if __name__ == '__main__':
    main()
