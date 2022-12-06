from flask import Flask
from controllers.index import index_page
from controllers.dashboard import dashboard_page
from dotenv import dotenv_values

app = Flask(__name__)

app.register_blueprint( dashboard_page,url_prefix = "/dashboard" )
app.register_blueprint( index_page )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6001, debug=True)
