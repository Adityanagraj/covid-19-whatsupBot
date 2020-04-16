from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World i am aditya!"

@app.route("/sms", methods=['POST'])
def sms_reply():
	"""Respond to incoming calls with a simple text message."""
	# Fetch the message
	incoming_msg = request.values.get('Body', '')
	#print(incoming_msg)
	resp = MessagingResponse()
	msg = resp.message()
	responded = False


	if 'Hi' in incoming_msg or 'Hey' in incoming_msg or 'hi' in incoming_msg or 'ನಮಸ್ಕಾರ' in incoming_msg or 'नमस्ते' in incoming_msg:
		text = f'Welcome 🙏, \nThis is a Covid-19 BOT developed by Blackhat team to provide latest information updates i.e stay home stay safe.\n For any emergency \n Helpline: 011-23978046 | Toll-Free Number: 1075 \n ✉ Email: ncov2019@gov.in \n\n Please enter one of the following option 👇 \n *1* Covid-19 statistics *INDIA*. \n *2*. How does it *Spread*? \n *3*. *Preventive measures* to be taken.\n *4*. *further info*'
		msg.body(text)
		responded = True
	if '1' in incoming_msg:
		r = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
		if r.status_code == 200:
	
		
				data=r.json()
				text = f'_Covid-19 Cases INDIA_🇮🇳 \n\n🛑Total : {data["data"]["summary"]["total"]} \n\n🛑ConfirmedCasesIndian : {data["data"]["summary"]["confirmedCasesIndian"]}\n\n🛑Discharged : {data["data"]["summary"]["discharged"]}\n\n🛑Deaths : {data["data"]["summary"]["deaths"]}'
				msg.body(text)
				responded = True 
	if '2' in incoming_msg:	
		text=f'👉 The new coronavirus is a respiratory virus which spreads primarily through droplets generated when an infected person coughs or sneezes, or through droplets of saliva or discharge from the nose. To protect yourself, clean your hands frequently with an alcohol-based hand rub or wash them with soap and water.'
		msg.body(text)
		responded = True 

	if '3' in incoming_msg:
		text=f'*1* *STAY* home\n*2* *KEEP* a safe distance\n*3* *WASH* hands often\n*4* *COVER* your cough\n*5* *SICK*?Call the helpline'
		msg.body(text)
		responded = True

	if '4' in incoming_msg:
		text=f'https://www.mohfw.gov.in/'
		msg.body(text)
		responded = True
		
		 
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)