"""Example search_out_invs."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the ids of the five most recent out invoices
    that are not canceled and have been validated.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    out_invoices_ids = odoo.env['account.move'].search(
        domain=[
            ('move_type', '=', 'out_invoice'),
            ('state', 'not in', ('draft', 'cancel')),
            ],
        order='id desc',
        limit=5,
        )

    print(out_invoices_ids)


if __name__ == '__main__':
    main()
