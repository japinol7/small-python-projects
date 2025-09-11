## Odoo json-rpc
    Odoo json-rpc client wihout external dependencies.
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

* Official json-rpc documentation
  * [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

<br>

### Implemented client
* odoo_jsonrpc
  * odoo_client     -> Te odoo client with the API interface
  * simple_jsonrpc  -> The underlying json-rpc client and connection.


### Small programs that can be useful as examples of usage

* Odoo integration examples in Python using this Odoo json-rpc package
    * [odoo-integration-examples](https://github.com/japinol7/odoo-integration-examples)

<br>

### Install the last package tag released from this repo in your project
Add this to your requirements.txt file: <br>

    git+https://github.com/japinol7/odoo-jsonrpc.git@v0.0.2

<br>
Alternatively, if you use an uv toml file: <br>

    dependencies = [
        "odoo-jsonrpc",
    ]
    
    [tool.uv.sources]
    odoo-jsonrpc = { git = "https://github.com/japinol7/odoo-jsonrpc.git", rev = "v0.0.2" }

<br>
.
