#!/usr/bin/env python3
""" Auth module
"""
import bcrypt


def _hash_password(password: str) -> str:
    """ create password hash
    """
    password = password
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    hash_password = bcrypt.hashpw(password_bytes, salt)

    return hash_password
