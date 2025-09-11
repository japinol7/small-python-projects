## Odoo integration examples: json-rpc and xml-rpc clients
    Odoo integration examples in Python using json-rpc and xml-rpc.
    We have moved the Odoo RPC clients to separate repositories 
    and added them as dependencies.
<br>

	version: 0.0.3
	author: Joan A. Pinol
	author_nickname: japinol
	author_gitHub: japinol7
	author_twitter: @japinol
<br>

	Dependencies:
      * git+https://github.com/japinol7/odoo-jsonrpc.git@v0.0.2
      * git+https://github.com/japinol7/odoo-xmlrpc.git@v0.0.2
	Python requires: 3.13 or greater.
    Tested against Odoo 18.0 CE.
<br>


### More info

* Official Odoo documentation
  * [External API — Odoo 18.0 documentation](https://www.odoo.com/documentation/18.0/developer/reference/external_api.html)

* Official json-rpc documentation
  * [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

<br>

### Implemented Odoo RPC clients added as dependencies
* odoo_jsonrpc
  * odoo_client     -> Te odoo client with the API interface
  * simple_jsonrpc  -> The underlying json-rpc client and connection.
* odoo_xmlrpc
  * odoo_client     -> Te odoo client with the API interface
  * simple_xmlrpc   -> The underlying xml-rpc client and connection.

Both odoo clients are implemented with the same public API,  <br>
so you can change the target package in the following examples <br>
to use xml-rpc instead of json-rpc. 
<br>


### Small programs that can be useful as examples of usage
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
* search_read_products
* search_read_sale_order_various
* search_read_sale_orders
* search_read_sale_orders_and_their_lines
* search_read_users
* unlink_move
* write_addon_state_to_upgrade
* write_environment_ribbon
* write_move

.
