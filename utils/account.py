from sqlalchemy.orm import Session
from db.models import User
import random
import string


class AccountService:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    @staticmethod
    def generate_token():
        # Generate a random 25-character long string
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
        return random_string

    def signup(self, email: str, password: str):

        try:
            token = self.generate_token()
            new_user = User(
                email=email,
                password=password,
                token=token
            )
            self.db_session.add(new_user)
            self.db_session.commit()
            self.db_session.refresh(new_user)
            return token
        except Exception as e:
            print(e)
            return False

    def login(self, email: str, password: str):
        try:
            user = self.db_session.query(User).filter_by(email=email).first()
            if user:
                if user.password == password:
                    return user.token
            return False
        except Exception as e:
            return False
