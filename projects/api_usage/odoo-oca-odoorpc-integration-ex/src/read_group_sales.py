"""Example read_group_sales."""
__author__ = 'Joan A. Pinol  (japinol)'

from pprint import pp

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Gets the aggregated amounts of all sales grouped by company.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    data = odoo.execute_kw(
        'sale.order',
        method='read_group',
        kwargs={
            'domain': [ ],
            'fields': ['company_id', 'amount_untaxed', 'amount_total'],
            'groupby': 'company_id',
            },
        )

    pp(data)


if __name__ == '__main__':
    main()
