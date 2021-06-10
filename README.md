# Disruptive Technologies Python Integrations

![build](https://github.com/disruptive-technologies/python-integrations/actions/workflows/build.yml/badge.svg)
[![codecov](https://codecov.io/gh/disruptive-technologies/python-integrations/branch/main/graph/badge.svg?token=KX0W7H6ALS)](https://codecov.io/gh/disruptive-technologies/python-integrations)

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
Currently, the main functionality of this package is for validating event requests forwarded by a [Data Connector](https://developer.disruptive-technologies.com/docs/data-connectors/introduction-to-data-connector).  

The following example shows this for a [Google Cloud Function](https://cloud.google.com/functions).
```python
import os
from dtintegrations import data_connector, provider


def endpoint(request):
    # Use the provider-specific validation function.
    event, labels = data_connector.http_push.validate(
        request,
        provider=provider.GCLOUD,
        secret=os.getenv('DT_SIGNATURE_SECRET'),
    )

    # Print the event data.
    print(event)

    # If all is well, return 200 response.
    return ('OK', 200)
```

## Examples
A few examples has been provided, but must be run either on a serverless platform or locally with a combination or [ngrok](https://developer.disruptive-technologies.com/docs/data-connectors/development-guides/local-development-with-ngrok) and the appropriate development framework.

## Exceptions
If a method is unsuccessful or has been provided with invalid parameters, an exception is raised. A list of available exceptions are available in the [API Reference](https://developer.disruptive-technologies.com/api/libraries/python/errors.html).

## Development
Set up the development virtualenv environment:
```
make
```

Run unit-tests against the currently active python version:
```
make test
```

Lint the package code using MyPy and flake8:
```
make lint
```

Build the package distribution:
```
make build
```
