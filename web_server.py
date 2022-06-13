from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route("/")
def alpha():
    return render_template("alpha.html")

@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def _upload_file():
    if request.method == 'POST':
        global f
        f = request.files['file']
        os.chdir(r"C:\Users\shang\Desktop\python\Question_Maker_proj\Uploads")
        f.save(secure_filename(f.filename))
        print(f.filename)
        from main import Process
        a = Process()
        a.main(f.filename)
        return render_template("Upload_successful.html")

@app.route("/Download", methods = ['GET', 'POST'])
def download_files():
    print(f.filename)
    link1 = f.filename[:-4] + "_questions.txt"
    link2 = f.filename[:-4] + "_answers.txt"
    return render_template("Download.html", link1=link1, link2=link2)




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)