"""Example odoo_client_ex_unlink."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Deletes a given invoice.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    odoo.client.unlink(
        "account.move",
        ids=[29],
        )


if __name__ == '__main__':
    main()
