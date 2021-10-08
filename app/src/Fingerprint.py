from ua_parser import user_agent_parser
from werkzeug.utils import cached_property
from flask import request
import requests
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("googleapiclient.discovery").setLevel(logging.WARNING)
logging.getLogger("googleapiclient.discovery_cache").setLevel(logging.ERROR)


class FingerPrint():

    def __init__(self, request):
        self.request = request

    @cached_property
    def _details(self):
        return user_agent_parser.Parse(self.request.user_agent.string)

    @property
    def platform(self):
        return self._details['os']['family']

    @property
    def device(self):
        return self._details['device']

    @property
    def os(self):
        os = self._details['os']
        os['version'] = f"{os['major']}"
        if not os['minor'] == None:
            os['version'] = f"{os['version']}.{os['minor']}"
        if not os['patch'] == None:
            os['version'] = f"{os['version']}.{os['patch']}"
        return os

    @property
    def browser(self):
        browser = self._details['user_agent']
        browser['version'] = f"{browser['major']}"
        if not browser['minor'] == None:
            browser['version'] = f"{browser['version']}.{browser['minor']}"
        if not browser['patch'] == None:
            browser['version'] = f"{browser['version']}.{browser['patch']}"
        return browser

    @property
    def browser_language(self):
        return self.request.accept_languages

    @property
    def do_not_track(self):
        logger.info(self.request.headers.get('DNT'))
        if self.request.headers.get('DNT') == None:
            logger.info("Return False")
            return 0
        else:
            return self.request.headers.get('DNT')

    @property
    def upgrade_insecure_requests(self):
        return self.request.headers.get('Upgrade-Insecure-Requests')

    @property
    def client_ip(self):
        ip = self.request.remote_addr
        # Manage localdev
        if not ip.startswith("172"):
            ip = self.request.headers.get('X-Forwarded-For')
        return ip

    @property
    def browser_version(self):
        return '.'.join(
            part
            for key in ('major', 'minor', 'patch')
            if (part := self._details['user_agent'][key]) is not None
        )

    # https://ip-api.com/docs/api:json
    @property
    def geolocalisation(self):
        return requests.get(f"http://ip-api.com/json/{self.client_ip}").json()
