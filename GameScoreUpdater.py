#C:\Python37\python.exe C:\Python37\Scripts\prog\Game-Score-Updater\GameScoreUpdater.py
# -*- coding:utf-8 -*-
import requests
import smtplib
import sys
import time
from bs4 import BeautifulSoup

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
ChosenTeam = "" #selected team here
server.login( '', '' ) #email user/pass here

def loop(GameIndex,CheckMsg,msg):
	while True:
		read = requests.get('https://www.cbssports.com/nba/scoreboard/', timeout = None)
		soup = BeautifulSoup(read.text, 'html.parser')
		results = soup.find_all(attrs={'class': 'ingame'})
		LengthStatus = len(results)		
		GameIndex += 1
		if GameIndex == LengthStatus: # reset GameIndex
			GameIndex = 0
		if LengthStatus == 0:
			print("No current games")
		else:
			TempResults2 = TempResults1 = results[GameIndex]
			LengthTeam = len(TempResults1.find_all("a", string = ChosenTeam))
			if(LengthTeam == 0):
					print("Chosen team not playing")
			while LengthTeam > 0: # team found in list
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
					def negfive():
						msg = Team + " down by at least 5 pts \U0001F610"
						return msg
					def negten():
						msg = Team + " down by at least 10 pts \U0001F610"	
						return msg
					def negtwenty():
						msg = Team + " down by at least 20 pts \U0001F62D"
						return msg
					def upfive():
						msg = Team + " up by at least 5 pts \U0001F44C"	
						return msg
					def upten():
						msg = Team + " up by at least 10 pts \U0001F919"
						return msg
					def uptwenty():
						msg = Team + " up by at least 20 pts \U0001F600"
						return msg
					def close():
						msg = Team + " +/- 4 pts, it's close \U0001F525"						
						return msg
					def even():
						msg = "Tie Game!!! \U0001F525 \U0001F525 \U0001F525"
						return msg
					Number = {
								'-1' : close,
								'-2' : close,
								'-3' : close,
								'-4' : close,						
								'-5' : negfive,
								'-6' : negfive,
								'-7' : negfive,
								'-8' : negfive,
								'-9' : negfive,
								'-10' : negten,
								'-11' : negten,
								'-12' : negten,
								'-13' : negten,
								'-14' : negten,
								'-15' : negten,
								'-16' : negten,
								'-17' : negten,
								'-18' : negten,
								'-19' : negten,
								'-20' : negtwenty,
								'-21' : negtwenty,
								'-22' : negtwenty,
								'-23' : negtwenty,
								'-24' : negtwenty,
								'-25' : negtwenty,
								'-26' : negtwenty,
								'-27' : negtwenty,
								'-28' : negtwenty,
								'-29' : negtwenty,
								'-30' : negtwenty,
								'0' : even,
								'1' : close,
								'2' : close,
								'3' : close,
								'4' : close,
								'5' : upfive,
								'6' : upfive,
								'7' : upfive,
								'8' : upfive,
								'9' : upfive,
								'10' : upten,
								'11' : upten,
								'12' : upten,
								'13' : upten,
								'14' : upten,
								'15' : upten,
								'16' : upten,
								'17' : upten,
								'18' : upten,
								'19' : upten,
								'20' : uptwenty,
								'21' : uptwenty,
								'22' : uptwenty,
								'23' : uptwenty,
								'24' : uptwenty,
								'25' : uptwenty,
								'26' : uptwenty,
								'27' : uptwenty,
								'28' : uptwenty,
								'29' : uptwenty,
								'30' : uptwenty
					}
					msg = Number[Subject]()
					if CheckMsg != msg:
						print(msg)
						try:
							server.sendmail('', '9166623460@vzwpix.com', msg.encode("utf-8"))
						except smtplib.SMTPSenderRefused:
							pass
						except smtplib.SMTPException:
							pass
						CheckMsg = msg
					else:
						print("no updates")
				try:
					read = requests.get('https://www.cbssports.com/nba/scoreboard/', timeout = None)
				except requests.ConnectionError:
					pass	
					
				soup = BeautifulSoup(read.text, 'html.parser')
				results = soup.find_all(attrs={'class': 'ingame'})
				TempResults2 = TempResults1 = results[GameIndex]
				LengthTeam = len(TempResults1.find_all("a", string = ChosenTeam))
				print(LengthTeam)
				time.sleep(10)
			GameIndex = 0 
try:
	loop(0,"null","")
except KeyboardInterrupt:
	print("Program Terminated")