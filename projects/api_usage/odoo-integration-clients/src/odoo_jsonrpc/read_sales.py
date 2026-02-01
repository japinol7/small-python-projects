"""Example read_sales."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the name, state, and company of some sales.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    sales_vals = odoo.read(
        'sale.order',
        ids=[2, 1],
        fields=['name', 'state', 'company_id'],
        )

    for sale_vals in sales_vals:
        print(f"{sale_vals['name']:10}, state: {sale_vals['state']:8}, "
              f"Company: [{sale_vals['company_id'][0]:7}] "
              f"{sale_vals['company_id'][1]}")


if __name__ == '__main__':
    main()
