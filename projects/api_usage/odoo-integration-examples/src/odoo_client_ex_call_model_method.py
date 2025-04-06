"""Example odoo_client_ex_call_model_method."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo_client_ex_config import TEST_SERVER_ACCESS_CONFIG
from odoo_using_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Calls a given method on the account move model to get all the
    invoice types, including receipts.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG)

    invoice_types = odoo.client.call(
        'account.move',
        method='get_invoice_types',
        values={
            'include_receipts': True,
            },
        )

    print(invoice_types)
    

if __name__ == '__main__':
    main()
