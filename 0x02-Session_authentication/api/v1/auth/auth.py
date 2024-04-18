#!/usr/bin/env python3
"""auth module
handles user authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class
    """
    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        """ require_auth method
            Args:
                path: a string argument
                exclude_paths: a list of strings
            Return:
                a boolean
        """
        if path is None or exclude_paths is None or exclude_paths == []:
            return True
        if path in exclude_paths or path + '/' in exclude_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
            Args:
                request: a request object
            Return:
                a string
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
            Args:
                request: a request object
            Return:
                None
        """
        return None
