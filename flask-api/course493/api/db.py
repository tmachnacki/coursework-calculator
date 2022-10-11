"""API for managing db."""

import flask
# from flask_cors import CORS
# from flask_cors import cross_origin
import course493

@course493.app.route('/', methods=["GET"])
def get_service():
    """Return available service."""
    print("service")
    context = {
        "courses": "/courses/DEPT/NO",
        "url": flask.request.path,
    }
    return flask.jsonify(**context)

@course493.app.route('/<dept>/<no>', methods=["GET"])
def get_course(dept, no):
    
    print(dept)
    print(no)

    courseName = dept + " " + no
    print(courseName)

    connection = course493.model.get_db()

    print("connected")

    course_fetch = connection.execute(
        "SELECT classname, department, classnumber, title, credits, workload "
        "FROM classes "
        "WHERE classname = ?", (courseName,)
    )
    print(course_fetch)

    course = course_fetch.fetchone()

    print(course)
    
    if not course:
        context = {
            "classname": "none"
        }
        #response = flask.jsonify(**context)
        #response.add.headers('Access-Control-Allow-Origin', 'http://localhost')
        return flask.jsonify(**context)

    context = {
        "classname": course["classname"],
        "department": course["department"],
        "title": course["title"],
        "classnumber": course["classnumber"],
        "credits": course["credits"],
        "workload": course["workload"],
    }

    print(context)

    #response = flask.jsonify(**context)
    #response.add.headers('Access-Control-Allow-Origin', 'http://localhost')
    return flask.jsonify(**context)





