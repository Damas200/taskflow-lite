from flask import Flask
from app.routes import task_routes

def create_app():
    app = Flask(__name__, template_folder="templates")
    
    app.register_blueprint(task_routes)

    return app
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)