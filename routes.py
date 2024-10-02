from flask import Flask, request, jsonify
from config import get_db_connection
from models import Member, MemberSchema, WorkoutSession, WorkoutSessionSchema

app = Flask(__name__)

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
workout_session_schema = WorkoutSessionSchema()
workout_sessions_schema = WorkoutSessionSchema(many=True)

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

if __name__ == '__main__':
    app.run(debug=True)