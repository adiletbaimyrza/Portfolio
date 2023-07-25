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
    
    projects_info = [
        {
            "name": "Movie Watchlist WebApp",
            "desc": """I am a Movie geek, so I built a secure and user-friendly web app using HTML,
                    CSS, and Flask. Movie Watchlist allows you to effortlessly create and manage your
                    personalized movie collection. Powered by MongoDB Cloud for personalized data storage
                    and hosted on Heroku.""",
            "thumb": "img/movie-watchlist-wall.png",
            "categories": ["python", "css", "html", "mongodb"],
            "prod": "https://movie-watchlist-by-adilet-b565458f53bd.herokuapp.com/login",
            "github": "https://github.com/AdiletBaimyrza/movie-watchlist",
        },
        {
            "name": "Lyft Back-End Engineering Virtual Experience Program",
            "desc": """At this Virtual Experience Program, I refactored the codebase by the design
                    given by engineers, added a new parameter for car servicing and wrote unit tests for it
                    while following SOLID principles.""",
            "thumb": "img/lyft-logo.png",
            "categories": ["python", "unittests", "software design"],
            "prod": "https://www.theforage.com/virtual-internships/prototype/xSw9echtixLAoPdsH/Lyft-Back-End-Engineering-Virtual-Experience-Program",
            "github": "https://github.com/AdiletBaimyrza/forage-lyft-starter-repo",
        },
        {
            "name": "Team Project - Telegram Bot",
            "desc": """Led a group of three students in the development of a Telegram-bot
            that could generate graphs of mathematical functions based on functions given
            as strings and manipulate them with various commands. This project was the part of Software Engineering Course.""",
            "thumb": "img/bot.png",
            "categories": ["python", "numpy", "matplotlib", "telegram-api"],
            "prod": "#",
            "github": "https://github.com/AdiletBaimyrza/FunctionPlotterBot",
        },
    ]

    @app.route("/")
    def home():
        return redirect(url_for("about"))
    
    @app.route("/projects")
    def projects():
        return render_template("projects.html", projects=projects_info)

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
    app.run()