#!/usr/bin/python3
""" Quiz route module """

from api.views import app_views
from flask import jsonify, render_template
from models.question import Question
from models import storage
import requests, random, html

@app_views.route('/quiz', methods=['GET', 'POST'], strict_slashes=False)
def quiz():
    """Quiz page route"""
    return render_template("quiz.html")

@app_views.route('/fetch_questions', methods=['GET', 'POST'], strict_slashes=False)
def fetch_questions():
    """Fetch questions using opentdb API and store in DB"""
    # Clear existing questions from the database
    try:
        for obj in storage.all(Question).values():
            storage.delete(obj)
        storage.save()
    except Exception as e:
        return jsonify({'error': 'Failed to clear database: {}'.format(e)}), 500

    # Fetch question from OpenTDB API
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

        # Ensure options are exactly 4
        if len(options) != 4:
            continue

        # Shuffle options for right answer
        random.shuffle(options)
        correct_option = options.index(correct_answer) + 1

        # Create a new Question object
        try:
            question = Question(
                question=question_text,
                option_1=options[0],
                option_2=options[1],
                option_3=options[2],
                option_4=options[3],
                correct_option=correct_option
            )
            storage.new(Question)
        except Exception as e:
            return jsonify({'error': 'Failed to save question: {}'.format(e)}), 500

    # Commit all changes to the database
    try:
        storage.save()
    except Exception as e:
        return jsonify({'error', 'Failed to save data in database: {}'.format(e)}), 500
    return jsonify({'message': 'Questions fetched and stored successflly'}), 200
    return redirect(url_for('app_views.results_routes'))
