#!/usr/bin/env python
import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
from bs4 import BeautifulSoup
import logging
import time

timestamp_long = datetime.now()
current_time = timestamp_long.strftime("%D %H:%M:%S")

file_object = open(r"/automater/url_checker/log.txt")

# Log File
file1 = open('/automater/url_checker/log.txt', 'a')

# Evaluation Senarios
evaluation_good = "Google: " + (current_time) + "\n"
evaluation_bad = "Google is down: " + (current_time) + "\n"
evaluation_except = "Google is neither up or down, except was hit on: " + (current_time) + "\n"


def e_mail():
        msg = EmailMessage()
        msg.set_content("A failover event has been detected on Google, at this moment in time a banner grab from Google fails to return a banner titled Google which is a clear indicator that Google is down")
        msg['Subject'] = "Google Down"
        msg['From'] = "123@aol.com"
        msg['To'] = "123@aol.com"
#       msg['Bcc'] = "123@aol.com", "", ""
        server = smtplib.SMTP("8.8.8.8")
        server.send_message(msg)
        server.quit()



def banner_grab():
        try:
                response = requests.get('https://8.8.8.8', verify=False)
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.title.string
                if title == "Google":
                        print("Google is up as of: ", current_time)
                        file1 = open('/automater/url_checker/log.txt', 'a')

                        # Writing a string to file
                        file1.write(evaluation_good)

                        # Closing file
                        file1.close()

                elif title != "Google":
                        print("Google is down as of: ", current_time)
                        file1 = open('/automater/url_checker/log.txt', 'a')

                        # Writing a string to file
                        file1.write(evaluation_bad)

                        # Closing file
                        file1.close()

                        # Send E-Mail
                        e_mail()

                        # Since we triggered the evaluation, sleep for 1 hours to prevent alert fatigue.
                        #time.sleep(3600)

        except Exception as e:
                print(e)
                file1 = open('/automater/url_checker/log.txt', 'a')

                # Writing a string to file
                file1.write(evaluation_except)

                # Closing file
                file1.close()

                # Send E-Mail
                e_mail()

                # Since we triggered the evaluation, sleep for 1 hours to prevent alert fatigue.
                #time.sleep(3600)

if __name__ == "__main__":
        banner_grab()
