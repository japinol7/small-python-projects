"""Example count_out_invs."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the Number of posted out invoices.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    count_out_sales = odoo.env['account.move'].search_count([
        ('move_type', '=', 'out_invoice'),
        ('state', 'not in', ('draft', 'cancel')),
        ])

    print(f"Number of posted out invoices: {count_out_sales}")


if __name__ == '__main__':
    main()
