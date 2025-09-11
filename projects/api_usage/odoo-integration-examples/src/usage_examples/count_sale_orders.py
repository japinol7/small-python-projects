"""Example count_sale_orders."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the Number of confirmed sales.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    count_out_sales = odoo.search_count(
        'sale.order',
        domain=[[
            ('state', 'not in', ('draft', 'sent', 'cancel')),
            ]],
        )

    print(f"Number of confirmed sales: {count_out_sales}")


if __name__ == '__main__':
    main()
