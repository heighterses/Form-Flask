from flask import Flask, render_template, request
import smtplib

# <--------Email Credentials-------------
my_email = ""
password = ""

# <-------------App Code------------------


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def data_receive():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>name: {name}</h1>"


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/contact', methods=["POST"])
def contact_form():
    if request.method == 'POST':
        data = request.form
        name = (data["name"])
        email = (data["email"])
        message = (data["message"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=email,
                                to_addrs="binaftaba@gmail.com",
                                msg=f"Subject: 'Portfolio Message'\n\n Hello My NAME IS: {name}\nQuery: {message} ")

        return render_template('Form-Entered.html')


def sending_mail():
    pass


if __name__ == '__main__':
    app.run()
