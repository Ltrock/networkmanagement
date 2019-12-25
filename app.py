from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/router/')

def router():

    return render_template('router.html')

@app.route('/L2switch/')

def L2switch():

    return render_template('L2switch.html')

@app.route('/L3switch/')

def L3switch():

    return render_template('L3switch.html')



@app.route('/member/')

def member():

    return render_template('member.html')

if __name__ == '__main__':

    app.run(debug=True)