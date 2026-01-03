from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Student')
    return jsonify({"message": f"Hello {name}, welcome to REST API!"})

if __name__ == '__main__':
    app.run(debug=True)
