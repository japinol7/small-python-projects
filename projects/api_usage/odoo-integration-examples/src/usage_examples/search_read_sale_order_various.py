"""Example search_read_sale_order_various."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def get_odoo_client():
    return OdooClient(**TEST_SERVER_ACCESS_CONFIG).client


def get_not_confirmed_sale_order_name(odoo):
    out_sales_vals = odoo.search_read(
        'sale.order',
        domain=[[
            ('state', '=', 'draft'),
            ]],
        fields=['name'],
        order='id desc',
        limit=1,
    )
    return out_sales_vals[0]['name']


def get_sale_order_state(odoo, sale_name):
    out_sales_vals = odoo.search_read(
        'sale.order',
        domain=[[
            ('name', '=', sale_name),
            ]],
        fields=['name', 'state'],
        order='id desc',
        limit=1,
    )
    return out_sales_vals[0]['state']


def main():
    odoo = get_odoo_client()
    sale_name = get_not_confirmed_sale_order_name(odoo)
    sale_state = get_sale_order_state(odoo, sale_name)
    print(f"Sale order name: {sale_name}, state: {sale_state}")


if __name__ == '__main__':
    main()
