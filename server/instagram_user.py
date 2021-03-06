class instagram_user(object):
    full_name = ""
    instagram_id = "0"
    profile_picture = ""
    username = ""

    def __init__(self, user_info):
        try:
            self.full_name = user_info.full_name
            self.instagram_id = user_info.id
            self.profile_picture = user_info.profile_picture
            self.username = user_info.username
        except AttributeError:
            self.full_name = user_info['full_name']
            self.instagram_id = user_info['id']
            self.profile_picture = user_info['profile_picture']
            self.username = user_info['username']
