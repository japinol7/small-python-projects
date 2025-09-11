"""Example write_move."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Changes the narration and the checked fields of two invoices.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    odoo.env['account.move'].write(
        [30, 33],
        {'narration': 'TEST 2',
         'checked': True,
         },
        )


if __name__ == '__main__':
    main()
