"""Example search_read_sale_orders."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the names of the five most recent sale orders created
    that are not canceled and have been confirmed.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    out_sales_vals = odoo.env['sale.order'].search_read([
        ('state', 'not in', ('draft', 'sent', 'cancel')),
        ],
        fields=['name', 'state', 'partner_id'],
        order='id desc',
        limit=5,
        )

    for sale_vals in out_sales_vals:
        print(f"{sale_vals['name']}, "
              f"state: {sale_vals['state']}, "
              f"Customer: {sale_vals['partner_id'][1]}")


if __name__ == '__main__':
    main()
