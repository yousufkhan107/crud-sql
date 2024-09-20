   


from flask import Flask,request

app = Flask(__name__)



import db
import json

db_conn = db.mysqlconnect()






# @app.route("/books", methods=['GET'])
# def get_employees():
#   cur = db_conn.cursor()
#   cur.execute("SELECT * FROM category")
#   return cur.fetchall()
    


# @app.route('/books/<int:id>', methods=['GET'])
# def get_id(id):
#   cur = db_conn.cursor()
#   cur.execute("select * from category where id = %s" , (id,))
#   return cur.fetchall()    


# @app.route("/books", methods=['POST'])
# def add_employee():
#   params = request.get_json()
#   names = params.get("name")
#   print(names) 
#   cur = db_conn.cursor()
#   cur.execute("INSERT INTO category (name) VALUES (%s)", (names,))
#   db_conn.commit()
#   return "helll"


   

@app.route("/books/<int:id>", methods=['PUT'])
def update_books(id):
    params = request.get_json()
    names = params.get("name")
    cur = db_conn.cursor()
    cur.execute('UPDATE category SET name = %s , WHERE id = %s', (names,id))
    db_conn.commit()
    return "helll"

   
  
  
# @app.route("/books/<int:id>", methods=['DELETE'])
# def update(id):
#     cur = db_conn.cursor()
#     cur.execute("DELETE FROM category where id = %s" ,(id,))
#     db_conn.commit()
#     return "helll"
    

app.run(
    debug=True,
    port=3000
)
