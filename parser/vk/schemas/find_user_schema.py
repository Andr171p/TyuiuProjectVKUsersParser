

class VkUserSchema:
    user_id: int | None = None
    name: str | None = None
    surname: str | None = None
    age: int | None = None
    city: str | None = None
    posts: dict | None = None
    groups: dict | None = None
    subscriptions: dict | None = None

    @classmethod
    def add(
            cls, user_id: int, name: str, surname: str, age: int, city: str, posts: dict, groups: dict, subscriptions: dict
    ) -> None:
        cls.user_id = user_id
        cls.name = name
        cls.surname = surname
        cls.age = age
        cls.city = city
        cls.posts = posts
        cls.groups = groups
        cls.subscriptions = subscriptions

    @classmethod
    def clear(cls) -> None:
        cls.user_id = None
        cls.name = None
        cls.surname = None
        cls.age = None
        cls.city = None
        cls.posts = None
        cls.groups = None
        cls.subscriptions = None

    def __str__(self) -> str:
        user = (f"User(\n"
                     f"user_id={self.user_id!r}"
                     f"name={self.name!r}\n"
                     f"surname={self.surname!r}\n"
                     f"age={self.age!r}\n"
                     f"city={self.city!r}\n"
                     f"posts={self.posts!r}\n"
                     f"groups={self.groups!r}\n"
                     f"subscriptions={self.subscriptions!r}\n"
                     f")")
        return user
