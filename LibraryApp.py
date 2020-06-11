import pandas as pd
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def CCPL_Events(): # don't forget to redefine every new return command!
    items = pd.read_csv('CCPL_Events_Info.csv') #Click on the file path and tap on 'copy filename as pathname'.
    return items.to_html()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
