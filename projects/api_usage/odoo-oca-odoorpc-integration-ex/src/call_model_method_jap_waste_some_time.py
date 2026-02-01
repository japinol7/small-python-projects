"""Example call_model_method_jap_waste_some_time."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG
from odoo.tools.logger.logger import log


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Calls a given method on the sale order model to check the timeout behavior.
    The method we call in this example is a custom method created just
    for this example, and it does not exist in Odoo Core.
    The called method should log each second wasted and return the
    total seconds wasted.
    It should waste time only if the context has this key: ctx_jap_allow_waste_some_time.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    res = odoo.execute_kw(
        'sale.order',
        method='jap_waste_some_time',
        kwargs={
            'time_to_waste': 2,
            'context': {'ctx_jap_allow_waste_some_time': True},
            },
        )

    log.info(f"Seconds wasted: {res}")


if __name__ == '__main__':
    main()
