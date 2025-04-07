"""Example call_model_method_message_post_on_move."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Calls the message post method on some account move instances.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    odoo.call_kw_on_instances(
        'account.move',
        method='message_post',
        ids=[1],
        values={
            'body': 'TEST Message from your friendly developer buddy',
            'message_type': 'comment',
            },
        )


if __name__ == '__main__':
    main()
