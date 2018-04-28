import sys, os
import subprocess
import urllib, optparse
from flask import Flask, jsonify, request, abort, make_response
import json
#from werkzeug.utils import secure_filename


###GLOBAL VARIABLES###############################
app = Flask(__name__)
##################################################
@app.route('/', methods=['GET'])
def hello_world():
	return jsonify('Hello World!- This Flask App is working!!')

#assumes parameter is encoded using quote_plus
@app.route('/getuid', methods=['GET'])

def getuid():

	if request.method == 'GET':
		#os.environ['PYTHON_PATH']=os.environ['PYTHON_PATH'] + ":" + os.path.join(os.getcwd(), "SimpleText", "nmt")
		uid = request.args.get('text')
		if(uid is None or uid ==''):
			abort(400)

		user_url = './testData/UserInfo/'+uid+'_user.json'
		rec_url = './testData/recom/'+uid+'_recom.json'
		with open(user_url) as user:
			u = json.load(user)
		with open(rec_url) as rec:
			r = json.load(rec)
		res = []
		res.append(u['profile']['nickname'])
		res.append(u['profile']['avatarUrl'])
		for i in range(10):
			res.append(r[i]['image'])
			res.append(r[i]['name'])
			res.append(r[i]['score'])
		# output = open(os.path.join('SimpleText', 'test', 'inference.txt')).readline()
		return jsonify(res)



@app.errorhandler(404) # resource not found
def error404(error):
	return make_response(jsonify({'error':'The requested endpoint does not exist'}),404)

@app.errorhandler(400) # payload too large
def error413(error):
	return make_response(jsonify({'error':'Invalid input string'}),400)


if __name__ == '__main__':
	default_host="127.0.0.1"
	default_port="5000"
	parser = optparse.OptionParser()
	parser.add_option("-H", "--host",
					  help="Hostname of the Flask app " + \
						   "[default %s]" % default_host,
					  default=default_host)
	parser.add_option("-P", "--port",
					  help="Port for the Flask app " + \
						   "[default %s]" % default_port,
					  default=default_port)

	# Two options useful for debugging purposes, but 
	# a bit dangerous so not exposed in the help message.
	parser.add_option("-d", "--debug",
					  action="store_true", dest="debug",
					  help=optparse.SUPPRESS_HELP)
	parser.add_option("-p", "--profile",
					  action="store_true", dest="profile",
					  help=optparse.SUPPRESS_HELP)

	options, _ = parser.parse_args()

	app.run(
		debug=options.debug,
		host=options.host,
		port=int(options.port)
	)