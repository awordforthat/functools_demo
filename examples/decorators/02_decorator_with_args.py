"""
Exercise 2

This exercise makes use of the pre-written User class. Users have a name and one preference setting: do_not_disturb.
If users have do_not_disturb (DND) set to True, they will be angry if they receive any messages. 

As written, the `send_message` function delivers a message to a user no matter if they have DND turned on or not.
You should:

1. Decorate `send_message` with the `safe_deliver` decorator
2. Fill in `safe_deliver` with logic that only delivers a message if the user has DND set to `False`

If your code is correct, running this script with `python 02_decorator_with_args.py` should complete with
no assertion errors.
"""


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
    """
    Fill in this function such that the original function is only called if the user is available.
    It may be helpful to look at a few examples of how to use *args and **kwargs in the wrapper function
    (for example, https://www.ritchieng.com/python/decorators-kwargs-args/)
    """
    pass


# Decorate this function with `safe_deliver`
def send_message(user, message):
    return user.receive_message(message)


awake_user = User("Awake", do_not_disturb=False)
asleep_user = User("Asleep", do_not_disturb=True)

awake_result = send_message(awake_user, "hey want to get coffee?")
asleep_result = send_message(asleep_user, "hey want to get coffee?")

assert awake_result == "User Awake received message: hey want to get coffee?"
assert asleep_result is None
