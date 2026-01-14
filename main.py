import subprocess
from flask import Flask, send_file


app = Flask(__name__)


@app.route("/snapshot", methods=["GET"])
def snapshot():
    subprocess.run(["gphoto2", "--capture-image-and-download"])
    result = send_file("capt0000.jpg", mimetype="image/jpg")
    subprocess.run(["rm", "capt0000.jpg"])
    return result


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=4040)
