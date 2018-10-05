from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    #return "OpenShift Hello World!"
    return "Created by Richardo"
    #return "Friday, October 5th, 2018"

if __name__ == "__main__":
    application.run()
