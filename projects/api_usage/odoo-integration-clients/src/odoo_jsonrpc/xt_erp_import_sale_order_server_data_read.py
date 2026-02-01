"""Example xt_erp_import_sale_order_server_data_read."""
__author__ = 'Joan A. Pinol  (japinol)'

import json

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    The model and fields we use in this example were created just
    for this example, and they do not exist in Odoo Core.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    vals = odoo.search_read(
        'jap.import.sale.order.from.ext.odoo',
        domain=[],
        fields=[
            'id', 'url', 'dbname', 'username', 'proxy_host', 'proxy_port'],
        order='id desc',
        )

    vals_json = json.dumps(vals, indent=4)
    print(vals_json)


if __name__ == '__main__':
    main()
