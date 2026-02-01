"""Example write_sale_order."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_json2x.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses json2.
    Changes the narration and the checked fields of two sale orders.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.write(
        'sale.order',
        ids=[1, 2],
        vals={
            'note': 'TEST',
            },
        )


if __name__ == '__main__':
    main()
