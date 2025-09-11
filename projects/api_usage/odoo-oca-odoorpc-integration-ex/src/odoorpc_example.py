from src.odoo.res_connection import OdooConnection
from config import TEST_SERVER_ACCESS_CONFIG


def main():
    """Example of usage for the odoo connection that uses odoorpc.
    Prints the names of the five most recent invoices.
    """
    odoo = OdooConnection(**TEST_SERVER_ACCESS_CONFIG).odoo

    out_invoice_ids = odoo.env['account.move'].search(
        domain=[('id', '>', 0)],
        order="id desc",
        limit=5,
        )
    for inv in odoo.env["account.move"].browse(out_invoice_ids):
        if inv.name:
            print(inv.name)


if __name__ == '__main__':
    main()
