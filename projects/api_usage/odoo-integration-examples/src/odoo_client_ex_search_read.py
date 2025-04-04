"""Example odoo_client_ex_search_read."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the names of the five most recent out invoices created
    that are not canceled and have been validated.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    out_invoices_vals = odoo.client.search_read(
        "account.move",
        domain=[[
            ('move_type', '=', 'out_invoice'),
            ('state', 'not in', ('draft', 'cancel')),
            ]],
        fields=['name', 'state'],
        order='id desc',
        limit=5,
        )

    for invs_vals in out_invoices_vals:
        print(f"{invs_vals["name"]}, state: {invs_vals["state"]}")


if __name__ == '__main__':
    main()
