import logging
import json
from flask import Flask, render_template, request

from src.UserAgent import ParsedUserAgent

from src.Fingerprint import FingerPrint

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("googleapiclient.discovery").setLevel(logging.WARNING)
logging.getLogger("googleapiclient.discovery_cache").setLevel(logging.ERROR)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def timer():
    fp = FingerPrint(request)
    logger.info(fp.request)
    return render_template("id.html.j2", fp=fp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
