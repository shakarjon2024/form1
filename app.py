from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        ism = request.form.get('ism')
        familiya = request.form.get('familiya')
        return f"<h2>Salom, {ism} {familiya}!</h2><br><a href='/'>Bosh sahifaga</a>"
    return render_template('form1.html')

if __name__ == '__main__':
    app.run(debug=True)
