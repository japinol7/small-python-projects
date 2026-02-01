"""Example read_group_out_invoices."""
__author__ = 'Joan A. Pinol  (japinol)'

from pprint import pp

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Gets the aggregated amounts of validated out invoices grouped by company.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    data = odoo.execute_kw(
        'account.move',
        method='read_group',
        kwargs={
            'domain': [
                ('move_type', '=', 'out_invoice'),
                ('state', 'not in', ('draft', 'cancel')),
                ],
            'fields': ['company_id', 'amount_untaxed', 'amount_total'],
            'groupby': 'company_id',
            },
        )

    pp(data)


if __name__ == '__main__':
    main()
