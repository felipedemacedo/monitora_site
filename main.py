import requests
import mysql.connector
import os
# from selenium import webdriver
# from bs4 import BeautifulSoup


website_online_status = False
website_main_url = os.environ['WEBSITE_URL'] # "https://google.com/"
db_host = os.environ['DB_HOST']
db_password = os.environ['DB_PWD']

if __name__ == "__main__":    
    response = requests.get(website_main_url)

    if response.status_code == 200:
        website_online_status = True

    mydb = mysql.connector.connect(
    host=db_host, #"localhost",
    user="root",
    passwd=db_password, # "",
    database="monitoramento"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO logs (website_id, website_status) VALUES ((select id from websites where url like %s), %s)"
    val = (website_main_url, website_online_status)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
