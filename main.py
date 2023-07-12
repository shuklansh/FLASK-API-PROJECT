from flask import Flask,request
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func


app = Flask(__name__)
api = Api(app) #initialises the fact that we are using a restful api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) # db storage

class VideModel(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(100), nullable = False) # 100 is max characters allowed
    likes = db.Column(db.Integer, nullable = False)
    views = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(name = {VideModel.name}, views = {VideModel.views}, likes = {VideModel.likes})"#.format(name = name,views=views,likes=likes)


#db.create_all() # do this only once



# names = {"bill":{"age":70,"gender":"male"},
#     "tim":{"age":20,"gender":"male"}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type = str, help = "Name of video is required",required = True) #duplicate line with alt+shift+down/up
video_put_args.add_argument("likes",type = int, help = "Likes on video is required",required = True)
video_put_args.add_argument("views",type = int, help = "Views on video is required",required = True)

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer,
}

# videos = {} # memory storage 

# def abort_req_if_vid_id_nonexistent(video_id ):
#     if video_id not in videos:
#         abort(404, message = "video with id {vid} not stored".format(vid = video_id)) # 404 -> not found

# def abort_put_if_vid_id_exists(video_id ):
#     if video_id in videos:
#         abort(409, message = "video with id {vid} already stored".format(vid = video_id)) # 409-> conflict

class allvideolist(Resource):
    @marshal_with(resource_fields)
    def get(self):
       
        rows = VideModel.query.count()
        list =[]
        for i in range(0,rows):
            res = VideModel.query.filter_by(id=i).first()
            list.append(res)
        return list
      
            
            

         

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404,message = "could not find video with that id")

        return result
        # abort_req_if_vid_id_nonexistent(video_id)
        # return videos[video_id]        

    @marshal_with(resource_fields)
    def post(self,video_id):
        # print(request.form['likes'])
        # print(request.form)
        # abort_put_if_vid_id_exists(video_id=video_id)
        args = video_put_args.parse_args()
        result = VideModel.query.filter_by(id = video_id).first()
        if result:
            abort(409,message = "video id taken")
        # videos[video_id] = args #video_id will be key in the dict
        video = VideModel(id = video_id, name = args['name'], likes = args['likes'],views = args['views'])
        db.session.add(video)
        db.session.commit()
        return video,201
        # return videos[video_id],201 # 201 -> created successfully (200 -> OK is default)
        # return {video_id:args}
        # return {"Your video {name} has {likes} likes and {views} views.".format(name = video["name"],likes=video['likes'],views = video['views'])}
        # return {"data":"you have {likes} likes".format(likes=request.form["likes"])}
    @marshal_with(resource_fields)
    def delete(self,video_id):
        # abort_req_if_vid_id_nonexistent(video_id)
        videobyid = VideModel.query.filter_by(id = video_id).first()
        if not videobyid:
            abort(404,message = "no video with that id")
        db.session.delete(videobyid)
        db.session.commit()
        return "successfully deleted video",204 # 204->deleted successfully
        

    

# class GermanHello(Resource):
    # def get(self, name):
    #     return {"name" :  names[name]}  # json data parceleable
    # def get(self,name,age):
    #     return {"name" : name,"age":age,"method":"get"}
    # def post(self,name):
    #     return {"data" : name + "Posted"} 
    # def post(self):
    #     return {"data" : "Posted"} 
    
api.add_resource(Video, "/video/<int:video_id>") # "/" means default URL .... use /<type : name> to define the type of parameter u will accept 
# /deutschHallo/<string:name>/<int:age>

api.add_resource(allvideolist,"/allvideolist")

if __name__ == "__main__":  
    app.run(debug=True) # this will start our server,flask app. (IF IN PRODUCTION ENV DO NOT RUN DEBUG=TRUE)
     