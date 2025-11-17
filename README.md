# tele-watch

*tele-watch.py is a Telegram group monitor written in Python 3. Tele_watch is designed to be ran on a Linux server. After running the program on your server any new messages from within your Telegram groups will be sent to your Slack channel via a webhook.*

## Basic Set-up:

***In order to use tele_watch.py you must have the following***

### Slack
---

* *Slack Account with your own channel* 
* *Slack webhook*
   * *In order to obtain you Slack webhook you must create a Slack app and enable incoming webhooks in the settings*
   * *After creating your Slack app add a new wehook config to post to your channel*

### Telegram
---

* Telegram account
* You need to Join the groups you want updates from

### Host
---
*Tele_watch.py is designed to work on a Linux server. You do not need anythng expensive as a cheap Digital Ocean droplet will work fine. The script is going to be running 24/7 so running this on your personal computer will not be optimal.*

### Server Set-Up:
---

* **After choosing your run location on our server clone this repository**
  * ***https***: `git clone https://github.com/discon3ct/tele-watch.git`
  * ***SSH***: `git clone git@github.com:discon3ct/tele-watch.git`
* **Create a Python Virtual Environment so you avoid any dependency conflicts**
  * ***create the venv***: `python3 -m venv <environment name>`
  * ***activate the venv***: `source env/bin/activate`
* **Install required dependencies**
    * `pip install -r requirements.txt`
* **Create required environment variables and include in .env or variable/secret management of your choice (must fix code to use manager of your choice)**
	* tele_watch.py
 	  * ***Telegram*** - *API ID, API Hash, Phone, and Channels Joined*
      * ***Slack*** - *Webhook*
    * init.sh
      * ***Path where your python venv was created***
      * ***Path to where you put tele_watch.cpy***
         
### Running program:
---

>Do to the fact that telegram must confirm you through the app you must run tele_watch.py as follows:

1. ***run tele_watch.py. wait till you enter your conformation code and then exit the program with "Ctrl C"***
2. ***You will now have a session file, run init.sh.***
3. ***That's it your done and the tele_watch.py process is running in the background.***

***To check that tele_watch.py is running you can run the following command:***
* `ps -ef | grep python'

***To kill the tele_watch.py process use the following command***
* `kill <PID of tele_watch.py>`

***For a more detailed and step-by-step setup process you can refer to the Wiki***




