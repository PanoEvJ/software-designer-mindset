from dataclasses import dataclass
from time import time

# # each social channel has a type
# # and the current number of followers
# SocialChannel = tuple[str, int]

# # each post has a message and the timestamp when it should be posted
# Post = tuple[str, int]


# def post_to_youtube(channel: SocialChannel, message: str) -> None:
#     type, followers = channel
#     print(f"{type} channel: {message}")


# def post_to_facebook(channel: SocialChannel, message: str) -> None:
#     type, followers = channel
#     print(f"{type} channel: {message}")


# def post_to_twitter(channel: SocialChannel, message: str) -> None:
#     type, followers = channel
#     print(f"{type} channel: {message}")


# def post_a_message(channel: SocialChannel, message: str) -> None:
#     type, followers = channel
#     if type == "youtube":
#         post_to_youtube(channel, message)
#     elif type == "facebook":
#         post_to_facebook(channel, message)
#     elif type == "twitter":
#         post_to_twitter(channel, message)


# def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
#     for post in posts:
#         message, timestamp = post
#         for channel in channels:
#             if timestamp <= time():
#                 post_a_message(channel, message)


@dataclass
class SocialChannel:
    ctype: str
    followers: int

    def post_message(self, message: str) -> None:
        print(f"{self.ctype} channel: {message}")


@dataclass
class Posts:
    message: str
    timestamp: int

    def process_schedule(self, channels: list[SocialChannel]) -> None:
        for channel in channels:
            if self.timestamp <= time():
                channel.post_message(self.message)


def main() -> None:
    # posts = [
    # (
    # "Grandma's carrot cake is available again (limited quantities!)!",
    # 1568123400,
    # ),
    # ("Get your carrot cake now, the promotion ends today!", 1568133400),
    # ]
    # channels = [
    # ("youtube", 100),
    # ("facebook", 100),
    # ("twitter", 100),
    # ]
    # process_schedule(posts, channels)

    posts = [
        Posts(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Posts("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        SocialChannel("youtube", 100),
        SocialChannel("facebook", 100),
        SocialChannel("twitter", 100),
    ]
    for post in posts:
        post.process_schedule(channels)


if __name__ == "__main__":
    main()
