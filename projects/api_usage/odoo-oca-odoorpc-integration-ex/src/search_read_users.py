"""Example search_read_users."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def print_users_info(users_vals):
    users_info = sorted((
        (user['name'] or '',
         user['login'] or '',
         ) for user in users_vals),
        key=lambda x: x[0].lower())

    users_info_str = [f"{user[0]:50}{user[1]}" for user in users_info]

    print(f"{'\n'.join(users_info_str)}\n"
          f"{'-' * 80}\nTotal users found: {len(users_info)}")


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Fetches active users and prints their username and login.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    users_vals = odoo.env['res.users'].search_read([
        # This domain condition ensures only active users are fetched,
        # although this is not strictly necessary as odoo defaults
        # to active records.
        ('active', '=', True),
        ],
        fields=['name', 'login'],
        order='name',
        limit=500,
        )

    print_users_info(users_vals)


if __name__ == '__main__':
    main()
