#!/usr/bin/env python3
""" Module: session_auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a user_id

        Args:
            user_id (str): the user id
        Returns:
            str: The generated session id if successful otherwise none
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID.

        Args:
            session_id (str): The Session ID.

        Returns:
            str: The User ID associated with the Session ID if found,
            otherwise None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        else:
            return self.user_id_by_session_id.get(session_id)
