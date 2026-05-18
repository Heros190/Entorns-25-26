class UserDao:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_user_by_username_or_email(self, username_or_email):
        return self.db_session.query(User).filter(
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()

    def validate_user(self, username_or_email, password):
        user = self.get_user_by_username_or_email(username_or_email)
        if user and user.password == password:  # In a real application, use hashed passwords
            return user
        return None

    def get_user_by_id(self, user_id):
        return self.db_session.query(User).filter(User.id == user_id).first()