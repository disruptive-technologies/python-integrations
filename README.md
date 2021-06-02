# Disruptive Technologies Python Integrations

![build](https://github.com/disruptive-technologies/python-integrations/actions/workflows/build.yml/badge.svg)

## Installation

The package can be installed through pip:

```sh
pip install --upgrade dtintegrations
```

or from source:

```sh
pip install .
```

### Requirements

- Python 3.7+

## Usage

```python
import os
from dtintegrations import data_connector, provider


def endpoint(request):
    # Use the provider-specific validation function.
    event = data_connector.http_push.validate(
        request,
        provider=provider.GCLOUD,
        secret=os.getenv('DT_SIGNATURE_SECRET'),
    )

    # Print the event data.
    print(event)

    # If all is well, return 200 response.
    return ('OK', 200)
```
