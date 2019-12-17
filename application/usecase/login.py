from adapters.gateway.user.post_user import post_user


def login(user_id):
    post_user(user_id)
