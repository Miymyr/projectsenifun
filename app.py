from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def mane():
    return render_template("Главная итог.html")


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


@app.route('/advice/4')
def advice4():
    return render_template("советы 4.html")


@app.route('/advice/5')
def advice5():
    return render_template("советы 5.html")


@app.route('/advice/6')
def advice6():
    return render_template("советы 6.html")


@app.route('/history')
def history():
    return render_template("untitled-1010.html")


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
    return render_template("untitled-9-35.html")


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
    return render_template("untitled-10-1.html")


@app.route('/h')
def h():
    return render_template("h.html")


@app.route('/h0')
def h0():
    return render_template("h0.html")


@app.route('/h1')
def h1():
    return render_template("h1.html")


@app.route('/h2')
def h2():
    return render_template("h2.html")


@app.route('/h3')
def h3():
    return render_template("h3.html")


@app.route('/h4')
def h4():
    return render_template("h4.html")


@app.route('/h5')
def h5():
    return render_template("h5.html")


@app.route('/h6')
def h6():
    return render_template("h6.html")


@app.route('/h7')
def h7():
    return render_template("h7.html")


@app.route('/h8')
def h8():
    return render_template("h8.html")


@app.route('/h9')
def h9():
    return render_template("h9.html")


@app.route('/h10')
def h10():
    return render_template("h10.html")


@app.route('/h11')
def h11():
    return render_template("h11.html")


@app.route('/h12')
def h12():
    return render_template("h12.html")


@app.route('/h13')
def h13():
    return render_template("h13.html")


@app.route('/h14')
def h14():
    return render_template("h14.html")


@app.route('/h15')
def h15():
    return render_template("h15.html")


@app.route('/h16')
def h16():
    return render_template("h16.html")


@app.route('/h17')
def h17():
    return render_template("h17.html")


@app.route('/h18')
def h18():
    return render_template("h18.html")


@app.route('/h19')
def h19():
    return render_template("h19.html")


@app.route('/h20')
def h20():
    return render_template("h20.html")


@app.route('/h21')
def h21():
    return render_template("h21.html")


@app.route('/h22')
def h22():
    return render_template("h22.html")


@app.route('/h23')
def h23():
    return render_template("h23.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
