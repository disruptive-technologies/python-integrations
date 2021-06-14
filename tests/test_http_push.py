import pytest
import disruptive  # type: ignore

from dtintegrations import data_connector, provider
import tests.events as events
from tests import framework


class TestHttpPush():

    def test_decode_secret_empty_string(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode(
                headers={},
                body=b'',
                secret='',
            )

    def test_decode_secret_invalid_type(self):
        with pytest.raises(TypeError):
            data_connector.http_push.decode(
                headers={},
                body=b'',
                secret=22,
            )

    def test_decode_missing_header_token(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode(
                headers={},
                body=b'',
                secret='test-secret',
            )

    def test_decode_expired_signature(self):
        test_event = events.touch
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode(
                headers=test_event.headers,
                body=test_event.body_str.encode('utf-8'),
                secret='test-secret',
            )

    def test_decode_checksum_mismatch(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Corrupt the body string.
        body_str = test_event.body_str + 'abc'

        # Attempt to decode the request.
        with pytest.raises(disruptive.errors.ConfigurationError):
            event, _ = data_connector.http_push.decode(
                headers=test_event.headers,
                body=body_str.encode('utf-8'),
                secret='test-secret',
            )

    # ------------------------- Flask -------------------------
    def test_decode_flask(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        event, _ = data_connector.http_push.decode_request(
            request=framework.FlaskRequestFormat(test_event),
            provider=provider.FLASK,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_decode_flask_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        data_connector.http_push.decode_request(
            request=framework.FlaskRequestFormat(test_event),
            provider='fLAsk',
            secret='test-secret',
        )

    def test_decode_flask_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode_request(
                request=framework.FlaskRequestFormat(events.touch),
                provider=provider.FLASK,
                secret='bad-secret',
            )

    def test_decode_flask_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.decode_request(
                request=framework.FlaskRequestFormat(events.touch),
                provider='Xflask',
                secret='test-secret',
            )

    # ------------------------- Django -------------------------
    def test_decode_django(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        event, _ = data_connector.http_push.decode_request(
            request=framework.DjangoRequestFormat(test_event),
            provider=provider.DJANGO,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_decode_django_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        data_connector.http_push.decode_request(
            request=framework.DjangoRequestFormat(test_event),
            provider='djANgO',
            secret='test-secret',
        )

    def test_decode_django_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode_request(
                request=framework.DjangoRequestFormat(events.touch),
                provider=provider.DJANGO,
                secret='bad-secret',
            )

    def test_decode_django_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.decode_request(
                request=framework.DjangoRequestFormat(events.touch),
                provider='Xdjango',
                secret='test-secret',
            )

    # ------------------------- Gcloud -------------------------
    def test_decode_gcloud(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        event, _ = data_connector.http_push.decode_request(
            request=framework.GcloudRequestFormat(test_event),
            provider=provider.GCLOUD,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_decode_gcloud_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        data_connector.http_push.decode_request(
            request=framework.GcloudRequestFormat(test_event),
            provider='GcLouD',
            secret='test-secret',
        )

    def test_decode_gcloud_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode_request(
                request=framework.GcloudRequestFormat(events.touch),
                provider=provider.GCLOUD,
                secret='bad-secret',
            )

    def test_decode_gcloud_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.decode_request(
                request=framework.GcloudRequestFormat(events.touch),
                provider='Xgcloud',
                secret='test-secret',
            )

    # ------------------------- Lambda -------------------------
    def test_decode_lambda(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        event, _ = data_connector.http_push.decode_request(
            request=framework.lambda_request_format(test_event),
            provider=provider.LAMBDA,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_decode_lambda_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        data_connector.http_push.decode_request(
            request=framework.lambda_request_format(test_event),
            provider='lAMbdA',
            secret='test-secret',
        )

    def test_decode_lambda_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode_request(
                request=framework.lambda_request_format(events.touch),
                provider=provider.LAMBDA,
                secret='bad-secret',
            )

    def test_decode_lambda_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.decode_request(
                request=framework.lambda_request_format(events.touch),
                provider='Xlambda',
                secret='test-secret',
            )

    # ------------------------- Azure -------------------------
    def test_decode_azure(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        event, _ = data_connector.http_push.decode_request(
            request=framework.AzureRequestFormat(test_event),
            provider=provider.AZURE,
            secret='test-secret',
        )

        assert isinstance(event, disruptive.events.Event)
        assert event.event_id == test_event.body['event']['eventId']

    def test_decode_azure_name_casing(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        data_connector.http_push.decode_request(
            request=framework.AzureRequestFormat(test_event),
            provider='AzuRE',
            secret='test-secret',
        )

    def test_decode_azure_bad_secret(self):
        with pytest.raises(disruptive.errors.ConfigurationError):
            data_connector.http_push.decode_request(
                request=framework.AzureRequestFormat(events.touch),
                provider=provider.AZURE,
                secret='bad-secret',
            )

    def test_decode_azure_bad_name(self):
        with pytest.raises(ValueError):
            data_connector.http_push.decode_request(
                request=framework.AzureRequestFormat(events.touch),
                provider='Xazure',
                secret='test-secret',
            )
