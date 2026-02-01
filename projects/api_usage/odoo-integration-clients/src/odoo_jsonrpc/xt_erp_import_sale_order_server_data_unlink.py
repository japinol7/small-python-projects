"""Example xt_erp_import_sale_order_server_data_unlink."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    The model and fields we use in this example were created just
    for this example, and they do not exist in Odoo Core.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    record_ids = odoo.search(
        'jap.import.sale.order.from.ext.odoo',
        domain=[],
        order='id desc',
        )

    if not record_ids:
        print("No records found")
        return

    odoo.unlink(
        'jap.import.sale.order.from.ext.odoo',
        ids=record_ids,
        )


if __name__ == '__main__':
    main()
