from flask import Flask, render_template, request
import downloader

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=['POST'])
def download():
    url = request.form['url']
    d = downloader.get_content(url)
    if d:
        return render_template("download.html")
    else:
        print("wrong")

if __name__=="__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')