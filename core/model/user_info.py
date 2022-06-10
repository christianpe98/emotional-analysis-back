class UserInfo:
    username = ""
    name = ""
    profile_image_url = ""
    description = ""

    def __init__(self, data):
        self.name = data.name
        self.username = data.username
        self.profile_image_url = data.profile_image_url.replace("_normal", "")
        self.description = data.description
