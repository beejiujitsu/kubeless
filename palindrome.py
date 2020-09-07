from flask import Flask
from flask_restful import fields, marshal, Resource, Api
import re
from typing import Dict


class Palindrome(Resource):
    def get(self, word) -> Dict[str, bool]:
        return palindrome(word)


def palindrome(word) -> Dict[str, bool]:
    normalized = re.sub(r"\W+", "", word).lower()
    return {
        "given": word,
        "normalized": normalized,
        "palindrome": normalized == normalized[::-1],
    }


def is_palindrome(word) -> bool:
    return palindrome(word).get("palindrome")


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Palindrome, "/<word>")
    app.run()
