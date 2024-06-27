from ext import app, db
import routes, routes2
from models import Post, User, Comment
if __name__ == "__main__":

    app.run(debug=True)
