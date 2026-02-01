## Odoo integration clients: json-2, json-rpc, and xml-rpc
    Odoo integration clients in Python using json-2, json-rpc, and xml-rpc.
<br>

	version: 0.0.6
	author: Joan A. Pinol
	author_nickname: japinol
	author_gitHub: japinol7
	author_twitter: @japinol
<br>

	Dependencies:
      * requests
	Python requires: 3.13 or greater.
    Tested against Odoo 19.0 CE and PostgreSQL 18.1.
<br>


### More info

* Official Odoo documentation
  * [Web Services — Odoo 18.0 documentation](https://www.odoo.com/documentation/18.0/developer/howtos/web_services.html)
  * [External API — Odoo 18.0 documentation](https://www.odoo.com/documentation/18.0/developer/reference/external_api.html)

* Official json-rpc documentation
  * [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

<br>

### Implemented Json-2 Odoo clients - For Odoo 19.0+
* odoo-json2
  * Simple json-2 client using 'requests' as the underlying transport.
  * odoo_client   -> Te odoo client with the API interface
  * simple_json2  -> The underlying json-2 client and connection.
* odoo-json2x
  * Simple json-2 client using 'httpx' as the underlying transport.
  * odoo_client   -> Te odoo client with the API interface
  * simple_json2  -> The underlying json-2 client and connection.
* odoo-json2xa
  * More advanced json-2 client using 'httpx' as the underlying transport, <br>
    with support for some advanced features.
  * odoo_client   -> Te odoo client with the API interface
  * simple_json2  -> The underlying json-2 client and connection.

All JSON-2 Odoo clients are implemented with the same basic public API,  <br>
so you can change the target package in the following examples <br>
to use xml-rpc or json-rpc instead of json-2. 

### Implemented RPC Odoo clients - For Odoo 10.0 to 19.0
* odoo-jsonrpc
  * odoo_client     -> Te odoo client with the API interface
  * simple_jsonrpc  -> The underlying json-rpc client and connection.
* odoo-xmlrpc
  * odoo_client     -> Te odoo client with the API interface
  * simple_xmlrpc   -> The underlying xml-rpc client and connection.

All RPC Odoo clients are implemented with the same public API,  <br>
so you can change the target package in the following examples <br>
to use xml-rpc or json-rpc instead of json-2. 
<br>


### Small programs that can be useful as examples of usage
* call_method_message_post_on_move
* call_method_message_post_on_sale
* call_model_method_get_invoice_types
* call_model_method_jap_waste_some_time
* call_upgrade_modules_immediately
* count_out_invs
* count_sale_orders
* create_out_inv
* create_sale_quotation
* get_db_list
* get_server_version
* read_group_out_invoices
* read_group_sales
* read_out_invs
* read_products_with_context
* read_sales
* read_sales_more_info
* search_out_invs
* search_read_companies
* search_read_contacts
* search_read_out_invs
* search_read_out_invs_and_their_lines
* search_read_product_various
* search_read_products
* search_read_products_with_context
* search_read_products_with_global_context
* search_read_sale_order_various
* search_read_sale_orders
* search_read_sale_orders_and_their_lines
* search_read_users
* unlink_move
* unlink_sale_order
* write_addon_state_to_upgrade
* write_environment_ribbon
* write_move
* write_sale_order
* xt_erp_import_sale_order_server_data_create
* xt_erp_import_sale_order_server_data_read
* xt_erp_import_sale_order_server_data_unlink
* xt_erp_import_sale_order_server_data_write
* xt_erp_import_sale_order_server_data_write_domain 
* xt_erp_import_sale_order_server_data_write_proxy

.
