from dtintegrations import request as dtrequest, provider
import tests.events as events
from tests import framework


class TestRequest():

    def test_flask_provider(self):
        r = dtrequest.Request(
            request=framework.FlaskRequestFormat(events.touch),
            provider_name=provider.FLASK,
        )
        assert r.provider == provider.Flask

    def test_gcloud_provider(self):
        r = dtrequest.Request(
            request=framework.GcloudRequestFormat(events.touch),
            provider_name=provider.GCLOUD,
        )
        assert r.provider == provider.Gcloud

    def test_lambda_provider(self):
        r = dtrequest.Request(
            request=framework.lambda_request_format(events.touch),
            provider_name=provider.LAMBDA,
        )
        assert r.provider == provider.Lambda

    def test_azure_provider(self):
        r = dtrequest.Request(
            request=framework.lambda_request_format(events.touch),
            provider_name=provider.AZURE,
        )
        assert r.provider == provider.Azure
