## Odoo integration examples: json-rpc and xml-rpc clients
    Odoo integration examples in Python using json-rpc and xml-rpc.
<br>

	version: 0.0.1
	author: Joan A. Pinol
	author_nickname: japinol
	author_gitHub: japinol7
	author_twitter: @japinol
<br>

	Dependencies: None.
	Python requires: 3.13 or greater.
    Tested against Odoo 18.0 CE.
<br>


### More info

* Official Odoo documentation
  * [External API — Odoo 18.0 documentation](https://www.odoo.com/documentation/18.0/developer/reference/external_api.html)

* Official json-rpc documentation
  * [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

<br>

### Implemented clients
* odoo_using_jsonrpc
  * odoo_client  -> Te odoo client with the API interface
  * jsonrpc_jap  -> The underlying json-rpc client and connection.
* odoo_using_xmlrpc
  * odoo_client  -> Te odoo client with the API interface
  * xmlrpc_jap   -> The underlying xml-rpc client and connection.

Both odoo clients are implemented with the same public API,  <br>
so you can change the target package in the following examples <br>
to use xml-rpc instead of json-rpc. 
<br>


### Small programs that can be useful as examples of usage
  * odoo_client_ex_call_model_method
  * odoo_client_ex_call_model_method_message_post
  * odoo_client_ex_config
  * odoo_client_ex_count
  * odoo_client_ex_create
  * odoo_client_ex_get_server_version
  * odoo_client_ex_read
  * odoo_client_ex_search
  * odoo_client_ex_search_read
  * odoo_client_ex_search_read_invs_and_their_lines
  * odoo_client_ex_unlink
  * odoo_client_ex_write
  * odoo_client_ex_write_addon_state_to_upgrade
