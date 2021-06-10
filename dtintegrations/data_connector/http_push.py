import jwt
import ast
import hashlib
from typing import Any

import disruptive  # type: ignore

from dtintegrations import request as dtrequest


def decode(headers: dict, body: bytes, secret: str) -> Any:
    """
    Decodes the incoming event, first validating the source- and origin
    using a signature secret and the request header- and body.

    Parameters
    ----------
    headers : dict[str, str]
        Headers key- value pairs in request. For multi-header
        format, the value should be a comma-separated string.
    body : bytes
        Request body bytes.
    secret : str
        The secret to sign the request at source.

    Returns
    -------
    event : Event
        An object representing the received event.
    labels : dict
        Labels from the source device forwarded by the Data Connector.

    """

    # Do some mild secret sanitization, ensuring populated string.
    if isinstance(secret, str):
        if len(secret) == 0:
            raise disruptive.errors.EmptyStringError(
                'Secret is empty string.'
            )
    else:
        raise TypeError(
            f'Got secret of type <{type(secret).__name__}>. Expected <str>.'
        )

    # Isolate the token in request headers.
    token = None
    for key in headers:
        if key.lower() == 'x-dt-signature':
            token = headers[key]
            break
    if token is None:
        raise disruptive.errors.ConfigurationError(
            'Missing header X-Dt-Signature.'
        )

    # Decode the token using the signature secret.
    try:
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256'],
        )
    except jwt.exceptions.InvalidSignatureError:
        raise disruptive.errors.ConfigurationError(
            'Invalid secret.'
        )
    except jwt.exceptions.ExpiredSignatureError:
        raise disruptive.errors.ConfigurationError(
            'Signature has expired.'
        )

    # Calculate the body checksum.
    m = hashlib.sha1()
    m.update(body)
    checksum = m.digest().hex()

    # Compare body checksum with the one in payload.
    if payload['checksum'] != checksum:
        raise disruptive.errors.ConfigurationError(
            'Checksum mismatch.'
        )

    # Convert the body bytes string into a dictionary.
    body_dict = ast.literal_eval(body.decode('utf-8'))

    # Initialize and return an Event instance of the body.
    return disruptive.events.Event(body_dict['event']), body_dict['labels']


def decode_request(request: Any, provider: str, secret: str) -> Any:
    """
    Decodes the incoming event, first validating the source- and origin
    using a signature secret and the provider-specific request.

    Parameters
    ----------
    request : Any
        Unmodified incoming request format of the spcified provider.
    provider : {"flask", "gcloud", "lambda", "azure"}, str
        Name of the :ref:`provider <integrations_provider>`
        used to receive the request.
    secret : str
        The secret to sign the request at source.

    Returns
    -------
    event : Event
        An object representing the received event.
    labels : dict
        Labels from the source device forwarded by the Data Connector.

    """

    # Create a Request instance of the provider used for MISO.
    r = dtrequest.Request(request, provider)

    # Use a more generic function for the validation process.
    return decode(r.headers, r.body_bytes, secret)
