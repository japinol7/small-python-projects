"""Example read_sales_more_info."""
__author__ = 'Joan A. Pinol  (japinol)'

from pprint import pp

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient

SALE_FIELDS = [
    'id',
    'name',
    'state',
    'user_id',
    'company_id',
    ]
USER_FIELDS = [
    'id',
    'name',
    'login',
    'contact_address',
    'country_code',
    ]
COMPANY_FIELDS = [
    'id',
    'name',
    'currency_id',
    'website',
    ]


def get_sales_vals(odoo, ids):
    return odoo.read(
        'sale.order',
        ids=ids,
        fields=SALE_FIELDS,
        )


def get_users_vals(odoo, user_ids):
    return odoo.read(
        'res.users',
        ids=user_ids,
        fields=USER_FIELDS,
        )


def get_company_vals(odoo, company_ids):
    return odoo.read(
        'res.company',
        ids=company_ids,
        fields=COMPANY_FIELDS,
        )


def get_entities_vals_by_id(entities_vals):
    res = {}
    for entity_vals in entities_vals:
        res[entity_vals['id']] = entity_vals
    return res


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints some first and second-level info about some sales.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    sale_ids_to_fetch = [1, 2]
    sales_vals = get_sales_vals(odoo, ids=sale_ids_to_fetch)

    user_ids = [sale_vals['user_id'][0] for sale_vals in sales_vals]
    users_vals = get_users_vals(odoo, user_ids)
    users_vals_dict = get_entities_vals_by_id(users_vals)

    companies_ids = [sale_vals['company_id'][0] for sale_vals in sales_vals]
    companies_vals = get_company_vals(odoo, companies_ids)
    companies_vals_dict = get_entities_vals_by_id(companies_vals)

    for sale_vals in sales_vals:
        user_id = sale_vals['user_id'][0]
        for field in USER_FIELDS:
            if field in ('id', 'name'):
                continue
            sale_vals[field] = users_vals_dict[user_id][field]

        company_id = sale_vals['company_id'][0]
        for field in COMPANY_FIELDS:
            if field in ('id', 'name'):
                continue
            sale_vals[field] = companies_vals_dict[company_id][field]

    pp(sales_vals)


if __name__ == '__main__':
    main()
