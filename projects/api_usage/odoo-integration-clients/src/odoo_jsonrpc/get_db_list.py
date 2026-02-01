"""Example get_db_list."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Gets the available databases.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    db_names = odoo.get_db_list()
    print(f"Available databases: {db_names}")


if __name__ == '__main__':
    main()
