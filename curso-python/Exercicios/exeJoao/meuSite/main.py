#Aprendendo a criar site com o flask # Hashtag treinamentos

from flask import Flask
from routes import create_routes

app = Flask(__name__)
create_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
