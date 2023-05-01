from flask import Flask, render_template, request
from py2neo import Graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123456789"))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = str(request.form['name'])
    birthdate = str(request.form['birthdate'])
    birthplace = str(request.form['birthplace'])
    name_fa = str(request.form['name_fa'])


    

    q1 = "create (emp:Person {"
    query = f"""
        name: '{str(name)}', birthdate: '{str(birthdate)}', birthplace: '{str(birthplace)}', name_fa: '{str(name_fa)}'
        """
    q2 = "})"
    quer = q1 + query+ q2


    m = graph.run(quer)
    
    return "Form submitted successfully!"



@app.route('/ppl')
def data():
    newquery = """
    MATCH (n) RETURN n LIMIT 25
    """
    m = graph.run(newquery)
    dta = m.data()
    return f"<h1>{dta}</h1>"

if __name__ == '__main__':
    app.run(port=8000)