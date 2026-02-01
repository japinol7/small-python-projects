"""Example read_group_out_invoices."""
__author__ = 'Joan A. Pinol  (japinol)'

from pprint import pp

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Gets the aggregated amounts of validated out invoices grouped by company.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    data = odoo.read_group(
        'account.move',
        domain=[
            ('move_type', '=', 'out_invoice'),
            ('state', 'not in', ('draft', 'cancel')),
            ],
        fields=['company_id', 'amount_untaxed', 'amount_total'],
        group_by=['company_id'],
        )

    pp(data)


if __name__ == '__main__':
    main()
