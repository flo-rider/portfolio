from flask import Flask, render_template, url_for, request, redirect, session
import csv
app = Flask(__name__)
print(__name__)

'''
use this command to generate secret keys
python -c 'import secrets; print(secrets.token_hex())'
'''
app.secret_key = '8c7b1eac02ae6c354dfae7bd03412a0eaaff96afc541c4091830c8edddb968c0'

'''use the route() decorator to bind a function to a URL
equivalent to app.add_url_rule("/hello", view_func=hello_world
'''


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<page_name>")
def show_page(page_name=None):
    if 'name' in session:
        name=session['name'].upper()
    return render_template(f'{page_name}.html', name=name)

def write_to_csv(data):
    with open('database.csv') as database_to_read:
        with open('database.csv', mode='a', newline='') as database_to_write:
            fieldnames = ['name', 'email', 'subject', 'message']
            csv_writer = csv.DictWriter(database_to_write, fieldnames=fieldnames)

            # if file is empty, then add header
            if database_to_read.read(100) == "":
                csv_writer.writeheader()

            csv_writer.writerow(data)

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        session['name'] = data['name']
        write_to_csv(data)
        return redirect('thankyou')
    else:
        return 'something went wrong'

''' 
POWERSHELL
$env:FLASK_APP = "server.py" 
cd 'web server' 
flask run

$env:FLASK_ENV = "development"

'''