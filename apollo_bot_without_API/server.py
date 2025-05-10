from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/mixed_people/search', methods=['POST'])
def search_people():
    data = request.get_json()
    query = data.get('person_names', '')

    if query:
        return jsonify({
            "people": [{
                "name": "Sundar Pichai",
                "title": "CEO",
                "organization": {"name": "Google"},
                "email": "sundar@google.com",
                "linkedin_url": "https://linkedin.com/in/sundarpichai"
            }]
        })
    else:
        return jsonify({"error": "No results found"})

if __name__ == '__main__':
    app.run(debug=True)
