#!/usr/bin/python3

import json

from flask import Flask
from flask import request
from flask.ext.cors import CORS
app = Flask(__name__)

HOST = "0.0.0.0"
PORT = 3030

CORS(app)

@app.route("/api/v1/")
def hello():
    return "hello repo"

@app.route("/api/v1/review", methods=['POST'])
def submit_request():
    print("submit review request")
    _tmp = """{
        "failed": false,
        "result": ""
    }"""
    return _tmp


@app.route("/api/v1/reviews", methods=['GET'])
def get_all_reviews():
    _tmp = """
        {
            "failed": false,
            "result": {
                "reviews":[{
                        "id": 23,
                        "topic": "balaba",
                        "base": "http://packages.deepin.com/deepin",
                        "base_codename": "unstable",
                        "rpa": "http://pools.corp.deepin.com/ppa/dstore",
                        "rpa_codename": "experimental",
                        "status": "open",
                        "submit_timestamp": "1456999262"
                    },
                    {
                        "id": 24,
                        "topic": "balaba",
                        "base": "http://packages.deepin.com/deepin",
                        "base_codename": "unstable",
                        "rpa": "http://pools.corp.deepin.com/ppa/dstore",
                        "rpa_codename": "experimental",
                        "status": "open",
                        "submit_timestamp": "1456999262"
                    }
                ]
            }
        }
    """
    return _tmp


@app.route("/api/v1/review/<int:rr_number>", methods=['GET'])
def get_review(rr_number):
    print("review num: %s" % rr_number)
    _tmp = """
        {
            "failed": false,
            "result": {
                "id": %d,
                "topic": "balaba",
                "base": "http://packages.deepin.com/deepin",
                "base_codename": "unstable",
                "rpa": "http://pools.corp.deepin.com/ppa/dstore",
                "rpa_codename": "experimental",
                "comment": "comment",
                "shell": "echo \\"deb http://pools.corp.deepin.com/test0225/ unstable main contrib non-free\\" > /etc/apt/sources.list\\n            echo \\"deb http://10.0.1.38/testrepo/ unstable main contrib non-free\\" >> /etc/apt/sources.list\\n            ",
                "status": "open",
                "submit_timestamp": "1456999262",
                "comments":[
                    {
                        "submitter": "choldrim",
                        "content": "look good to me ;)",
                        "create_timestamp": "1456999262",
                        "score": 1,
                        "verified": 0
                    },
                    {
                        "submitter": "wangyanli",
                        "content": "start testing",
                        "create_timestamp": "1456999262",
                        "score": 0,
                        "verified": 0
                    },
                    {
                        "submitter": "wangyanli",
                        "content": "test failed",
                        "create_timestamp": "1456999262",
                        "score": 0,
                        "verified": -1
                    }
                ]
            }
        }
    """ % rr_number
    _json = json.loads(_tmp)
    _tmp = json.dumps(_json)
    return _tmp


@app.route("/api/v1/test_result/<int:review_num>", methods=['POST'])
def submit_test_result(review_num):
    print("submit test result")
    data = request.form
    if not data:
        data = request.get_json()
    print(data)
    _tmp = """
    {
        "failed": false,
        "result": ""
    }
    """
    return _tmp


@app.route("/api/v1/merge/<int:review_id>", methods=['POST'])
def merge(review_id):
    print("merge repo")
    _tmp = """
    {
        "failed": false,
        "result": ""
    }
    """
    return _tmp


@app.route("/api/v1/merge_result/<int:merge_id>", methods=['POST'])
def merge_result(merge_id):
    print("return merge repo result")
    _tmp = """
    {
        "failed": false,
        "result": ""
    }
    """
    return _tmp


@app.route("/api/v1/abandon/<int:review_id>", methods=['POST'])
def abandon_review(review_id):
    print("abandon review")
    _tmp = """
    {
        "failed": false,
        "result": ""
    }
    """
    return _tmp


@app.route("/api/v1/comment/<int:review_id>", methods=['POST'])
def comment(review_id):
    print("comment review")
    _tmp = """
    {
        "failed": false,
        "result": ""
    }
    """
    return _tmp



if __name__ == "__main__":
    app.debug = True
    app.run(host=HOST, port=PORT)
