from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download_image():
    return send_from_directory("static", "drone_view.jpg", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
