from crypt import methods
import imp, os, json, pandas
import re
from json.tool import main
from unicodedata import name
from flask import Flask, render_template, Blueprint, send_file


result = Blueprint('result', __name__)

def analysis():
	os.chdir("Orthrus")
	os.system("python3 orthrus.py --tool slither --dataset my_contracts")

	#switch to results
	os.chdir("results")
	#mythril
	a = sorted(os.listdir("mythril"))
	c = a[-1]
	d = []
	for i in os.walk(f"mythril/{c}"):
		for j in i:
			if 'result.json' in j:
				d.append(i[0])

	e = []
	for k in d:
		myjsonfile = open(f"{k}/result.json","r")
		jsondata = myjsonfile.read()
		mythril_results = json.loads(jsondata)
		e.append(mythril_results)

	#slither
	b = sorted(os.listdir("slither"))
	f = b[-1]
	g = []
	for i in os.walk(f"slither/{f}"):
		for j in i:
			if 'result.json' in j:
				g.append(i[0])

	h = []
	for l in g:
		myjsonfile = open(f"{l}/result.json","r")
		jsondata = myjsonfile.read()
		slither_results = json.loads(jsondata)
		h.append(slither_results)
	
	for i in h:
		for j in i['analysis']:
			if j['check'] == 'reentrancy-eth':
				j['description'] += '. Reentrancy occurs when external contract calls are allowed to make new calls to the calling contract before the initial execution is complete. In the reentrancy attack, a malicious contract calls back into the calling contract before the first invocation of the function is finished. This may cause the different invocations of the function to interact in undesirable ways, including the draining of funds.'
			
			if j['check'] == 'solc-version':
				j['description'] += '. Using very old versions of Solidity prevents benefits offered by bug fixes and newer security checks. Using the latest versions might make contracts susceptible to undiscovered compiler bugs. Consider using one of these solidity versions: 0.7.5, 0.7.6 or 0.8.4.'

			if j['check'] == 'arbitrary-send':
				j['description'] += ". The user approves the contract to spend thei ERC20 tokens. An attacker can call and specify the users address as the from parameter in transferFrom, transferring the user's tokens to themself."
			
			if j['check'] == 'deprecated-standards':
				j['description'] += '. Consider replacing the deprecated symbols.'
			
			if j['check'] == 'suicidal':
				j['description'] += '. Due to insufficient access controls, malicious parties can cause the contract to self-destruct. Consider removing the self-destruct functionality unless absolutely required.'
			
			if j['check'] == 'calls-loop':
				j['description'] += '. DoS attack for smart contracts. The gas price of the looped calls increases exponentially and quickly goes beyond the maximum allowed gas price, causing the smart contract to stop running.'
			
			if j['check'] == 'timestamp':
				j['description'] += '. Built-in time dependencies can be exploited by malicious miners.'

	
	os.chdir("/home/savit/Dashboard")

	return h
 
@result.route("/results", methods=['POST', 'GET'])
def slitherresults():
		data = analysis()
		os.chdir("Orthrus/dataset/my_contracts")
		results = pandas.ExcelWriter('results.xlsx')
		for i in data:
			df = pandas.DataFrame(data=i['analysis'])
			df.to_excel(results, sheet_name=f"{i['contract']}")
			results.save()
		os.chdir("/home/savit/Dashboard/flaskblog")
		return render_template("slither.html", slither_results=data)

@result.route("/download", methods=['POST', 'GET'])
def download_results():
	path = "/home/savit/Dashboard/Orthrus/dataset/my_contracts/results.xlsx"
	return send_file(path, as_attachment=True)
