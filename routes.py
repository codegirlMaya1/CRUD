from flask import Flask, request, jsonify
from config import get_db_connection
from models import Member, MemberSchema, WorkoutSession, WorkoutSessionSchema

app = Flask(__name__)

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
workout_session_schema = WorkoutSessionSchema()
workout_sessions_schema = WorkoutSessionSchema(many=True)

# Member routes
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    id = data['id']
    name = data['name']
    age = data['age']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Member added successfully"}), 201

@app.route('/members', methods=['GET'])
def get_members():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(members_schema.dump(members))

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE members SET name=%s, age=%s WHERE id=%s", (name, age, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Member updated successfully"})

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Member deleted successfully"})

# WorkoutSession routes
@app.route('/workoutsessions', methods=['POST'])
def add_workout_session():
    data = request.get_json()
    session_id = data['session_id']
    member_id = data['member_id']
    session_date = data['session_date']
    session_time = data['session_time']
    activity = data['activity']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO workoutsessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)", 
                   (session_id, member_id, session_date, session_time, activity))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Workout session added successfully"}), 201

@app.route('/workoutsessions', methods=['GET'])
def get_workout_sessions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workoutsessions")
    workout_sessions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(workout_sessions_schema.dump(workout_sessions))

@app.route('/workoutsessions/<int:session_id>', methods=['PUT'])
def update_workout_session(session_id):
    data = request.get_json()
    member_id = data['member_id']
    session_date = data['session_date']
    session_time = data['session_time']
    activity = data['activity']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE workoutsessions SET member_id=%s, session_date=%s, session_time=%s, activity=%s WHERE session_id=%s", 
                   (member_id, session_date, session_time, activity, session_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Workout session updated successfully"})

@app.route('/workoutsessions/<int:session_id>', methods=['DELETE'])
def delete_workout_session(session_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM workoutsessions WHERE session_id=%s", (session_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Workout session deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
