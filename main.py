import subprocess
from flask import Flask, send_file
import os


app = Flask(__name__)


@app.route("/snapshot", methods=["GET"])
def snapshot():
    try:
        subprocess.run(["gphoto2", "--capture-image-and-download"], cwd=os.getcwd())
        result = send_file("capt0000.jpg", mimetype="image/jpg")
        subprocess.run(["rm", "capt0000.jpg"], cwd=os.getcwd())
        return result
    except:
        return send_file("backenderror.jpg", mimetype="image/jpg")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=4040)
