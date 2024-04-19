"""自定义异常"""

class UserNotFoundError(Exception):
    """Raised when user not found"""
    def __init__(self, message=None, errors=None):
        # Calling the base class constructor with the parameters it needs
        super().__init__(message)
        # New for this class
        self.errors = errors

def get_user_info(user_obj):
    user = get_user_from_db(user_obj)
    if not user:
        raise UserNotFoundError(f"No user found of this username: {user_obj.username}")
