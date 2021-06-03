import pytest
import disruptive

from dtintegrations import data_connector, provider
from tests.framework import GcloudRequestMock
import tests.events as events


class TestHttpPush():

    def test_validate_gcloud(self):
        test_event = events.touch
        request = GcloudRequestMock(test_event)
        event = data_connector.http_push.validate(
            request=request,
            provider_name=provider.GCLOUD,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)

        assert event.event_id == test_event.body['event']['eventId']

    def test_validate_gcloud_bad_secret(self):
        r = GcloudRequestMock(events.touch)

        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.validate(
                request=r,
                provider_name=provider.GCLOUD,
                secret='bad-secret',
            )

    def test_validate_gcloud_name_casing(self):
        r = GcloudRequestMock(events.touch)
        data_connector.http_push.validate(
            request=r,
            provider_name='GcLouD',
            secret='test-secret',
        )

    def test_validate_gcloud_bad_name(self):
        r = GcloudRequestMock(events.touch)
        with pytest.raises(ValueError):
            data_connector.http_push.validate(
                request=r,
                provider_name='Xgcloud',
                secret='test-secret',
            )
