from flask import Flask, render_template,request
from flask import MySQL
import yaml
app = Flask(_name_)
#Config db
db = yaml.load(open('db.yaml'))
app.Config['MYSQL_HOST'] =db['mysql_host']
app.Config['MYSQL_USER'] = db['mysql_user']
app.Config['MYSQL_PASSWORD'] = db['mysql_password']
app.Config['MYSQL_DB'] =db['mysql_db']

mysql = MYSQL(app)
@app.route('/', methods=['GET','POST'])
def index():
	if request.methods == 'post':
		#fetch data 
		userdetails = request.form
		name = userdetails['name']
		img = userdetails['file']
		summary = userdetails['textarea']
		cur = mysql.connection.cursor()
        cur.execute("INSERT INTO application(name,img,summ) VALUES(%s,%s,%s)(name,image,summary)")
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return 'successful'
    return render_template('index.html')
    @app.route('/users')
    def users():
    	cur = msql.connection,cursor()
    	resultValue = cur.execute("select * from application")
    	if resultValue > 0:
    		userdetails = cur.fetchll()
    		return render_template('users.html',userdetails=userdetails)
if _name_ == '_main_':
    app.run(debug=True)
