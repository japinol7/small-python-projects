"""Example odoo_client_ex_create."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Creates an out invoice for a given customer.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    odoo.client.create(
        'account.move',
        values={
            'partner_id': 27,
            'move_type': 'out_invoice',
            },
        )


if __name__ == '__main__':
    main()
