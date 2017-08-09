import re
import random
import string
from functools import wraps

from flask import Flask, request, jsonify, abort


def key():
    return ''.join(random.choice(string.ascii_letters) for x in range(10))


def nick_check(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        nick = request.args.get("nick")

        if not nick:
            return abort(402)

        if len([c for c in nick if nick == " "]) * 2 >= len(text):
            return abort(400)
        else:
            return f(*args, **kwargs)

    return wrapper


app = Flask(__name__)


@app.route("/api/pwn", methods=["GET"])
@nick_check
def pwn():
    with open("keys.txt", "a") as out:
        vid, secret = key(), key().lower()
        nick = request.args.get("nick", "[no name query]")
        data = "{}:{}:{}".format(vid, secret, nick)
        out.write(data + "\n")
        return jsonify({"id": vid, "secret": secret})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6970)
