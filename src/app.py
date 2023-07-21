"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person


app = Flask(__name__)
CORS(app)

family = FamilyStructure("Jackson")

@app.route('/members', methods=['GET'])
def get_all_members():
    members = family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member = family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    member_info = request.get_json()
    if not member_info:
        return jsonify({"error": "Bad request"}), 400
    member = family.add_member(member_info)
    return jsonify(member), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = family.delete_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify({"done": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
