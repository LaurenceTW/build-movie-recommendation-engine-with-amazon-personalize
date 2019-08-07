import requests
import json
from flask import Flask, jsonify, request, render_template
import personalize
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index_page():
    return render_template('input_data.html')


@app.route('/result', methods=['POST', 'GET'])
def predict_result():
    if request.method == 'POST':
        # get user id
        user_input = request.form.getlist('text')
        predict_item = user_input[0]
        # use amazon personalize to recommend movie to user
        url_list,name_list = personalize.predict_movie(predict_item)

        return render_template('personalize.html', url_list=url_list, name_list=name_list,predict_item=predict_item)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0', port=8080)
