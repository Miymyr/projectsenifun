from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def mane():
    a = "test"

    return render_template("Главная.html")

@app.route('/about')
def about():

    return render_template("info.html")

@app.route('/advice')
def advice():

    return render_template("советы.html")

@app.route('/advice/1')
def advice1():

    return render_template("советы-1.html")

@app.route('/advice/2')
def advice2():

    return render_template("советы-1-1.html")

@app.route('/advice/3')
def advice3():
    return render_template("советы-1-2.html")

@app.route('/history')
def history():
    return render_template("untitled.html")

@app.route('/history1')
def history1():
    return render_template("untitled-1.html")

@app.route('/history11')
def history11():
    return render_template("untitled-1-1.html")

@app.route('/history2')
def history2():
    return render_template("untitled-2.html")



if __name__ == '__main__':
    app.run()
