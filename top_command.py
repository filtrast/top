import subprocess
from flask import Flask, render_template
import os

top_command = Flask(__name__)

@top_command.route("/")
def index():
	output = subprocess.check_output(['top', '-b', '-n1'])
	return output

if __name__ == "__main__":
	top_command.run(host="0.0.0.0", port=5000)


