from flask import Flask, jsonify
from routes.tasks import tasks_bp

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

app.register_blueprint(tasks_bp, url_prefix="/tasks")

if __name__ == "__main__":
    app.run(debug=True)

    