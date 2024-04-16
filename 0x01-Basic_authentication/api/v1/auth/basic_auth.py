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
