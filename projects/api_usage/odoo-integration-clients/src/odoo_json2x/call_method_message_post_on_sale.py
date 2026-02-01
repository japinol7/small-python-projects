"""Example call_method_message_post_on_sale."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_json2x.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses json2.
    Calls the message post method on a sale order instance.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.call(
        'sale.order',
        method='message_post',
        ids=[1],
        body='TEST Message from your friendly developer buddy',
        message_type='comment',
        )


if __name__ == '__main__':
    main()
