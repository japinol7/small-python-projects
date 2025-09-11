"""Example unlink_move."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Deletes a given invoice.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    odoo.env['account.move'].unlink(
        [29],
        )


if __name__ == '__main__':
    main()
