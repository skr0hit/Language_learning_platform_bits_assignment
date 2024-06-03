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

# Define other routes for language selection, learning materials, assessments, and progress tracking here
