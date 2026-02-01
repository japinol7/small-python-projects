"""Example xt_erp_import_sale_order_server_data_read."""
__author__ = 'Joan A. Pinol  (japinol)'

import json

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    The model and fields we use in this example were created just
    for this example, and they do not exist in Odoo Core.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    vals = odoo.env['jap.import.sale.order.from.ext.odoo'].search_read(
        [],
        fields=[
            'id', 'url', 'dbname', 'username', 'proxy_host', 'proxy_port'],
        order='id desc',
        )

    vals_json = json.dumps(vals, indent=4)
    print(vals_json)


if __name__ == '__main__':
    main()
