"""Example read_sales."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the name, state, and company of some sales.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    sales_vals = odoo.env['sale.order'].read(
        [2, 1],
        fields=['name', 'state', 'company_id'],
        )

    for sale_vals in sales_vals:
        print(f"{sale_vals['name']:10}, state: {sale_vals['state']:8}, "
              f"Company: [{sale_vals['company_id'][0]:7}] "
              f"{sale_vals['company_id'][1]}")


if __name__ == '__main__':
    main()
