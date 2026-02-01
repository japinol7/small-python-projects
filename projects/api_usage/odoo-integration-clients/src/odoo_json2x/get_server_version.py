"""Example get_server_version."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_json2x.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses json2.
    Gets the server version.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    version = odoo.get_server_version()
    print(f"Odoo server version: {version}")


if __name__ == '__main__':
    main()
