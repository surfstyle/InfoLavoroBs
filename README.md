
# InfoLavoroBs
Web scraping and notification for [https://informalavoro.comune.brescia.it](https://informalavoro.comune.brescia.it)  
The site is updated every week (es. friday) with a working bulletin  
The goal is having a notification of the jobs from the bulletin that match a list of personal keywords.  
  
*Example:  
my-keywords=['informatica', 'develop', 'programmazione']  
Generate a notification (email) of all the lines that contains these keys*
  
  

## What is doing?
- A personalized web scraping script for the website (at this time the jobs on page 'Concorsi')
- A cron is used for starting the script (one time a week)  
- Scrap all the interested data on the webpage and save it on files  
- Search the files for the lines that match the keys
- Notify with an email the lines with changes  




## How to use it
#### Dependencies
Install Selenium to simulate a browser
<pre>
pip install selenium	
</pre>
  

#### Create a .env file
Create in the main folder a file .env  
like this  

<pre>
# .env

# General
APP_PATH=/home/headless/Scripts/InfoLavoroBs/
APP_URL=https://informalavoro.comune.brescia.it
APP_FILE_NAME=bollettino-informalavorobs-concorsi.txt
APP_FILE_OUTPUT=bollettino-informalavorobs-risultati.txt

# Email
APP_SMTP_SERVER=smtp.gmail.com
APP_SMTP_PORT=587
APP_DESTINATARIO=destination@gmail.com
APP_MITTENTE=myaddress@gmail.com
APP_SOGGETTO=[HomeSrv] Concorsi Informalavoro BS
APP_SMTP_USERNAME=myaddress@gmail.com
APP_SMTP_PASSWORD=xytzn aabb ccdd eeff
</pre>
  

#### Personalized the keywords in the search
Modify the list in *searchkeywords.py*
  

#### Run a test
<pre>
cd /home/user/my-home-script/
python3 start.py
</pre>
  
  
#### Personalize your cron file
*crontab -e*
  
<pre>
30 00 * * 6 python3 /home/headless/Scripts/InfoLavoroBs/start.py
</pre>

