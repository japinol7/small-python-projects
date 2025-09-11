"""Example write_environment_ribbon."""
__author__ = 'Joan A. Pinol  (japinol)'

from pprint import pp

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo.tools.logger.logger import log
from odoo_jsonrpc.odoo_client import OdooClient

RIBBON_STAGING_PARAMS_DEFAULT = {
    'ribbon.name': 'Staging',
    'ribbon.color': '#f0f0f0',
    'ribbon.background.color': 'rgba(255,0,0,.6)',
    }
RIBBON_STAGING_PARAMS_CUSTOM = {
    'ribbon.name': 'Staging JP-1',
    'ribbon.color': '#ee0505',
    'ribbon.background.color': 'rgba(255,175,0,.6)',
    }


def fetch_ribbon_parameters(odoo):
    return odoo.search_read(
        'ir.config_parameter',
        domain=[[
            ('key', 'in',
             ('ribbon.name', 'ribbon.color', 'ribbon.background.color')
             ),
            ]],
        fields=['key', 'value'],
        limit=5,
        )

def set_ir_config_parameter(odoo, key_id, value):
    odoo.write(
        'ir.config_parameter',
        ids=[key_id],
        values={
            'value': value,
            },
        )


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Changes the staging ribbon parameters.
    Warning: the following OCA addon must be installed to use this example:
      * https://github.com/OCA/web/blob/18.0/web_environment_ribbon
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    vals = fetch_ribbon_parameters(odoo)
    if not vals:
        log.warning(
            "No ribbon parameters found. "
            "The web_environment_ribbon addon may not be installed!")
        return

    print("Ribbon parameters before executing:")
    pp(vals)

    vals = {item['id']: RIBBON_STAGING_PARAMS_CUSTOM[item['key']]
            for item in vals}
    for k, v in vals.items():
        set_ir_config_parameter(odoo, k, v)

    print("\nRibbon parameters after executing:")
    vals = fetch_ribbon_parameters(odoo)
    pp(vals)


if __name__ == '__main__':
    main()
