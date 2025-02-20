from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def mane():

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

@app.route('/history3')
def history3():
    return render_template("untitled-3.html")

@app.route('/history4')
def history4():
    return render_template("untitled-4.html")

@app.route('/history5')
def history5():
    return render_template("untitled-5.html")

@app.route('/history51')
def history51():
    return render_template("untitled-5-1.html")

@app.route('/history6')
def history6():
    return render_template("untitled-6.html")

@app.route('/history61')
def history61():
    return render_template("untitled-6-1.html")

@app.route('/history62')
def history62():
    return render_template("untitled-6-2.html")

@app.route('/history621')
def history621():
    return render_template("untitled-6-2-1.html")

@app.route('/history7')
def history7():
    return render_template("untitled-7.html")

@app.route('/history71')
def history71():
    return render_template("untitled-7-1.html")

@app.route('/history72')
def history72():
    return render_template("untitled-7-2.html")

@app.route('/history721')
def history721():
    return render_template("untitled-7-2-1.html")

@app.route('/history8')
def history8():
    return render_template("untitled-8.html")

@app.route('/history81')
def history81():
    return render_template("untitled-8-1.html")

@app.route('/history9')
def history9():
    return render_template("untitled-9.html")

@app.route('/history91')
def history91():
    return render_template("untitled-9-1.html")

@app.route('/history93')
def history93():
    return render_template("untitled-9-3.html")

@app.route('/history94')
def history94():
    return render_template("untitled-9-4.html")

@app.route('/history942')
def history942():
    return render_template("untitled-9-4-2.html")

@app.route('/history9421')
def history9421():
    return render_template("untitled-9-4-2-1.html")

@app.route('/history94211')
def history94211():
    return render_template("untitled-9-4-2-1-1.html")

@app.route('/history943')
def history943():
    return render_template("untitled-9-4-3.html")

@app.route('/history944')
def history944():
    return render_template("untitled-9-4-4.html")

@app.route('/history945')
def history945():
    return render_template("untitled-9-4-5.html")

@app.route('/history10')
def history10():
    return render_template("untitled-10.html")












if __name__ == '__main__':
    app.run()
