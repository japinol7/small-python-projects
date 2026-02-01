"""Example search_read_companies."""
__author__ = 'Joan A. Pinol  (japinol)'

from odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses jsonrpc.
    Prints the names of the most recent companies created.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    companies_vals = odoo.env['res.company'].search_read(
        [],
        fields=['name'],
        order='id desc',
        limit=15,
        )

    for company_vals in companies_vals:
        print(f"{company_vals['name']}")

    print(f"{'-' * 40}\n"
          f"Total companies found: {len(companies_vals)}")

if __name__ == '__main__':
    main()
