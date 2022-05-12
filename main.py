from cgi import test
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()


videos = {
}


class Video(Resource):
    def get(self,video_id):
        return videos[video_id]

    def put(self,video_id):
        return {}

api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)