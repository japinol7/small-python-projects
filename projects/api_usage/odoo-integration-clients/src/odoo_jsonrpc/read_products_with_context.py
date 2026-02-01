"""Example read_products_with_context."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the name, and type of some products.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    products_vals = odoo.read(
        'product.template',
        ids=list(range(1, 10)),
        fields=['name', 'type'],
        context={'lang': 'en_US'},
        )

    for product_vals in products_vals:
        print(f"{product_vals['name']:10}, type: {product_vals['type']:8}")


if __name__ == '__main__':
    main()
