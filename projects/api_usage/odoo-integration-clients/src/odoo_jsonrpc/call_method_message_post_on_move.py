"""Example call_method_message_post_on_move."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Calls the message post method on an account move instance.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.call(
        'account.move',
        method='message_post',
        ids=[1],
        kwargs={
            'body': 'TEST Message from your friendly developer buddy',
            'message_type': 'comment',
            },
        )


if __name__ == '__main__':
    main()
