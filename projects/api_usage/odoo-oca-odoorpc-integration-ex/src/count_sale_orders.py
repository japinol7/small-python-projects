"""Example count_sale_orders."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the Number of confirmed sales.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    count_out_sales = odoo.env['sale.order'].search_count([
        ('state', 'not in', ('draft', 'sent', 'cancel')),
        ])

    print(f"Number of confirmed sales: {count_out_sales}")


if __name__ == '__main__':
    main()
