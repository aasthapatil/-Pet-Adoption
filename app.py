from flask import Flask,render_template,request
import pickle


app = Flask(__name__)

# from sklearn.externals import joblib
model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods = ['GET','POST'])
def pred():
    if request.method == 'POST':
        # try:
            params = request.form


            duration = int(params['duration'])
            color = int(params['color'])
            breed = float(params['breed'])
            x1 = int(params['x1'] )
            x2 = int(params['x2'])
            condition = int(params['condition'])
            height = int(params['height'])
            length = int(params['width'])


            # length, height = 0, 0
            result = model.predict([[condition,color, length, height,  x1, x2,breed,duration]])
            return render_template('result.html',result = result)
        # except:
        #     return render_template('index.html')

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
