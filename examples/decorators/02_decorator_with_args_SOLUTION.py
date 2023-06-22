class User:
    def __init__(self, name, do_not_disturb):
        self.name = name
        self.do_not_disturb = do_not_disturb
        self.saved_messages = []

    def receive_message(self, message):
        if self.do_not_disturb:
            return "HEY! You woke me up!"
        return f"User {self.name} received message: {message}"


def safe_deliver(func):
    def wrapper(*args, **kwargs):
        if not args[0].do_not_disturb:
            return func(*args, **kwargs)

    return wrapper


@safe_deliver
def send_message(user, message):
    return user.receive_message(message)


awake_user = User("Awake", do_not_disturb=False)
asleep_user = User("Asleep", do_not_disturb=True)

awake_result = send_message(awake_user, "hey want to get coffee?")
asleep_result = send_message(asleep_user, "hey want to get coffee?")

assert awake_result == "User Awake received message: hey want to get coffee?"
assert asleep_result is None
