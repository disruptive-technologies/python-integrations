import jwt
import ast
import hashlib
import disruptive  # type: ignore

from dtintegrations import request as dtrequest


def validate_generic(headers: dict, body: bytes, secret: str):
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
    return disruptive.events.Event(body_dict['event'])


def validate(request, provider_name: str, secret: str):
    # Create a Request instance of the provider used for MISO.
    r = dtrequest.Request(request, provider_name)

    # Use a more generic function for the validation process.
    return validate_generic(r.headers, r.body_bytes, secret)
