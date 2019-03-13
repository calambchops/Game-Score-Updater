#C:\Python37\python.exe C:\Python37\Scripts\prog\Game-Score-Updater\GameScoreUpdater.py
# -*- coding:utf-8 -*-
import requests
import smtplib
import sys
import time
import Dictionary
from bs4 import BeautifulSoup


server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
ChosenTeam = "" #selected team here
server.login( '', '' ) #email user/pass here
url = 'https://www.cbssports.com/nba/scoreboard/'


def Request(website):
	try:
		read = requests.get(website, stream = True, timeout = None)
		soup = BeautifulSoup(read.text, 'html.parser')
		results = soup.find_all(attrs={'class': 'ingame'})
		return results
	except requests.ConnectionError:
		pass	



def Parse(Results,GameIndex):
	msg = ""
	results = Results
	LengthStatus = len(results)	
	print(LengthStatus)
	if LengthStatus == 0:
		print("No current games")
		return null
	else:
		while LengthStatus > 0:
			try:
				TempResults1 = results[GameIndex]
				TempResults2 = TempResults1
				LengthTeam = len(TempResults1.find_all("a", string = ChosenTeam))
			except IndexError:
				pass
			if(LengthTeam == 1):
				ProgressTableResults = TempResults2.find_all('div', attrs={'class':'in-progress-table'})
				TdResults = ProgressTableResults[0]	
				TdFinalResults = TdResults.find_all('td')							
				Team1 = str(TdFinalResults[0].text)
				Team1Cleaned = Team1.strip().replace(' ', '').split()			
				Team2 = str(TdFinalResults[6].text)
				Team2Cleaned = Team2.strip().replace(' ', '').split()				
				Team1Score = int(TdFinalResults[5].text)		
				Team2Score = int(TdFinalResults[11].text)				
				if Team1Cleaned[0] == ChosenTeam:
					Differential = Team1Score - Team2Score
					Subject = str(Differential)
					Team = Team1Cleaned[0]
				elif Team2Cleaned[0] == ChosenTeam:
					Differential = Team2Score - Team1Score
					Subject = str(Differential)
					Team = Team2Cleaned[0]	
				if not(Differential > 30 or Differential < -30):						
					msg = Team + Dictionary.Number[Subject]()
					return msg
				GameIndex += 1 
			if GameIndex == LengthStatus:
				GameIndex = 0
			
			
def Send(Msg, CheckMsg):
	if Msg != CheckMsg:
		print(Msg)
		try:
			server.sendmail('', '', Msg.encode("utf-8"))
			CheckMsg = Msg
			return CheckMsg
		except smtplib.SMTPSenderRefused:
			pass
		except smtplib.SMTPException:
			pass
	else:
		print("no updates")
		return CheckMsg

		

CheckMsg = "null"
while True:
	Results = Request(url)
	Msg = Parse(Results, 0)
	CheckMsg = Send(Msg, CheckMsg)
	time.sleep(20)