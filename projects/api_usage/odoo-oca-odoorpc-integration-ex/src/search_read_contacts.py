"""Example search_read_contacts."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def print_partners_info(partners_vals):
    partners_info = sorted((
        (partner['name'] or '',
         partner['email'] or '',
         partner['country_id'] and partner['country_id'][1] or '',
         ) for partner in partners_vals),
        key=lambda x: x[0].lower())

    partners_info_str = [f"{p[0]:50}{p[1]:40}{p[2]}" for p in partners_info]

    print(f"{'\n'.join(partners_info_str)}\n"
          f"{'-' * 80}\nTotal partners found: {len(partners_info)}")


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Fetches active partners and prints their name, email and country.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    partners_vals = odoo.env['res.partner'].search_read([],
        fields=['name', 'email', 'country_id'],
        order='name',
        limit=500,
        )

    print_partners_info(partners_vals)


if __name__ == '__main__':
    main()
