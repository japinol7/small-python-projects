"""Example write_addon_state_to_upgrade."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo.tools.logger.logger import log
from odoo_jsonrpc.odoo.odoo_client import OdooClient


def fetch_addon_id(odoo, addon_name):
    addon_ids = odoo.search(
        'ir.module.module',
        domain=[[
            ('name', '=', addon_name),
            ('state', 'not in',
                ('uninstalled', 'to install', 'uninstallable')
             ),
            ]],
        limit=1,
        )
    if not addon_ids:
        raise Exception(f"Addon '{addon_name}' not found")

    return addon_ids[0]


def set_addon_state_to_upgrade(odoo, addon_id):
    odoo.write(
        'ir.module.module',
        ids=[addon_id],
        values={
            'state': 'to upgrade',
            },
        )

def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Changes the state of one addon so will be upgraded once the server
    restarts.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    addon_name = 'jap_sale'
    addon_id = fetch_addon_id(odoo, addon_name)

    if not addon_id:
        return

    log.info(f"Set addon {addon_name} to state 'to upgrade'")
    set_addon_state_to_upgrade(odoo, addon_id)


if __name__ == '__main__':
    main()
