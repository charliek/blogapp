from flask import Flask

app = Flask(__name__)

# This must remain at the bottom of this file to avoid a circular dependency
import blogapp.views
