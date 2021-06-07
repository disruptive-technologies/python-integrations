from __future__ import annotations

from typing import Any


FLASK = 'flask'
DJANGO = 'django'
GCLOUD = 'gcloud'
LAMBDA = 'lambda'
AZURE = 'azure'
PROVIDERS = [
    FLASK,
    DJANGO,
    GCLOUD,
    LAMBDA,
    AZURE,
]


class Flask():

    name: str = FLASK

    @staticmethod
    def get_headers_dict(request: Any) -> dict:
        # Flask uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in request.headers:
            header_dict[key] = value
        return header_dict

    @staticmethod
    def get_body_bytes(request: Any) -> bytes:
        # Flask has an attribute for body bytes.
        data: bytes = request.data
        return data


class Django():

    name: str = DJANGO

    @staticmethod
    def get_headers_dict(request: Any) -> dict:
        # Django headers can simply be returned.
        headers: dict = request.headers
        return headers

    @staticmethod
    def get_body_bytes(request: Any) -> bytes:
        # Django has an attribute for body bytes.
        data: bytes = request.body
        return data


class Gcloud():

    name: str = GCLOUD

    @staticmethod
    def get_headers_dict(request: Any) -> dict:
        # gcloud uses some custom header type. Convert to dict.
        header_dict: dict = dict()
        for key, value in request.headers:
            header_dict[key] = value
        return header_dict

    @staticmethod
    def get_body_bytes(request: Any) -> bytes:
        # gcloud has a convenience function for getting body bytes.
        data: bytes = request.get_data()
        return data


class Lambda():

    name: str = LAMBDA

    @staticmethod
    def get_headers_dict(request: Any) -> dict:
        # Lambda headers can simply be returned.
        headers: dict = request['headers']
        return headers

    @staticmethod
    def get_body_bytes(request: Any) -> bytes:
        # Lambda body is a string, to it must be encoded.
        data: bytes = request['body'].encode('utf-8')
        return data


class Azure():

    name: str = AZURE

    @staticmethod
    def get_headers_dict(request: Any) -> dict:
        # Azure headers can simply be returned.
        headers: dict = request.headers
        return headers

    @staticmethod
    def get_body_bytes(request: Any) -> bytes:
        # Azure has a convenience function for getting body bytes.
        data: bytes = request.get_body()
        return data
