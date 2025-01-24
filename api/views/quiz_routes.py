#!/usr/bin/python3
""" Quiz route module """

from api.views import app_views
from flask import jsonify, render_template
from models.question import Question
from models import storage
import requests, random, html

@app_views.route('/quiz', methods=['GET', 'POST'], strict_slashes=False)
def quiz():
    """quiz page route"""
    return render_template("quiz.html")

def fetch_questions():
    """fetch questions using opentdb API and store in DB"""
    # Clear existing questions from the database
    storage.all(Question).clear()
    storage.save()

    # Fetch question from the API
    response = requests.get('https://opentdb.com/api.php?amount=10&category=17&type=multiple')

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch questions!'}), 500
    
    data = response.json()

    if not data.get('results'):
        return jsonify({'error': 'No questions found'}), 404
    
    # Process API response
    for item in data['results']:
        question_text = html.unescape(item.get('question'))
        options = [html.unescape(opt) for opt in item.get('incorrect_answers', [])]
        correct_answer = html.unescape(item.get('correct_answer'))
        options.append(correct_answer)

        if len(options) != 4:
            continue    # Ensure options are exactly 4

        # Shuffle options for right answer
        random.shuffle(options)
        correct_option = options.index(correct_answer) + 1

        # Create a new Question object
        question = Question(
            question=question_text,
            option_1=options[0],
            option_2=options[1],
            option_3=options[2],
            option_4=options[3],
            correct_option=correct_option
        )

        # Add and save the question
        storage.new(question)
    
    # Commit all changes to the database
    storage.save()
    return jsonify({'message': 'Questions fetched and stored successflly'}), 200
