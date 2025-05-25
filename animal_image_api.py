from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual Pexels API Key
PEXELS_API_KEY = 'pdSarskJusFmCaQBwkFjVnkoNR33LnUyFxhA8q1d1yhGxZU2kQeadzLi'
PEXELS_URL = 'https://api.pexels.com/v1/search'

@app.route('/animal-image', methods=['GET'])
def get_animal_image():
    animal = request.args.get('animal')

    if not animal:
        return jsonify({'error': 'Animal name is required'}), 400

    headers = {
        'Authorization': PEXELS_API_KEY
    }

    params = {
        'query': animal,
        'per_page': 1
    }

    response = requests.get(PEXELS_URL, headers=headers, params=params)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch image'}), 500

    data = response.json()

    if not data['photos']:
        return jsonify({'error': 'No image found for this animal'}), 404

    image_url = data['photos'][0]['src']['medium']

    return jsonify({
        'animal': animal,
        'image_url': image_url
    })

if __name__ == '__main__':
    app.run(debug=True)
