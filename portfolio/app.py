from flask import Flask, render_template, abort, session, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    
    projects_info = [
        {
            "name": "Habit tracking app with Python and MongoDB",
            "thumb": "img/habit-tracking.png",
            "hero": "img/habit-tracking-hero.png",
            "categories": ["python", "web"],
            "slug": "habit-tracking",
            "prod": "https://udemy.com",
        },
        {
            "name": "Personal finance tracking app with React",
            "thumb": "img/personal-finance.png",
            "hero": "img/personal-finance.png",
            "categories": ["react", "javascript"],
            "slug": "personal-finance",
            "prod": "https://udemy.com",
        },
        {
            "name": "REST API Documentation with Postman and Swagger",
            "thumb": "img/rest-api-docs.png",
            "hero": "img/rest-api-docs.png",
            "categories": ["writing"],
            "slug": "api-docs",
            "prod": "https://udemy.com",
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