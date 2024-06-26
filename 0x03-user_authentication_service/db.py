#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add a new user to the database
        Args:
            email (str): User's email address
            hashed_password (str): Hashed password for the user

        Return:
            User: User object that was added to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ Finds the first user whose token matches the keyword

        Args:
            keyword (string): keyword being searched

        Returns:
            First row of User found
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound("No user found")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update user

        Args:
            user_id (int): the user to update
            kwargs : user data

        Returns:
            User.
        """
        user = self.find_user_by(id=user_id)
        for attr, value in kwargs.items():
            if hasattr(user, attr):
                setattr(user, attr, value)
            else:
                raise ValueError(f"Invalid attribe '{attr}'")
        self._session.commit()
