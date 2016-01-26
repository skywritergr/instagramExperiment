import os
from flask import Flask, request, jsonify, send_from_directory, redirect
from instagram.client import InstagramAPI
from server.instagram_user import instagram_user
from server.instagram_photo import instagram_photo

app = Flask(__name__, static_url_path='', static_folder='public')
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))


CONFIG = {
    'client_id': 'ad842c2390844f0581e5b178c410741a',
    'client_secret': '9d94784498f5489db11f2281a5248dc6',
    'redirect_uri': 'http://46.101.29.114:7000/post_auth'
}
instagram_client = InstagramAPI(**CONFIG)
user = None
token = None


@app.route('/handleauth')
def handleauth():
        return send_from_directory('public', 'index.html')


@app.route('/node_modules/<path:filename>')
def serve_node(filename):
    return send_from_directory('node_modules', filename, as_attachment=True)


@app.route('/get_url')
def auth_instagram():
    try:
        url = instagram_client.get_authorize_url(scope=["likes", "comments", "public_content"])
        return jsonify(url=url)
    except Exception as e:
        print(e)


@app.route('/post_auth')
def on_success():
    code = request.args.get("code")
    if not code:
        return "Missing code"
    try:
        access_token, user_info =\
            instagram_client.exchange_code_for_access_token(code)
        if not access_token:
            return "could not get access token"
        global token
        token = access_token
        global user
        user = instagram_user(user_info)
        return redirect("http://46.101.29.114:7000/handleauth", code=302)
    except Exception as e:
        print(e)
        return jsonify(error=True)


def get_latest_photos(hashtag, num):
    api = InstagramAPI(access_token=token, client_secret=CONFIG['client_secret'])
    result, next_tag = api.tag_search(q=hashtag)
    tag_recent_media, next = api.tag_recent_media(count=num, tag_name=(tag_search[0].name if len(tag_search)>0 else hashtag))
    photos = []
    for tag_media in tag_recent_media:
        instaphoto = instagram_photo(tag_media)
        photos.append(instaphoto)
    return photos


@app.route('/api/likephotos', methods=['GET'])
def like_photos():
    # number = request.args.get("number")
    hashtag = request.args.get("tag")
    api = InstagramAPI(access_token=token, client_secret=CONFIG['client_secret'])
    number = 15 #static number in the beggining. Later get it from the url
    photos = get_latest_photos(hashtag, number)
    for photo in photos:
        api.like_media(photo['id'])
        
    return jsonify(success=True, liked=number)


@app.route('/api/leavecomments', methods=['POST'])
def comment_to_photos():
    content = request.get_json()
    comment = content['comment']
    hashtag = content['tag']
    number = 5 #content['number']
    api = InstagramAPI(access_token=token, client_secret=CONFIG['client_secret'])
    photos = get_latest_photos(hashtag, number)
    for photo in photos:
        api.create_media_comment(photo['id'], comment)
    return jsonify(success=True, commented=number)
    
    
@app.route('/api/followusers', methods=['GET'])
def follow_users():
    hashtag = request.args.get("tag")
    api = InstagramAPI(access_token=token, client_secret=CONFIG['client_secret'])
    number = 5 #static number in the beggining. Later get it from the url
    photos = get_latest_photos(hashtag, number)
    followed = 0
    for photo in photos:
        api.follow_user(photo['user']['instagram_id'])
        # check if the user is being followed already
        # if not then follow and increment the counter
        followed += 1
    return jsonify(success=True, followed=followed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 7000)))
