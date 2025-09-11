"""Example get_server_version."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Gets the server version.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    version = odoo.version
    print(f"Odoo server version: {version}")


if __name__ == '__main__':
    main()
