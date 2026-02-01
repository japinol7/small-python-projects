"""Example get_db_list."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Gets the available databases.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    db_names = odoo.db.list()
    print(f"Available databases: {db_names}")


if __name__ == '__main__':
    main()
