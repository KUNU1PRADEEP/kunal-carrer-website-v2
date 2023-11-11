from flask import Flask, render_template,jsonify

app=Flask(__name__)

JOBS=[

  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru',
    'salary':'$100,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'delhi,India ',
    'salary':'$100,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$120,000'
  }
]

@app.route("/")
# def hello_world():
#   return "Hello, world"

def hello_kunal():
  return render_template('home.html',jobs=JOBS,company_name='Kunal')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0' ,debug=True)