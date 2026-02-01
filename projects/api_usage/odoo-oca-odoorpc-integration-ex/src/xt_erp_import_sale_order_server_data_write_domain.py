"""Example xt_erp_import_sale_order_server_data_write_domain."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    The model and fields we use in this example were created just
    for this example, and they do not exist in Odoo Core.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    val_to_change = ("["
         "('date_sold', '>=', '2024-01-01'), ('state', '=', 'done'), "
         "'|', ('sync_sale_order', '=', False), ('sync_sale_order', '=', 'to_update')"
         "]")

    vals = {
        'sale_erp_import_domain': val_to_change,
        }

    record_ids = odoo.env['jap.sale.config'].search(
        [('id', '=', 1)],
        order='id desc',
        )

    if not record_ids:
        print("No records found")
        return

    odoo.env.context['ctx_jap_allow_set_ext_data_importing_sales'] = True
    odoo.env['jap.sale.config'].write(
        record_ids,
        vals,
        )


if __name__ == '__main__':
    main()
