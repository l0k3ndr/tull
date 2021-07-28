import os
import sys
from flask import Flask, jsonify
from constants import TULL_DATA_DIR

# <UI_RELATED_MINIMAL_CODING>
PAGE_REFRESH_JS = '<script>window.setInterval("refresh()", 10000); function refresh() {window.location.reload();}</script>'
html = lambda x: "<html>" + x + "</html>"
body = lambda x: "<body>" + x + "</body>"
head = lambda x: "<head>" + x + "</head>"
# </UI_RELATED_MINIMAL_CODING>

# disable flask banner
cli = sys.modules["flask.cli"]
cli.show_server_banner = lambda *x: None

# create flask app with apis
app = Flask(__name__)

# disable trailing slashes
app.url_map.strict_slashes = False


@app.route("/tull/raw")
def get_list_raw():
    return "\n".join(
        sid
        for sid in sorted(
            os.listdir(TULL_DATA_DIR),
            key=lambda x: os.path.getatime(f'{TULL_DATA_DIR}/{x}'),
            reverse=True,
        )
    )


@app.route("/tull/raw/<tull_id>")
def get_logs_raw(tull_id):

    try:
        if tull_id in os.listdir(TULL_DATA_DIR):
            with open(f'{TULL_DATA_DIR}/{tull_id}') as f:
                return f.read()
    except:
        return ""


@app.route("/tull/api")
def get_list_api():
    return jsonify(
        {
            "data": [
                x
                for x in sorted(
                    os.listdir(TULL_DATA_DIR),
                    key=lambda x: os.path.getatime(f'{TULL_DATA_DIR}/{x}'),
                    reverse=True,
                )
            ]
        }
    )


@app.route("/tull/api/<tull_id>")
def get_logs_api(tull_id):

    try:
        if tull_id in os.listdir(TULL_DATA_DIR):
            with open(f'{TULL_DATA_DIR}/{tull_id}') as f:
                return jsonify({"data": [x for x in f.readlines()]})
    except:
        return jsonify({"data": None})


@app.route("/tull/web")
def get_list():
    response = ""

    for link in [
        f'<a href="/tull/web/{sid}">{sid}</a>'
        for sid in sorted(
            os.listdir(TULL_DATA_DIR),
            key=lambda x: os.path.getatime(f'{TULL_DATA_DIR}/{x}'),
            reverse=True,
        )
    ]:
        response += link + "<br></br>"

    return html(body(response))


@app.route("/tull/web/<tull_id>")
def get_logs(tull_id):

    try:
        if tull_id in os.listdir(TULL_DATA_DIR):
            with open(f'{TULL_DATA_DIR}/{tull_id}') as f:
                return html(
                    head(PAGE_REFRESH_JS)
                    + body("<br>".join([x for x in f.readlines()]))
                )
    except:
        return html(body("No data found in log stream"))


@app.route("/server/halt")
def halt_server():
    os.kill(os.getpid(), signal.SIGKILL)
