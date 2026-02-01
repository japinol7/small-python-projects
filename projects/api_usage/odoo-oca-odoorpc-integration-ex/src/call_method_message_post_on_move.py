"""Example call_method_message_post_on_move."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Calls the message post method on an account move instance.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    odoo.execute_kw(
        'account.move',
        method='message_post',
        args=[1],
        kwargs={
            'body': 'TEST Message from your friendly developer buddy',
            'message_type': 'comment',
            },
        )


if __name__ == '__main__':
    main()
