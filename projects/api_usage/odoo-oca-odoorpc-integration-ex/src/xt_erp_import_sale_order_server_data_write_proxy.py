"""Example xt_erp_import_sale_order_server_data_write_proxy."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    The model and fields we use in this example were created just
    for this example, and they do not exist in Odoo Core.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    vals = {
        'proxy_host': '00.0.0.00',
        'proxy_port': '0000',
        }

    record_ids = odoo.env['jap.import.sale.order.from.ext.odoo'].search(
        [],
        order='id desc',
        )

    if not record_ids:
        print("No records found")
        return

    odoo.env.context['ctx_jap_allow_set_ext_data_importing_sales'] = True
    odoo.env['jap.import.sale.order.from.ext.odoo'].write(
        record_ids,
        vals,
        )


if __name__ == '__main__':
    main()
