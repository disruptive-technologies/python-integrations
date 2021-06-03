# Third-part imports.
import pytest

# Project imports.
from tests.framework import HttpPushMock


@pytest.fixture()
def http_push_mock(mocker):
    return HttpPushMock(mocker)
