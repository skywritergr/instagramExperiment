import os
# import json
from flask import Flask, Response, request, jsonify, send_from_directory
from instagram.client import InstagramAPI

app = Flask(__name__, static_url_path='', static_folder='public')
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

access_token = ""

CONFIG = {
    'client_id': 'ad842c2390844f0581e5b178c410741a',
    'client_secret': '9d94784498f5489db11f2281a5248dc6',
    'redirect_uri': 'http://46.101.29.114:7000/post_auth'
}
instagram_client = InstagramAPI(**CONFIG)


@app.route('/handleauth')
def handleauth():
        return send_from_directory('public', 'index.html')


@app.route('/node_modules/<path:filename>')
def serve_node(filename):
    return send_from_directory('node_modules', filename, as_attachment=True)


@app.route('/get_url')
def auth_instagram():
    try:
        url = instagram_client.get_authorize_url(scope=["likes", "comments"])
        return jsonify(url=url)
    except Exception as e:
        print(e)


def get_nav():
    nav_menu = ("<h1>Instagram Actions</h1>"
                "<ul>"
                "<li><a href='/likeHashtags'>Like a Hashtag</a></li>"
                "<li><a href='/getPhotos'>Get Hashtag photos</a></li>"
                "</ul>")
    return nav_menu


@app.route('/post_auth')
def on_success():
    code = request.args.get("code")
    if not code:
        return "Missing code"
    try:
        access_token, user_info = instagram_client.exchange_code_for_access_token(code)
        print(access_token)
        if not access_token:
            return "could not get access token"
        access_token = access_token
        return jsonify(access_token=access_token, user_info=user_info)
    except Exception as e:
        print(e)
        return jsonify(error=True)


@app.route('/api/hashtag', methods=['GET'])
def get_hashtags():
    return Response('Hello World!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 7000)))
