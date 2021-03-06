#!/usr/local/bin/python
# deploy.py: Deploy Multiple VM's from csv on github
# Version 2.1
# uses sshpass + gdocs

import csv
import os
import requests



# ===========================================================================================================================================
# VARS - Please modify this section as you require
# ===========================================================================================================================================
gsheet_id = '1rLuyFzzxZw9cDX2FMkpt8Jr1HnaJFTNxYFdVokYuthY' # Enter Google Sheet ID - TO BE USED LATER
gsheet_name = 'Sheet1' # sheet name
xmr_addy = 'XMR_ADDY' # Please make sure to set your XMR Address here
# ===========================================================================================================================================
# ===========================================================================================================================================



# ===========================================================================================================================================
# Do not edit below this line
# ===========================================================================================================================================

url = 'https://docs.google.com/spreadsheets/d/' + gsheet_id + '/gviz/tq?tqx=out:csv&sheet=' + gsheet_name
base_install_cmd = "'curl -s -L https://raw.githubusercontent.com/TheCookies/MO-Miner/master/start.sh | bash -s " + xmr_addy + "'"
print("Downloading csv from: ", url, " Please make sure this file is up to date!")
req = requests.get(url)
url_content = req.content
csv_file = open("list.csv","wb")
csv_file.write(url_content)
csv_file.close()
print("File Has been downloaded and saved to your computer!")


print("Processing The CSV file")
print("we will be installing the miner with the following command :", base_install_cmd)
with open('list.csv', 'r') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:

        print('Connecting to VM - IP Address: ', row['ip'], ' Username: ', row['user'], ' Password: ', row['pass'])
        install_cmd = "sshpass -p " + row['pass'] + " ssh -o StrictHostKeyChecking=no " + row['user'] + "@" + row['ip'] + " " + base_install_cmd
        try:
            returned_value = os.system(install_cmd)
        except:
            continue


        print("="*50, install_cmd, "="*50)
        print('VM been completed and xmrig has started')
            
# TODO: Delete CSV file after, but fuck it i'm lazy

# ===========================================================================================================================================
# ===========================================================================================================================================
