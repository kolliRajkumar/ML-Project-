from flask import Flask

app =Flask(_name_);



@app.route('/', methods=['GET', 'POST'])
def index():
    return "Starting a new Machine Learning Project"



if _name_ == "_main_":
    app.run(debug=True)
