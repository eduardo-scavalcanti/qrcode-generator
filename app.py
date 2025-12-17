from flask import Flask, render_template, request, send_file, abort
import os
import qrcode
import time
import uuid

QR_FOLDER = "static/qrcodes"
MAX_QRCODE_TIME = 1800

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    clean_old_qrcodes(QR_FOLDER, MAX_QRCODE_TIME)

    qr_code_path = None
    filename = None

    if request.method == "POST":
        url = request.form["url"]

        img = qrcode.make(url)

        filename = f"{uuid.uuid4()}.png"

        qr_code_path = os.path.join(QR_FOLDER, filename)

        img.save(qr_code_path)

    return render_template("index.html", qr_code=qr_code_path, filename=filename)


@app.route("/download/<filename>")
def download_qr(filename):
    file_path = os.path.join(QR_FOLDER, filename)

    if not os.path.exists(file_path):
        abort(404)

    return send_file(file_path, as_attachment=True)


def clean_old_qrcodes(folder, max_qrcode_time):
    now = time.time()

    for qrcode in os.listdir(folder):
        path = os.path.join(folder, qrcode)

        if os.path.isfile(path):
            file_time = os.path.getmtime(path)

            if now - file_time > max_qrcode_time:
                os.remove(path) 


if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)

if __name__ == "__main__":
    app.run(debug=True)