"""Example call_model_method_get_invoice_types."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Calls a given method on the account move model to get all the
    invoice types, including receipts.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    invoice_types = odoo.call(
        'account.move',
        method='get_invoice_types',
        values={
            'include_receipts': True,
            },
        )

    print(invoice_types)
    

if __name__ == '__main__':
    main()
