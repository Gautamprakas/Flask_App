from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/math',methods=['POST'])
def math_operation():
    ops=request.form['operation']
    num1=int(request.form['num1'])
    num2=int(request.form['num2'])
    if ops=='add':
        sum=num1+num2
        result= "the "+ops+" of "+str(num1)+" and "+str(num2)+" is "+str(sum)
    if ops=='subtract':
        sum=num1-num2
        result= "the"+ops+" of"+str(num1)+" and "+str(num2)+" is "+str(sum)
    if ops=='multiply':
        sum=num1*num2
        result= "the "+ops+" of "+str(num1)+" and "+str(num2)+" is "+str(sum)
    if ops=='divide':
     try:
        
            sum=num1/num2
            result= "the"+ops+" of "+str(num1)+" and "+str(num2)+" is "+str(sum)
     except Exception as e:
        result="You can divide any no. with zero "+ str(e)


    return render_template('results.html',result=result)

@app.route('/postman_data',methods=['POST'])
#This is  a method for testing our api using postman tool in return data into json key value format
def math_operation1():
    ops=request.json['operation']
    num1=int(request.json['num1'])
    num2=int(request.json['num2'])
    if ops=='add':
        sum=num1+num2
        result= "the "+ops+" of "+str(num1)+" and "+str(num2)+" is "+str(sum)
    if ops=='subtract':
        sum=num1-num2
        result= "the"+ops+" of"+str(num1)+" and "+str(num2)+" is "+str(sum)
    if ops=='multiply':
        sum=num1*num2
        result= "the "+ops+" of "+str(num1)+" and "+str(num2)+" is "+str(sum)
    if ops=='divide':
     try:
        
            sum=num1/num2
            result= "the"+ops+" of "+str(num1)+" and "+str(num2)+" is "+str(sum)
     except Exception as e:
        result="You can divide any no. with zero "+ str(e)


    return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
