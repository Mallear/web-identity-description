from ua_parser import user_agent_parser
from werkzeug.utils import cached_property
from flask import request
import requests


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
        os['version'] = f"{os['major']}.{os['minor']}"
        if not os['patch'] == None:
            os['version'] = f"{os['version']}.{os['patch']}"
        return os

    @property
    def browser(self):
        return self._details['user_agent']

    @property
    def browser_language(self):
        return self.request.accept_languages

    @property
    def do_not_track(self):
        return self.request.headers.get('DNT')

    @property
    def upgrade_insecure_requests(self):
        return self.request.headers.get('Upgrade-Insecure-Requests')

    @property
    def client_ip(self):
        return self.request.remote_addr

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
