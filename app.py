from flask import Flask, request, Response

app = Flask(__name__)

db = {"Ang": "Mon: 1500-1800; Tue: 0900-1200, 1400-1800; Thu: 0800-1200",
      "Tan": "Wed: 0900-1200, 1400-1800; Fri: 0800-1200",
      "Ong": "Tue: 1200-1400; Thu: 1600-1900, 1600-1800; Fri: 1200-1800"}

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/get-sched")
def get_sched():
    last_name = request.args.get('name')
    print(last_name)
    text = db[last_name]
    return Response(text, 200, mimetype="text/plain")

if __name__ == "__main__":
    app.run("0.0.0.0", port="5005")
