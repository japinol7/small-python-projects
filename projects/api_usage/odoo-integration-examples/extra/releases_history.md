# Release History

## v0.0.3

### New features and improvements:
* We have moved the Odoo RPC clients to separate repositories and added them as dependencies.
    * odoo-jsonrpc
    * odoo-xmlrpc

* Add examples of usage:
    * search_read_products


## v0.0.2

### New features and improvements:
* Add project toml files for packages, so they can be <br> installed from their directories:
  * odoo-jsonrpc
  * odoo-xmlrpc

* Add examples of usage:
  * search_read_sale_order_various

* Update examples of usage imports with the new setup.


## v0.0.1

### New features and improvements:

* Add connectors and clients to the Odoo External API:
  * Add json-rpc connector and client.
  * Add xml-rpc connector and client.

* Add examples of usage:
  * call_model_method_get_invoice_types
  * call_model_method_message_post_on_move
  * call_model_method_message_post_on_sale
  * call_upgrade_modules_immediately
  * count_out_invs
  * count_sale_orders
  * create_out_inv
  * create_sale_quotation
  * get_server_version
  * read_out_invs
  * search_out_invs
  * search_read_contacts
  * search_read_out_invs
  * search_read_out_invs_and_their_lines
  * search_read_sale_orders
  * search_read_sale_orders_and_their_lines
  * search_read_users
  * unlink_move
  * write_addon_state_to_upgrade
  * write_environment_ribbon
  * write_move
