from dtintegrations import provider


class Request(object):

    def __init__(self, request, provider_name: str):
        # Set parameter attributes.
        self.request = request
        self.provider: object = None

        # Select a provider class depending on provided name.
        if provider_name.lower() == provider.FLASK:
            self.provider = provider.Flask

        elif provider_name.lower() == provider.GCLOUD:
            self.provider = provider.Gcloud

        elif provider_name.lower() == provider.LAMBDA:
            self.provider = provider.Lambda

        elif provider_name.lower() == provider.AZURE:
            self.provider = provider.Azure

        else:
            raise ValueError(f'Unsupported provider {provider_name}.')

    @property
    def headers(self):
        return self.provider.get_headers_dict(self.request)

    @property
    def body_bytes(self):
        return self.provider.get_body_bytes(self.request)
