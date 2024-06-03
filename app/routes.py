from flask import request, jsonify
from app import app, db
from app.models import User, Language, LearningMaterial, Assessment, Progress

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'Please provide username, email, and password'}), 400
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # user = User.query.filter_by(username=username).first()
    # if user is None or not user.check_password(password):
    #     return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}), 200

@app.route('/languages', methods=['GET'])
def get_books():  
    return jsonify({"Languages Available ": "1.English 2.Bengali 3.Hindi 4.Spanish 5.French 6.Italian"}), 200

@app.route('/materials', methods=['GET'])
def get_materials():  
    return jsonify({"Materials Available ": "1.Youtube Vedios 2.Vocabulary lists 3.Audio recordings 4.Interactive lessons"}), 200

@app.route('/profeciency', methods=['GET'])
def get_profeciency():  
    return jsonify({"You profeciency ": "Beginner"}), 200

@app.route('/assesment', methods=['GET'])
def get_assesment():  
    return jsonify({"Assesment Link ": "Click Here"}), 200

# Define other routes for language selection, learning materials, assessments, and progress tracking here
