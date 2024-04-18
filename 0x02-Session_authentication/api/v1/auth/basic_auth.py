#!/usr/bin/env python3
"""module: basic_auth
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


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
    
    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        user object from credentials
        Args:
            user_email: a string argument
            user_pwd: a string argument
        Return:
            user object
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            return User(email=user_email, password=user_pwd)
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user
        Overloads Auth and retrieves the User instance for a request
        Args:
            request: a request object
        Return:
            a User instance
        """
        auth_header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(auth_header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(user_email, user_pwd)
