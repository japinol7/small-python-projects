import os

import odoorpc

from .tools.logger.logger import log


class OdooConnection:
    """Represents an Odoo connection."""

    def __init__(
            self, host, dbname, username, password,
            port, proxy_host=None, proxy_port=None, timeout=15,
        ):
        log.info(f"Connecting to {host}:{port} ({dbname}) as {username}")

        if proxy_host and proxy_port:
            proxy_url = f"http://{proxy_host}:{int(proxy_port)}"
            try:
                os.environ['HTTP_PROXY'] = proxy_url
                os.environ['HTTPS_PROXY'] = proxy_url
                log.info("Env proxies set for use in the odoo session")
            except Exception as e:
                log.error(
                    f"Failed to set env proxies {proxy_host}:{proxy_port}: {e}")

        self.odoo = odoorpc.ODOO(
            host, port=int(port), timeout=timeout,
            protocol='jsonrpc+ssl' if int(port) == 443 else 'jsonrpc'
            )
        self.odoo.login(dbname, username, password)
