#!/usr/bin/env python3
"""module: basic_auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Implements basic authentication
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extract base64 authorization header
        """
        if authorization_header is None or not isinstance(
                                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        decode base64 authorization header
        Args:
            base64_authorization_header: a string argument
        Return:
            a string
        """
        if base64_authorization_header is None or not isinstance(
                                base64_authorization_header, str):
            return None
        try:
            return base64_authorization_header.encode('utf-8').decode(
                'base64')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        extract user credentials
        Args:
            decoded_base64_authorization_header: a string argument
        Return:
            a tuple
        """
        if decoded_base64_authorization_header is None or not isinstance(
                                decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))
