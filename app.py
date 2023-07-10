from flask import *
import pyrebase
# from flask import Flask, render_template, request

config = {
    "apiKey": "AIzaSyDaI7cZZqJddKixCymqu7bfGlZRIief2hs",
    "authDomain": "geeky-nerds.firebaseapp.com",
    "databaseURL": "https://geeky-nerds-default-rtdb.firebaseio.com",
    "projectId": "geeky-nerds",
    "storageBucket": "geeky-nerds.appspot.com",
    "messagingSenderId": "427087123086",
    "appId": "1:427087123086:web:7e5381b05994ec84aeafdf",
    "measurementId": "G-P95P6QT18Q"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def basic():

    if (request.method == 'GET'):
        data = db.child("data").get()
        return jsonify(data.val()), 200

    if (request.method == 'POST'):
        if (request.form['submit'] == 'add'):
            try:
                product_name = request.form.get('product_name')
                owner_name = request.form.get('owner_name')
                owner_email = request.form.get('owner_email')
                image_link = request.form.get('image_link')
                description = request.form.get('description')
                buy_value = request.form.get('buy_value')
                sell_value = request.form.get('sell_value')
                print(product_name, owner_name, owner_email, image_link, description, buy_value, sell_value)
                object = {
                    product_name: product_name ,
                    owner_name: owner_name,
                    owner_email: owner_email,
                    image_link: image_link,
                    description: description,
                    buy_value: buy_value,
                    sell_value: sell_value
                }
                print('OBJECT===', object)
                db.child("data").push(object)
                print('DB===', db)
                data = db.child("data").get()
                to = data.val()
                print('TO===', to)
                # return jsonify(to), 200
                return '<h1>Data Added successfully!!!</h1>'
            except:
                return '<h1>invalid credentials!</h1>'
            # elif (request.form['submit'] == 'delete'):
            #     db.child("data").remove()
            # return render_template('index.html')
        # return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
