import sys
import os
import subprocess
import random
import time  
from winotify import Notification, audio#pip

from loguru import logger 
#from itertools import combinations


from phishingmail import phishmail
from AuthorisedMail import authomail
from SuspectLinks import suslinks
from WordsPhrases import Words, Phrases
#______________________________________________________________________________#

def descripor():
    print("")
    print(".......................")
    print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")

def EmailSender():
    print("")
    print("________________________")
    print("")
    print("    DETECTED EMAILS")
    print("________________________")
    
def words():
    print("")
    print("________________________")
    print("")
    print("    DETECTED WORDS")
    print("________________________")

def phrases():
    print("")
    print("________________________")
    print("")
    print("    DETECTED PHRASES")
    print("________________________")

def URL():
    print("")
    print("________________________")
    print("")
    print("    DETECTED LINKS")
    print("________________________")
#______________________________________________________________________________#

 
def Domnotification():
    toast = Notification(app_id= "Spear AntiPhishing Software©",
                         title = "Suspicious Content Detected",
                         msg = "Scan Has Detected Phishing Emails",
                         duration = "short",
                         icon = r"C:\Users\Abdurr\Pictures\alert.png")
    toast.set_audio(audio.Default , loop= False)
    toast.show()                         

def Linknotification():
    toast = Notification(app_id= "Spear AntiPhishing Software©",
                         title = "Suspicious Content Detected",
                         msg = "Scan Has Detected Phishing Links",
                         duration = "short",
                         icon = r"C:\Users\Abdurr\Pictures\alert.png")
    toast.set_audio(audio.Default , loop= False)
    toast.show()
    

def Domaincount(filename,listdomain,authdomain):
    try:
        file = open(filename,"r")
        read = file.readlines()
        file.close()
        
        for word in listdomain:
            lower= word
            count = 1
            alert =("!")
            Talert = ("!")
            
            for sentance in read:
                line = sentance.split()
                for each in line:
                    line2 = each.lower()
                                                              
                    if lower == line2:    
                        count += 2
                        
            if count == 3:
                print("Phishing Email Found:")
                print((Talert),":",lower,)
                Domnotification()
                 
                
        for word in authdomain:
             lower= word.lower()
             count =0
             alert =("✔")
             
             for sentance in read:
                 line = sentance.split()
                 for each in line:
                     line2 = each.lower()
                                                               
                     if lower == line2:
                              
                         count +=1
             if count >= 1:
                  print("")
                  print("Authorised Domain Found:")
                  print((alert),":",lower,)
                                  
                  
              
    except FileExistsError:
        print("The file is not there")
    except FileNotFoundError :
        print("Unable to retrieve content")        
        print("Error Code f",(random.randint(530, 780)),": Incorrect File Name")





def wordcount(filename,listwords):
    try:
        file = open(filename,"r")
        read = file.readlines()
        file.close()
        
        for word in listwords:
            lower= word.lower()
            count =0
            alert =("!")
            Talert = ("!!")
            
            for sentance in read:
                line = sentance.split()
                for each in line:
                    line2 = each.lower()
                                                              
                    if lower == line2:
                             
                        count +=1
           
                 
            if count >= 1 and count < 3:
                print((alert),":",lower,":","[",count,"]")
                   
            if count >= 3:
                print((Talert),":",lower,":","[",count,"]")           
           
                
    except FileExistsError:
        print("The file is not there")
    except FileNotFoundError :
         print("Unable to retrieve content")        
         print("Error Code f",(random.randint(530, 780)),": Incorrect File Name")       




def phrasecount(filename,mainbody):
    try:
        Talert = ("!")
        with open(filename, 'r') as f:
            read = f.read()
        for word in mainbody:
            word.lower()
            if word in read:
                print((Talert),':','"',word,'"','found in email body')
            #notification()
            
                
    except FileExistsError:
         print("The file is not there")
    except FileNotFoundError :
         print("Unable to retrieve content")        
         print("Error Code f",(random.randint(530, 780)),": Incorrect File Name")    


def Links(filename,phishlink):
    try:
        Talert = ("!")
        with open(filename, 'r') as f:
            read = f.read()
        for link in phishlink:
            if link in read:
                print((Talert),':',link,)
                Linknotification()
            
            
                
    except FileExistsError:
         print("The file is not there")
    except FileNotFoundError :
          print("Unable to retrieve content")        
          print("Error Code f",(random.randint(530, 780)),": Incorrect File Name")

#______________________________________________________________________________#
os.system("mode con cols=66 lines=40")
print("")
print("  <<<<<<<<<<<<<<<</ \>>>>>>>>>>>>>>>>")
print("       SPEAR ANTIPHISHING SOFTWARE     ")
print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")
username = os.environ.get('USERNAME')
if username =='Abdurr':
    print("Validated Staff User:",os.getlogin())
    print("Role: Head Of Accounting")# Retrieve Role
    print("Retrieving Relevent Directories...")
    print("")# Retrieve Credentials from server
    time.sleep(2)
    print("Enter the desired file name:") 
    emailfile = input()
    print("Scanning: ",emailfile)
    time.sleep(1)
    EmailSender()
    Domaincount(emailfile,phishmail,authomail)
    time.sleep(1)
    words()        
    wordcount(emailfile,Words)
    time.sleep(1)
    phrases()
    phrasecount(emailfile,Phrases)
    time.sleep(1)
    URL() 
    Links(emailfile,suslinks)
    descripor()

    print("Scan Another File?   Y / N")
    restart = input().upper()
    if restart == "Y":
               subprocess.call([sys.executable, 'Antiphishing Software 1.5.py'])
        
    if restart == "N":
        print("Closing...")
        time.sleep(2)
        sys.exit   
    
else:
    print("Invalid Credentials Detected")
