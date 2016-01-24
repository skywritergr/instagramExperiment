from server.instagram_user import instagram_user

class instagram_photo(object):
    id = ""
    likes = 0
    thumbnail = ""
    link = ""
    created_time = ""
    
    def __init__(self, picture_info):
        self.id = picture_info['id']
        self.likes = picture_info['likes']['count']
        self.thumbnail = picture_info['thumbnail']['url']
        self.link = picture_info['link']
        self.created_time = picture_info['created_time']
        self.user = instagram_user(picture_info['user'])