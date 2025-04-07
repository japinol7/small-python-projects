"""Example search_out_invs."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the ids of the five most recent out invoices
    that are not canceled and have been validated.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    out_invoices_ids = odoo.search(
        'account.move',
        domain=[[
            ('move_type', '=', 'out_invoice'),
            ('state', 'not in', ('draft', 'cancel')),
            ]],
        order='id desc',
        limit=5,
        )

    print(out_invoices_ids)


if __name__ == '__main__':
    main()
