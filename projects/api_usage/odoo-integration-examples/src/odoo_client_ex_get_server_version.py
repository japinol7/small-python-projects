"""Example odoo_client_ex_get_server_version."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Gets the server version.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    version = odoo.client.get_server_version()
    print(f"Odoo server version: {version}")


if __name__ == '__main__':
    main()
