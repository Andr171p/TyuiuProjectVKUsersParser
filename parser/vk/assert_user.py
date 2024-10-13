from parser.vk.schemas.primary_user_schema import VkPrimaryUserSchema


class VkAssertUser:
    def __init__(self, input_user: VkPrimaryUserSchema, output_user: dict) -> None:
        self.input_user = input_user
        self.output_user = output_user

    def assert_user(self) -> bool:
        ...