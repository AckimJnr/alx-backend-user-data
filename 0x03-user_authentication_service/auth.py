#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user

        Args:
            email: email
            password: password
        Returns:
            created user
        """
        try:
            if self._db.find_user_by(email=email):
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hash_password = _hash_password(password)
            user = self._db.add_user(email, hash_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ validate login

        Args:
            email: email
            password: password
        Returns:
            True if login is valid, False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False


def _generate_uuid() -> str:
    """ generate uuid

    Returns:
        A string representation of the generated UUID.
    """
    return str(uuid.uuid4())


def _hash_password(password: str) -> str:
    """ create password hash
    """
    password = password
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    hash_password = bcrypt.hashpw(password_bytes, salt)

    return hash_password
