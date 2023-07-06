from flask import Flask, render_template, abort, session, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    
    projects_info = [
        {
            "name": "Movie Watchlist WebApp",
            "desc": """I am a Movie geek, so I built a secure and user-friendly web app using HTML,
                    CSS, and Flask. Movie Watchlist allows you to effortlessly create and manage your
                    personalized movie collection. Powered by MongoDB Cloud for personalized data storage
                    and hosted on Heroku.""",
            "thumb": "img/movie-watchlist-wall.png",
            "hero": "img/habit-tracking-hero.png",
            "categories": ["flask", "css", "html", "mongodb"],
            "slug": "movie-watchlist",
            "prod": "https://movie-watchlist-by-adilet-b565458f53bd.herokuapp.com/login",
            "github": "https://github.com/AdiletBaimyrza/movie-watchlist",
        },
        {
            "name": "Personal finance tracking app with React",
            "desc": """I love helping students learn to code and
                    master software development. I've been teaching
                    online for over 6 years, and I founded Teclado to
                    bring software development to everyone—my objective
                    is for you to truly understand everything that goes on
                    behind the scenes.""",
            "thumb": "img/personal-finance.png",
            "hero": "img/personal-finance.png",
            "categories": ["react", "javascript"],
            "slug": "personal-finance",
            "prod": "#",
            "github": "",
        },
        {
            "name": "REST API Documentation with Postman and Swagger",
            "desc": """I love helping students learn to code and
                    master software development. I've been teaching
                    online for over 6 years, and I founded Teclado to
                    bring software development to everyone—my objective
                    is for you to truly understand everything that goes on
                    behind the scenes.""",
            "thumb": "img/rest-api-docs.png",
            "hero": "img/rest-api-docs.png",
            "categories": ["writing"],
            "slug": "api-docs",
            "prod": "#",
            "github": "#",
        },
    ]

    slug_to_project = {project["slug"]: project for project in projects_info}

    @app.route("/")
    def home():
        return redirect(url_for("about"))
    
    @app.route("/projects")
    def projects():
        return render_template("projects.html", projects=projects_info)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route('/contact')
    def contact():
        contact_details = [
            {
                "desc": "adiletbaimyrza@gmail.com",
                "class": "gmail",
                "link": "mailto:adiletbaimyrza@gmail.com"
            },
            {
                "desc": "Adilet Baimyrza",
                "class": "linkedin",
                "link": "https://www.linkedin.com/in/adiletbaim/"
            },
            {
                "desc": "@adiletBaimyrza",
                "class": "github",
                "link": "https://github.com/AdiletBaimyrza"
            }
        ]
        return render_template('contact.html', contact_details=contact_details)

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        
        return render_template(f'project_{slug}.html', project=slug_to_project[slug])

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