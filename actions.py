from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rasa_sdk.events import Restarted

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)

def RestaurantSearch(City,Cuisine,Budget):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	if (Budget=='low'):
		TEMP_new = TEMP.loc[(TEMP['Average Cost for two']<300)]
	elif (Budget=='mid'):
		TEMP_new = TEMP.loc[(TEMP['Average Cost for two']>=300)&(TEMP['Average Cost for two']<=300)]
	elif (Budget=='high'):
		TEMP_new = TEMP.loc[(TEMP['Average Cost for two']>700)]
	TEMP_new = TEMP_new.sort_values('Aggregate rating', ascending=False)
	return TEMP_new[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def sendmail(mailid,response):
	mail_content = response
	#The mail addresses and password
	sender_address = 'cupgrad@gmail.com'
	sender_pass = 'upgradaiml'
	receiver_address = mailid
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self,dispatcher,tracker,domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Budget=budget)
		response=""
		if type(results)==str:
			response=results
		else:
			if results.shape[0] == 0:
				response= "No results"
			else:
				for restaurant in RestaurantSearch(loc,cuisine,budget).iloc[:5].iterrows():
					restaurant = restaurant[1]
					response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
		dispatcher.utter_message(response)
		return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('budget',budget)]

class VerifyLocation(Action):
	WeOperate = []
	TIER = []
	def __init__(self):
		self.WeOperate = ['Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
		self.TIER = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune',
                       'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly',
                       'belgaum', 'secunderabad', 'rishikesh'
                       'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city',
                       'chandigarh',
                       'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad',
                       'firozabad',
                       'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur',
                       'hubli–dharwad',
                       'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi',
                       'jodhpur',
                       'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool',
                       'ludhiana', 'lucknow',
                       'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore',
                       'nagpur', 'nanded',
                       'nashik', 'nellore', 'noida', 'patna', 'puducherry', 'purulia', 'prayagraj', 'raipur', 'rajkot',
                       'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur',
                       'srinagar', 'surat',
                       'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara',
                       'varanasi',
                       'vasai-virar city', 'vijayawada', 'visakhapatnam', 'vellore', 'warangal', 'mohali', 'panchkula']
	def name(self):
		return "verify_location"
	
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		if loc.lower() not in self.TIER:
			dispatcher.utter_message("Sorry I cannot understand. Please try again")
			return [SlotSet('location', None), SlotSet("location_ok", False)]
		elif loc.lower() in self.TIER:
			if not (self.verify_location(loc)):
				dispatcher.utter_message("We do not operate in " + loc + " yet. Please try some other city.")
				return [SlotSet('location', None), SlotSet("location_ok", False)]
			else:
				return [SlotSet('location', loc), SlotSet("location_ok", True)]
	
	def verify_location(self,loc):
		self.WeOperate=[x.lower() for x in self.WeOperate]
		return loc.lower() in self.WeOperate

class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Budget=budget)
		response=""
		if results.shape[0] == 0:
			response= "No results"
		else:
			for restaurant in RestaurantSearch(loc,cuisine,budget).iloc[:10].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
		MailID = tracker.get_slot('email')
		sendmail(mailid=MailID,response=response)
		dispatcher.utter_message("-----"+"Email sent. Thank you!")
		return [SlotSet('email',MailID)]

class ActionRestarted(Action):
    def name(self):
        return 'action_restart'
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Hello again! I have been restarted. How may I help you?")
        return [Restarted()]