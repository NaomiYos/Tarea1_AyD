from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return jsonify({
        "nombre": "Naomi Rashel Yos Cujcuj",
        "cancion favorita": "Resiste - La Texana"
    })
if __name__ == '__main__':
    app.run(debug=True)