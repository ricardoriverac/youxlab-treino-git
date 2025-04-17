#Rotas
#www.sitetestedojoao.com/home
#www.sitetestedojoao.com/blog
#www.sitetestedojoao.com/contato e etc

from flask import render_template

def create_routes(app):
    @app.route("/")
    def homepage():
        return render_template("homepage.html")

    @app.route("/blog")
    def blog():
        return render_template("blog.html")
