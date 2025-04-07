"""Example write_move."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Changes the narration and the checked fields of two invoices.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.write(
        'account.move',
        ids=[1, 2],
        values={
            'narration': 'TEST',
            'checked': True,
            },
        )


if __name__ == '__main__':
    main()
