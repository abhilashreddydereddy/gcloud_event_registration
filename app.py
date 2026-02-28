from flask import Flask, render_template, request, redirect
from google.cloud import firestore

app = Flask(__name__)

db = firestore.Client()

@app.route('/')
def index():
    docs = db.collection("registrations").stream()
    registrations = [doc.to_dict() for doc in docs]
    return render_template("index.html", registrations=registrations)


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    event = request.form.get("event")

    db.collection("registrations").add({
        "name": name,
        "email": email,
        "event": event
    })

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)