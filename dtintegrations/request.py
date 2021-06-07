from __future__ import annotations

from typing import Any

from dtintegrations import provider


class Request(object):

    def __init__(self, request: Any, provider_name: str):
        # Set parameter attributes.
        self.request = request
        self.provider: Any = None

        # Select a provider class depending on provided name.
        if provider_name.lower() == provider.FLASK:
            self.provider = provider.Flask

        elif provider_name.lower() == provider.DJANGO:
            self.provider = provider.Django

        elif provider_name.lower() == provider.GCLOUD:
            self.provider = provider.Gcloud

        elif provider_name.lower() == provider.LAMBDA:
            self.provider = provider.Lambda

        elif provider_name.lower() == provider.AZURE:
            self.provider = provider.Azure

        else:
            msg = f'Unsupported provider {provider_name}.'
            raise ValueError(msg)

    @property
    def headers(self) -> dict:
        headers: dict = self.provider.get_headers_dict(self.request)
        return headers

    @property
    def body_bytes(self) -> bytes:
        data: bytes = self.provider.get_body_bytes(self.request)
        return data
