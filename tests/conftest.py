# Third-part imports.
import pytest

# Project imports.
from tests.framework import DecodeMock


@pytest.fixture()
def decode_mock(mocker):
    return DecodeMock(mocker)
