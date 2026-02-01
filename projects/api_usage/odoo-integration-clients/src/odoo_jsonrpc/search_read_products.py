"""Example search_read_products."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the sale products and whether they are services, goods or combos.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    products_vals = odoo.search_read(
        'product.template',
        domain=[
            ('sale_ok', '=', True),
            ],
        fields=['name', 'type', 'sale_ok', 'purchase_ok'],
        order='name',
        limit=5000,
        )

    for product_val in products_vals:
        print(f"id:{product_val['id']:6}  |  "
              f"{product_val['name'][:55]:55}  |  "
              f"Type: {product_val['type']:8}  |  "
              f"Can be sold: {product_val['sale_ok']}  |  "
              f"Can be purchased: {product_val['purchase_ok']}")

    print(f"{'-' * 137}\nTotal products to sell found: "
          f"{len(products_vals)}")


if __name__ == '__main__':
    main()
