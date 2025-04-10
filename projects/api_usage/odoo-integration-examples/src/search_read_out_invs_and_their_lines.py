"""Example search_read_out_invs_and_their_lines."""
__author__ = 'Joan A. Pinol  (japinol)'

from itertools import groupby

from config import TEST_SERVER_ACCESS_CONFIG
from odoo_jsonrpc.odoo.odoo_client import OdooClient

MAX_INVOICES_TO_FETCH = 5
MAX_INVOICE_LINES_TO_FETCH = 400


def get_grouped(dataset, key_group):
    """Gets the dataset grouped by a key.
    The dataset param must be a sequence of dicts.
    Returns a groupby object grouped by key_group and
    a list of dictionaries with the dataset rows.
    """
    def key_func(x):
        return x[key_group]

    return groupby(sorted(dataset, key=key_func), key_func)


def get_out_invoices_vals(odoo):
    return odoo.search_read(
        'account.move',
        domain=[[
            ('move_type', '=', 'out_invoice'),
            ('state', 'not in', ('draft', 'cancel')),
            ]],
        fields=['name', 'state', 'invoice_date',
                'currency_id', 'amount_untaxed',
                'amount_total', 'invoice_line_ids',
                ],
        order='id desc',
        limit=MAX_INVOICES_TO_FETCH,
        )


def get_invoice_lines_vals(odoo, line_ids):
    res = odoo.search_read(
        'account.move.line',
        domain=[[
            ('id', 'in', line_ids),
            ]],
        fields=[
            'name', 'move_id', 'quantity', 'price_unit',
            'price_subtotal',
            ],
        order='id desc',
        limit=MAX_INVOICE_LINES_TO_FETCH,
        )
    return res


def print_invoices(out_invoices_vals, invoice_lines_vals):
    for inv_vals in out_invoices_vals:
        print(f"{inv_vals['name']}, state: {inv_vals['state']}, "
              f"Invoice date: {inv_vals['invoice_date']}, "
              f"Currency: {inv_vals['currency_id'][1]}, "
              f"Untaxed amount: {inv_vals['amount_untaxed']:<,}, "
              f"Amount total: {inv_vals['amount_total']:<,}")
        if not invoice_lines_vals.get(inv_vals['id']):
            print("\t No lines\n")
            continue
        for line in invoice_lines_vals[inv_vals['id']]:
            product_name = line['name'].splitlines()[0]
            print(f"\tProduct: {product_name[:40]:40}  "
                  f"Qty: {line['quantity']:<8,} "
                  f"Price: {line['price_unit']:<12,} "
                  f"Amount: {line['price_subtotal']:<12,}")
        print()


def main():
    """Example of usage for the odoo connection that uses jsonrpc or xmlrpc.
    Prints invoice info and their lines for the five most recent out
    invoices created that are not canceled and have been validated.
    """
    odoo = OdooClient(**TEST_SERVER_ACCESS_CONFIG).client

    # Fetch invoices
    out_invoices_vals = get_out_invoices_vals(odoo)

    # Fetch all invoices lines
    line_ids = [line for inv in out_invoices_vals
                 for line in inv['invoice_line_ids']]
    invoice_lines_vals = get_invoice_lines_vals(odoo, line_ids)

    # Remove unnecessary move name info from the move id
    for line in invoice_lines_vals:
        line['move_id'] = line['move_id'][0]

    # Group the invoice lines by invoice id and transform the grouped
    # result as a grouping dict with lists of dicts representing the line vals.
    invoice_lines_vals = get_grouped(invoice_lines_vals, key_group='move_id')
    invoice_lines_vals = {k: list(v) for k, v in invoice_lines_vals}

    print_invoices(out_invoices_vals, invoice_lines_vals)


if __name__ == '__main__':
    main()
