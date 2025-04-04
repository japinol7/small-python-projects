"""Example odoo_client_ex_count."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the Number of posted out invoices.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    count_out_invoices = odoo.client.search_count(
        "account.move",
        domain=[[
            ('move_type', '=', 'out_invoice'),
            ('state', 'not in', ('draft', 'cancel')),
            ]],
        )

    print(f"Number of posted out invoices: {count_out_invoices}")


if __name__ == '__main__':
    main()
