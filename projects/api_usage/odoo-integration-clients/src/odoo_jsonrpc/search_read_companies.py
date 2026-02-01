"""Example search_read_companies."""
__author__ = 'Joan A. Pinol  (japinol)'

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints the names of the most recent companies created.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    companies_vals = odoo.search_read(
        'res.company',
        domain=[],
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
