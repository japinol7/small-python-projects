import odoorpc

from .tools.logger.logger import log


class OdooConnection:
    """Represents an Odoo connection."""

    def __init__(
            self, host, dbname, username, password,
            port, proxy_url=None, timeout=10,
        ):
        log.info(f'Connecting to {host}:{port} ({dbname}) as {username}')
        self.odoo = odoorpc.ODOO(
            host, port=int(port), timeout=timeout,
            protocol='jsonrpc+ssl' if int(port) == 443 else 'jsonrpc'
            )
        self.odoo.login(dbname, username, password)
