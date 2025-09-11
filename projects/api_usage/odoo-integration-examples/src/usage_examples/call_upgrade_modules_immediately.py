"""Example call_upgrade_modules_immediately."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def search_installed_module_ids(odoo, module_names):
    """Searches modules by name."""
    return odoo.search(
        'ir.module.module',
        domain=[[
            ('name', 'in', module_names),
            ('state', 'in', ('installed', 'to upgrade')),
            ]],
        order='name ASC',
        limit=len(module_names),
        )


def get_modules_not_found(odoo, modules_to_upgrade, module_ids):
    """Returns which modules to upgrade have not been found."""
    module_names_to_check = odoo.read(
        'ir.module.module',
        ids=module_ids,
        fields=['name'],
        )
    module_names_to_check = [x['name'] for x in module_names_to_check]
    modules_not_found = set(modules_to_upgrade) - set(module_names_to_check)
    return modules_not_found


def upgrade_modules(odoo, module_ids):
    try:
        odoo.call_kw_on_instances(
            'ir.module.module',
            method='button_immediate_upgrade',
            ids=[module_ids],
            values={},
            )
    except Exception as e:
        print(f"Error upgrading modules: {e}")


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Upgrades the given modules immediately if they are already installed.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    modules_to_upgrade = sorted({
        'module_name',
        'another_module_name',
        })

    print(f"Modules to upgrade immediately:\n  > "
          f"{f'\n  > '.join(modules_to_upgrade)}\n")

    module_ids = search_installed_module_ids(odoo, modules_to_upgrade)

    modules_not_found = get_modules_not_found(
        odoo, modules_to_upgrade, module_ids)
    if modules_not_found:
        print(f"Modules not found or not installed: "
              f"{modules_not_found}\n"
              f"No modules upgraded.")
        return

    upgrade_modules(odoo, module_ids)
    print("Modules upgraded.")


if __name__ == '__main__':
    main()
