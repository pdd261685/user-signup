from flask import Flask, request, redirect, escape,render_template
import html

app = Flask (__name__)

app.config['DEBUG']=True


@app.route("/")  
# ,'GET'])
def inedx():
   return render_template('errors.html')

@app.route("/signup",methods=['POST']) 

def signup():
    error1=''
    error2=''
    error3=''
    error4=''
    u_name=request.form['user_name']
    pwd=request.form['pwd']
    v_pwd=request.form['vpwd']
    email=request.form['email']


    if ' ' in u_name or len(u_name)<3 or len(u_name)>20:
        error1="Thats not a valid user name"
       
    if ' ' in pwd or len(pwd)<3 or len(pwd)>20 :
        error2="Thats not a valid password"
    if ' ' in v_pwd or len(v_pwd)<3 or len(v_pwd)>20 or v_pwd!= pwd :
        error3="Passwords don't match"    
        
    if email:
        if ' ' in email or len(email)<3 or len(email)>20 or email.count('@')>1 or email.count('.')>1 or  email[-1]=='@' or '@' not in email:
            error4="That's not a valid email"

    if error1 or error2 or error3 or error4 :
        return render_template('errors.html',user_name=u_name,email=email,error1=error1,error2=error2,error3=error3,error4=error4)        
    else:
        return render_template('welcome.html',user_name=u_name)


app.run()