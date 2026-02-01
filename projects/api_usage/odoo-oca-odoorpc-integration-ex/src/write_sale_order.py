"""Example write_sale_order."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Changes the narration and the checked fields of two sale orders.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    odoo.env['sale.order'].write(
        [1, 2],
        {'note': 'TEST',
         },
        )


if __name__ == '__main__':
    main()
