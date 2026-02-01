"""Example call_model_method_jap_waste_some_time."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient
from odoo_jsonrpc.tools.logger.logger import log


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Calls a given method on the sale order model to check the timeout behavior.
    The method we call in this example is a custom method created just
    for this example, and it does not exist in Odoo Core.
    The called method should log each second wasted and return the
    total seconds wasted.
    It should waste time only if the context has this key: ctx_jap_allow_waste_some_time.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    res = odoo.call_on_model(
        'sale.order',
        method='jap_waste_some_time',
        kwargs={
            'time_to_waste': 2,
            },
        context={'ctx_jap_allow_waste_some_time': True},
        )

    log.info(f"Seconds wasted: {res}")


if __name__ == '__main__':
    main()
