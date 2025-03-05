from models.user import User


# TODO: 認証認可実装
def verify_jwt(token: str) -> str:
    return 'line_user_id_test'


def get_current_user(token: str = "hoge") -> User:
    line_user_id = verify_jwt(token)
    return User(
        id=1,
        line_user_id=line_user_id,
        email="hoge@example.com",
        tel=0000000000
    )
