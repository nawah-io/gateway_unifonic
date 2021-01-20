# Ancora Imparo.

from nawah.classes import PACKAGE_CONFIG, ATTR
from nawah.registry import Registry

from typing import TypedDict
from otsdc.rest.client import OTSRestClient
from otsdc.url.http_url import HttpOTSUrl


def unifonic_gateway(
	phone: str,
	content: str,
	unifonic_auth: TypedDict('GATEWAY_UNIFONIC_AUTH', sid=str) = None,
):
	if not unifonic_auth:
		unifonic_auth = Registry.var('unifonic')

	client = OTSRestClient(appSid=unifonic_auth['sid'])
	msg = client.messageResource
	msg.send(phone, content)


config = PACKAGE_CONFIG(
	api_level='1.1',
	version='1.1.0b1',
	gateways={'unifonic': unifonic_gateway},
	vars_types={'unifonic': ATTR.TYPED_DICT(dict={'sid': ATTR.STR()})},
)