"""Example unlink_move."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_json2x.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses json2.
    Deletes a given invoice.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.unlink(
        'account.move',
        ids=[29],
        )


if __name__ == '__main__':
    main()
