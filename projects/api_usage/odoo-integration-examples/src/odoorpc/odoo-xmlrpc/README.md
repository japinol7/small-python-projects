## Odoo xml-rpc
    Odoo xml-rpc client wihout external dependencies.
<br>

	version: 0.0.2
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

<br>

### Implemented client
* odoo_xmlrpc
  * odoo_client     -> Te odoo client with the API interface
  * simple_xmlrpc  -> The underlying xml-rpc client and connection.


### Small programs that can be useful as examples of usage

* Odoo integration examples in Python using this Odoo xml-rpc package
    * [odoo-integration-examples](https://github.com/japinol7/odoo-integration-examples)

    Note: You will need to change the imports of the examples from odoo_jsonrpc to odoo_xmlrpc. <br>
    Ex: from odoo_xmlrpc.odoo_client import OdooClient

<br>

### Install the last package tag released from this repo in your project
Add this to your requirements.txt file: <br>

    git+https://github.com/japinol7/odoo-xmlrpc.git@v0.0.2

<br>
Alternatively, if you use an uv toml file: <br>

    dependencies = [
        "odoo-xmlrpc",
    ]
    
    [tool.uv.sources]
    odoo-xmlrpc = { git = "https://github.com/japinol7/odoo-xmlrpc.git", rev = "v0.0.2" }

<br>
.
