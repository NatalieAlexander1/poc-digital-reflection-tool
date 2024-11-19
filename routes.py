from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, JournalEntry, GratitudeEntry, Goal
from extensions import db

routes_blueprint = Blueprint('routes', __name__)

# ... (keep existing routes) ...

@routes_blueprint.route('/add_journal_entry', methods=['POST'])
@jwt_required()
def add_journal_entry():
    user_id = get_jwt_identity()
    entry = request.json.get('entry', '')
    
    new_entry = JournalEntry(user_id=user_id, entry=entry)
    db.session.add(new_entry)
    db.session.commit()
    
    return jsonify({'success': True}), 200

@routes_blueprint.route('/get_journal_entries', methods=['GET'])
@jwt_required()
def get_journal_entries():
    user_id = get_jwt_identity()
    entries = JournalEntry.query.filter_by(user_id=user_id).order_by(JournalEntry.date.desc()).all()
    return jsonify({'entries': [{'date': entry.date.strftime('%Y-%m-%d'), 'entry': entry.entry} for entry in entries]}), 200

@routes_blueprint.route('/add_gratitude', methods=['POST'])
@jwt_required()
def add_gratitude():
    user_id = get_jwt_identity()
    entry = request.json.get('entry', '')
    
    new_entry = GratitudeEntry(user_id=user_id, entry=entry)
    db.session.add(new_entry)
    db.session.commit()
    
    return jsonify({'success': True}), 200

@routes_blueprint.route('/get_gratitude_entries', methods=['GET'])
@jwt_required()
def get_gratitude_entries():
    user_id = get_jwt_identity()
    entries = GratitudeEntry.query.filter_by(user_id=user_id).order_by(GratitudeEntry.date.desc()).all()
    return jsonify({'entries': [{'date': entry.date.strftime('%Y-%m-%d'), 'entry': entry.entry} for entry in entries]}), 200

@routes_blueprint.route('/add_goal', methods=['POST'])
@jwt_required()
def add_goal():
    user_id = get_jwt_identity()
    title = request.json.get('title', '')
    description = request.json.get('description', '')
    
    new_goal = Goal(user_id=user_id, title=title, description=description)
    db.session.add(new_goal)
    db.session.commit()
    
    return jsonify({'success': True}), 200

@routes_blueprint.route('/get_goals', methods=['GET'])
@jwt_required()
def get_goals():
    user_id = get_jwt_identity()
    goals = Goal.query.filter_by(user_id=user_id).all()
    return jsonify({'goals': [{'id': goal.id, 'title': goal.title, 'description': goal.description, 'status': goal.status} for goal in goals]}), 200

@routes_blueprint.route('/update_goal_status/<int:goal_id>', methods=['PUT'])
@jwt_required()
def update_goal_status(goal_id):
    user_id = get_jwt_identity()
    status = request.json.get('status', '')
    
    goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
    if goal:
        goal.status = status
        db.session.commit()
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False, 'message': 'Goal not found'}), 404
