import pytest
import disruptive

from dtintegrations import data_connector, provider
from tests.framework import GcloudRequestEmulator
import tests.events as events


class TestHttpPush():

    def test_validate_gcloud(self, http_push_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        http_push_mock.event = test_event

        # Attempt to validate the request.
        event = data_connector.http_push.validate(
            request=GcloudRequestEmulator(test_event),
            provider_name=provider.GCLOUD,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)

        assert event.event_id == test_event.body['event']['eventId']

    def test_validate_gcloud_name_casing(self, http_push_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        http_push_mock.event = test_event

        # Attempt to validate the request.
        data_connector.http_push.validate(
            request=GcloudRequestEmulator(test_event),
            provider_name='GcLouD',
            secret='test-secret',
        )

    def test_validate_gcloud_bad_secret(self):
        r = GcloudRequestEmulator(events.touch)

        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.validate(
                request=r,
                provider_name=provider.GCLOUD,
                secret='bad-secret',
            )

    def test_validate_gcloud_bad_name(self):
        r = GcloudRequestEmulator(events.touch)
        with pytest.raises(ValueError):
            data_connector.http_push.validate(
                request=r,
                provider_name='Xgcloud',
                secret='test-secret',
            )
