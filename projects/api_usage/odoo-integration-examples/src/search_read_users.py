"""Example search_read_users."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Fetches active users and prints their username and login.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    users_vals = odoo.search_read(
        'res.users',
        domain=[[
            # This domain condition ensures only active users are fetched,
            # although this is not strictly necessary as odoo defaults
            # to active records.
            ('active', '=', True),
            ]],
        fields=['name', 'login'],
        order='name',
        limit=500,
        )

    for user_vals in users_vals:
        print(f"{user_vals['name']:40} {user_vals['login']}")
    print(f"{'-'*80}\nTotal users found: {len(users_vals)}")


if __name__ == '__main__':
    main()
