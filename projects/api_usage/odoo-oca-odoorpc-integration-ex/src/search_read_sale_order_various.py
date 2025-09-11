"""Example search_read_sale_order_various."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def get_odoo_client():
    return OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo


def get_not_confirmed_sale_order_name(odoo):
    out_sales_vals = odoo.env['sale.order'].search_read([
        ('state', '=', 'draft'),
        ],
        fields=['name'],
        order='id desc',
        limit=1,
        )
    return out_sales_vals and out_sales_vals[0]['name'] or None


def get_sale_order_state(odoo, sale_name):
    out_sales_vals = odoo.env['sale.order'].search_read([
        ('name', '=', sale_name),
        ],
        fields=['name', 'state'],
        order='id desc',
        limit=1,
        )
    return out_sales_vals[0]['state']


def main():
    odoo = get_odoo_client()
    sale_name = get_not_confirmed_sale_order_name(odoo)

    if not sale_name:
        print("No sale product found with state: draft")
        return

    sale_state = get_sale_order_state(odoo, sale_name)
    print(f"Sale order name: {sale_name}, state: {sale_state}")


if __name__ == '__main__':
    main()
