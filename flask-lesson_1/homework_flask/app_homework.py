from flask import Flask, render_template, url_for, request, redirect, abort
app = Flask(__name__)


vegetables = ['potato', 'carrot', 'cucumber', 'broccoli', 'onion']
fruits = ['apple', 'pinapple', 'banana', 'orange', 'citrus']


@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/')
def redirect_to_main():
    return redirect(url_for('main_page'))


@app.route('/fruits')
@app.route('/fruits/<string:value>', methods=['GET', 'POST', 'DELETE'])
def fruits_page(value=None):
    if request.method == 'POST':
        do_post(value)
        return "Successfully added a new value"
    if request.method == 'DELETE':
        do_delete(value)
        return "Successfully deleted the value"
    else:
        return do_get()


def do_post(value):
    return fruits.append(value)


def do_get():
    return render_template('fruits.html', values=fruits, name="a", title='fruits')


def do_delete(value):
    for i, elem in enumerate(fruits):
        if elem == value:
            fruits.pop(i)


@app.route('/vegetables')
@app.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
def vegetables_page(value=None):
    if request.method == 'POST':
        do_post_v(value)
        return "Successfully added a new value"
    if request.method == 'DELETE':
        do_delete_v(value)
        return "Successfully deleted the value"
    else:
        return do_get_v()


def do_post_v(value):
    return vegetables.append(value)


def do_get_v():
    return render_template('vegetables.html', values=vegetables, name="a", title='vegetables')


def do_delete_v(value):
    for i, elem in enumerate(vegetables):
        if elem == value:
            fruits.pop(i)
            
            
@app.route("/test_abort")
def test_abort():
    abort(501, "Our program has an error")


@app.errorhandler(501)
def error_501_handler(error):
    return render_template("error_501.html")



if __name__ == '__main__':
    app.run(debug=True)


