import dtintegrations
from tests import events


class TestMetadata():

    def test_metadata_dunder(self):
        # Construct a metadata input.
        test_dict = events.metadata

        # Construct the Metadata object from dict input.
        m = dtintegrations.data_connector.metadata.DeviceMetadata(test_dict)

        print(m)

    def test_metadata_dunder_eval(self):
        # Construct a metadata input.
        test_dict = events.metadata

        # Construct the Metadata object from dict input.
        m = dtintegrations.data_connector.metadata.DeviceMetadata(test_dict)

        eval(repr(m))
