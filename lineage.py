from flask import Blueprint,render_template

lineage = Blueprint('lineage', __name__)

@lineage.route('/')
def index():
    return render_template('index.html')