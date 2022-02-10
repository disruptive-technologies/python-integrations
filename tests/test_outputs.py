import dtintegrations
import tests.events as events

from tests import framework


class TestOutputs():

    def test_HttpPush_dunder(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        payload = dtintegrations.data_connector.HttpPush.from_provider(
            request=framework.FlaskRequestFormat(test_event),
            provider=dtintegrations.provider.FLASK,
            secret='test-secret',
        )

        print(payload)

    def test_HttpPush_dunder_eval(self, decode_mock):
        # Choose an event to receive.
        test_event = events.touch

        # Update the mock event attribute.
        decode_mock.event = test_event

        # Attempt to decode the request.
        payload = dtintegrations.data_connector.HttpPush.from_provider(
            request=framework.FlaskRequestFormat(test_event),
            provider=dtintegrations.provider.FLASK,
            secret='test-secret',
        )

        eval(repr(payload))
