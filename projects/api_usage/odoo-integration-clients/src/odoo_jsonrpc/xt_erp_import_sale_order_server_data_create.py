"""Example xt_erp_import_sale_order_server_data_create."""
__author__ = 'Joan A. Pinol  (japinol)'

import getpass

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    The model and fields we use in this example were created just
    for this example, and they do not exist in Odoo Core.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    ext_erp_proxy = input("Enter Proxy url: ")
    ext_erp_proxy_port = int(input("Enter Proxy Port: "))
    ext_erp_host_url = input("Enter External Odoo host url: ")
    ext_erp_dbname = input("Enter External Odoo DB name: ")
    ext_erp_username = input("Enter External Odoo username: ")
    ext_erp_password = getpass.getpass('Enter External Odoo user password: ')

    vals = {
        'url': ext_erp_host_url,
        'dbname': ext_erp_dbname,
        'username': ext_erp_username,
        'password': ext_erp_password,
        }

    if ext_erp_proxy:
        vals.update({
            'proxy_host': ext_erp_proxy,
            'proxy_port': ext_erp_proxy_port,
            })

    odoo.create(
        'jap.import.sale.order.from.ext.odoo',
        vals=vals,
        )


if __name__ == '__main__':
    main()
