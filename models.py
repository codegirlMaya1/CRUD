from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

class Member:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class WorkoutSession:
    def __init__(self, session_id, member_id, session_date, session_time, activity):
        self.session_id = session_id
        self.member_id = member_id
        self.session_date = session_date
        self.session_time = session_time
        self.activity = activity

class MemberSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "age")

class WorkoutSessionSchema(ma.Schema):
    class Meta:
        fields = ("session_id", "member_id", "session_date", "session_time", "activity")