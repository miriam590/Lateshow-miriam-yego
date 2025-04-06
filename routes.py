from flask import request, jsonify, make_response
from app import app
from models import Episode, Guest, Appearance
from extensions import db

@app.route('/')
def home():
    return make_response(jsonify({
        'message': 'Welcome to the Late Show API',
        'endpoints': {
            'episodes': '/episodes',
            'guests': '/guests',
            'appearances': '/appearances'
        }
    }), 200)

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    
    episode_data = episode.to_dict()
    episode_data['appearances'] = [{
        'id': appearance.id,
        'rating': appearance.rating,
        'episode_id': appearance.episode_id,
        'guest_id': appearance.guest_id,
        'guest': appearance.guest.to_dict()
    } for appearance in episode.appearances]
    
    return jsonify(episode_data)

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        
        if not (1 <= appearance.rating <= 5):
            return jsonify({'errors': ['Rating must be between 1 and 5']}), 400
            
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify(appearance.to_dict()), 201
        
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400
