from flask import Flask

# requesting flask to create web application
app = Flask(__name__) 

#flask routing
# / - home page
# to print hello world we need to define route
@app.route("/")
def hello():
    return "Welcome<h1>Hello World...</h1>"

if __name__=="__main__":
    app.run(debug=True, port=8000)
# debug turns on the debug-mode so that we can get error
# port=8000, for changing the port
    
    
    
    
#*Note* - It will give a link. We need to press the link to get hello world.