from flask import (
    Flask,
    render_template,
    abort,
    session,
    request,
    redirect,
    url_for
)
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["MONGODB_URI"] = os.getenv("MONGODB_URI")
    app.db = MongoClient(app.config["MONGODB_URI"])["Portfolio"]

    @app.route("/")
    def home():
        return redirect(url_for("about"))

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route('/bookshelf')
    def bookshelf():
        return render_template('bookshelf.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    @app.get("/toggle-theme")
    def toggle_theme():
        current_theme = session.get("theme")

        if current_theme == "dark":
            session["theme"] = "light"
        else:
            session["theme"] = "dark"

        return redirect(request.args.get("current_page"))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
