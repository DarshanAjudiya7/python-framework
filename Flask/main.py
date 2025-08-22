from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def index123():
    return render_template('index.html')

@app.route("/in2")
def index456():
    name = "Darshan"
    return render_template('index2.html', Fname = name)

@app.route("/ajudiya")
def family():
    return "hello ajudiyaas. how are you??"

@app.route("/boot")
def application():
    return render_template('bootstrap.html')


@app.route("/sample")
def website():
    return render_template('sample.html')

app.run(debug=True)
