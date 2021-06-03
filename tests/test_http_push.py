import pytest
import disruptive

from dtintegrations import data_connector, provider
import tests.events as events
from tests import framework


class TestHttpPush():

    # ------------------------- Flask -------------------------
    def test_validate_flask(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        event = data_connector.http_push.validate(
            request=framework.FlaskRequestFormat(test_event),
            provider_name=provider.FLASK,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_validate_flask_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        data_connector.http_push.validate(
            request=framework.FlaskRequestFormat(test_event),
            provider_name='fLAsk',
            secret='test-secret',
        )

    def test_validate_flask_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.validate(
                request=framework.FlaskRequestFormat(events.touch),
                provider_name=provider.FLASK,
                secret='bad-secret',
            )

    def test_validate_flask_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.validate(
                request=framework.FlaskRequestFormat(events.touch),
                provider_name='Xflask',
                secret='test-secret',
            )

    # ------------------------- Gcloud -------------------------
    def test_validate_gcloud(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        event = data_connector.http_push.validate(
            request=framework.GcloudRequestFormat(test_event),
            provider_name=provider.GCLOUD,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_validate_gcloud_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        data_connector.http_push.validate(
            request=framework.GcloudRequestFormat(test_event),
            provider_name='GcLouD',
            secret='test-secret',
        )

    def test_validate_gcloud_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.validate(
                request=framework.GcloudRequestFormat(events.touch),
                provider_name=provider.GCLOUD,
                secret='bad-secret',
            )

    def test_validate_gcloud_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.validate(
                request=framework.GcloudRequestFormat(events.touch),
                provider_name='Xgcloud',
                secret='test-secret',
            )

    # ------------------------- Lambda -------------------------
    def test_validate_lambda(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        event = data_connector.http_push.validate(
            request=framework.lambda_request_format(test_event),
            provider_name=provider.LAMBDA,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_validate_lambda_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        data_connector.http_push.validate(
            request=framework.lambda_request_format(test_event),
            provider_name='lAMbdA',
            secret='test-secret',
        )

    def test_validate_lambda_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.validate(
                request=framework.lambda_request_format(events.touch),
                provider_name=provider.LAMBDA,
                secret='bad-secret',
            )

    def test_validate_lambda_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.validate(
                request=framework.lambda_request_format(events.touch),
                provider_name='Xlambda',
                secret='test-secret',
            )

    # ------------------------- Azure -------------------------
    def test_validate_azure(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        event = data_connector.http_push.validate(
            request=framework.AzureRequestFormat(test_event),
            provider_name=provider.AZURE,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_validate_azure_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to validate the request.
        data_connector.http_push.validate(
            request=framework.AzureRequestFormat(test_event),
            provider_name='AzuRE',
            secret='test-secret',
        )

    def test_validate_azure_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.validate(
                request=framework.AzureRequestFormat(events.touch),
                provider_name=provider.AZURE,
                secret='bad-secret',
            )

    def test_validate_azure_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.validate(
                request=framework.AzureRequestFormat(events.touch),
                provider_name='Xazure',
                secret='test-secret',
            )
