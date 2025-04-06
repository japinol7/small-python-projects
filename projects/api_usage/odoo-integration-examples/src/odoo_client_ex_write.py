"""Example odoo_client_ex_write."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Changes the narration and the checked fields of two invoices.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    odoo.client.write(
        'account.move',
        ids=[1, 2],
        values={
            'narration': 'TEST',
            'checked': True,
            },
        )


if __name__ == '__main__':
    main()
