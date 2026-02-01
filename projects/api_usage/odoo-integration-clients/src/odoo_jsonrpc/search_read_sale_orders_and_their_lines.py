"""Example search_read_sale_orders_and_their_lines."""
__author__ = 'Joan A. Pinol  (japinol)'

from itertools import groupby

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo_client import OdooClient

MAX_SALES_TO_FETCH = 5
MAX_SALE_LINES_TO_FETCH = 400


def get_grouped(dataset, key_group):
    """Gets the dataset grouped by a key.
    The dataset param must be a sequence of dicts.
    Returns a groupby object grouped by key_group and
    a list of dictionaries with the dataset rows.
    """
    def key_func(x):
        return x[key_group]

    return groupby(sorted(dataset, key=key_func), key_func)


def get_sales_vals(odoo):
    return odoo.search_read(
        'sale.order',
        domain=[
            ('state', 'not in', ('draft', 'cancel')),
            ],
        fields=['name', 'state', 'date_order', 'currency_id',
                'amount_untaxed', 'amount_total',
                'order_line',
                ],
        order='id desc',
        limit=MAX_SALES_TO_FETCH,
        )


def get_sale_lines_vals(odoo, order_line_ids):
    res = odoo.search_read(
        'sale.order.line',
        domain=[
            ('id', 'in', order_line_ids),
            ],
        fields=[
            'name', 'order_id', 'product_uom_qty',
            'price_unit', 'price_subtotal',
            ],
        order='id desc',
        limit=MAX_SALE_LINES_TO_FETCH,
        )
    return res


def print_sales(sales_vals, sale_lines_vals):
    for sale_vals in sales_vals:
        print(f"{sale_vals['name']}, state: {sale_vals['state']}, "
              f"Currency: {sale_vals['currency_id'][1]}, "
              f"Untaxed amount: {sale_vals['amount_untaxed']:<,}, "
              f"Amount total: {sale_vals['amount_total']:<,}")
        if not sale_lines_vals.get(sale_vals['id']):
            print("\t No lines\n")
            continue
        for line in sale_lines_vals[sale_vals['id']]:
            product_name = line['name'].splitlines()[0]
            print(f"\tProduct: {product_name[:40]:40}  "
                  f"Qty: {line['product_uom_qty']:<8,} "
                  f"Price: {line['price_unit']:<12,} "
                  f"Amount: {line['price_subtotal']:<12,}")
        print()


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints sale info and their lines for the five most recent sales
    created that are not canceled and have been confirmed.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    # Fetch sales
    sales_vals = get_sales_vals(odoo)

    # Fetch all sales lines
    order_line_ids = [line for sale in sales_vals
                 for line in sale['order_line']]
    sale_lines_vals = get_sale_lines_vals(odoo, order_line_ids)

    # Remove unnecessary sale order name info from the order id
    for line in sale_lines_vals:
        line['order_id'] = line['order_id'][0]

    # Group the sale lines by sale id and transform the grouped
    # result as a grouping dict with lists of dicts representing the line vals.
    sale_lines_vals = get_grouped(sale_lines_vals, key_group='order_id')
    sale_lines_vals = {k: list(v) for k, v in sale_lines_vals}

    print_sales(sales_vals, sale_lines_vals)


if __name__ == '__main__':
    main()
