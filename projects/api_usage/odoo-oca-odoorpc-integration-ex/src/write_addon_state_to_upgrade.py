"""Example write_addon_state_to_upgrade."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG
from src.odoo.tools.logger.logger import log


def fetch_addon_id(odoo, addon_name):
    addon_ids = odoo.env['ir.module.module'].search([
        ('name', '=', addon_name),
        ('state', 'not in',
         ('uninstalled', 'to install', 'uninstallable')
         ),
        ],
        limit=1,
        )
    if not addon_ids:
        raise Exception(f"Addon '{addon_name}' not found")

    return addon_ids[0]


def set_addon_state_to_upgrade(odoo, addon_id):
    odoo.env['ir.module.module'].write(
        [addon_id],
        { 'state': 'to upgrade',
          },
        )

def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Changes the state of one addon so will be upgraded once the server
    restarts.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    addon_name = 'module_name'
    addon_id = fetch_addon_id(odoo, addon_name)

    if not addon_id:
        return

    log.info(f"Set addon {addon_name} to state 'to upgrade'")
    set_addon_state_to_upgrade(odoo, addon_id)


if __name__ == '__main__':
    main()
