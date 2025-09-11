"""Example call_model_method_get_invoice_types."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Calls a given method on the account move model to get all the
    invoice types, including receipts.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    invoice_types = odoo.execute_kw(
        'account.move',
        method='get_invoice_types',
        kwargs={
                'include_receipts': True,
            }
        )

    print(invoice_types)
    

if __name__ == '__main__':
    main()
