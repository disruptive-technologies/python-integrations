import jwt
import ast
import hashlib
from typing import Any, Optional

import disruptive  # type: ignore

from dtintegrations import request as dtrequest, outputs
from dtintegrations.data_connector import metadata as metadata


class HttpPush(outputs.OutputBase):
    """
    Represents the HTTP Push Data Connector at the receiver side.

    Attributes
    ----------
    event : Event
        An object representing the received event.
    labels : dict
        Labels from the source device forwarded by the Data Connector.

    """
    def __init__(self, headers: dict, body: bytes, secret: str):
        """
        Constructs the HtttpPush object given request contents.

        """

        self._body_dict = self._decode(headers, body, secret)
        super().__init__(self._body_dict)

        self.event = disruptive.events.Event(self._body_dict['event'])
        self.labels = self._body_dict['labels']
        self._metadata_dict = self._body_dict['metadata']

    def get_device_metadata(self) -> Optional[metadata.DeviceMetadata]:
        """
        Fetch source device metadata if it exists.

        Returns
        -------
        metadata : DeviceMetadata, optional
            An object representing the source device metadata.
            If the event forwarded by the Data Connector does not originate
            a device, DeviceMetadata returns None.
        """

        try:
            return metadata.DeviceMetadata(self._metadata_dict)
        except KeyError:
            return None

    def _decode(self, headers: dict, body: bytes, secret: str) -> dict:
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
        payload : HttpPush
            An object representing received HTTP Push Data Connector payload.

        Raises
        ------
        ConfigurationError
            If any of the input parameters are of invalid type, or
            the signature secret is expired.

        """

        # Do some mild secret sanitization, ensuring populated string.
        if isinstance(secret, str):
            if len(secret) == 0:
                raise disruptive.errors.ConfigurationError(
                    'Secret is empty string.'
                )
        else:
            raise TypeError(
                f'Got secret type <{type(secret).__name__}>. Expected <str>.'
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

        return dict(body_dict)

    @staticmethod
    def from_provider(request: Any, provider: str, secret: str) -> Any:
        """
        Decodes the incoming event using a specified provider, first validating
        the the source- and origin using a signature secretand
        and the provider-specific request.

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
        payload : HttpPush
            An object representing received HTTP Push Data Connector payload.

        Raises
        ------
        ConfigurationError
            If any of the input parameters are of invalid type, or
            the signature secret is expired.

        """

        # Create a Request instance of the provider used for MISO.
        r = dtrequest.Request(request, provider)

        # Use a more generic function for the validation process.
        return HttpPush(r.headers, r.body_bytes, secret)
