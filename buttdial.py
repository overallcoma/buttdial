from twilio.rest import Client
import datetime
import time
import random
from configparser import ConfigParser

configfilename = "./buttdial.cfg"

configinfo = ConfigParser()
try:
    configinfo.read(configfilename)
except:
    print("Could not read config file")
try:
    xmlscript = configinfo["serverconfig"]["xmlscript"]
except:
    print("Could not get xml script value")
try:
    account_sid = configinfo["twilioconfig"]["account_sid"]
except:
    print("Could not get account sid value")
try:
    auth_token = configinfo["twilioconfig"]["auth_token"]
except:
    print("Could not read auth token")
try:
    numberlistimport = configinfo["twilioconfig"]["numberlist"]
    numberlist = numberlistimport.split()
except:
    print("Could not read number list")

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", dest="targetnumber", help="Target Number")
parser.add_argument("-s", "--sleeptime", type=int, dest='sleeptime', help="Sleep time between calls (Default 10s)")
parser.add_argument("-r", "--record", dest="recordswitch", help="Turn off recording (default is true")
parser.add_argument("-l", "--loopcalls", help="Run calls on an repeating loop", action="store_true")
args = parser.parse_args()

if args.targetnumber:
        targetnumber = args.targetnumber
else:
    exit("Target Number is required")
if args.sleeptime:
    sleeptime = args.sleeptime
else:
    sleeptime = 10
if args.recordswitch:
    recordtf = "false"
else:
    recordtf = "true"
if args.loopcalls:
    runonloop = True
else:
    runonloop = False

client = Client(account_sid, auth_token)


def makecall():
    call = client.api.account.calls \
        .create(to=targetnumber,
                from_=number,
                url=xmlscript,
                record=recordtf)
    timenow = datetime.datetime.now()
    print("{time}: Calling {destination} from {source}").format(time=timenow, destination=targetnumber, source=number)
    time.sleep(sleeptime)
    return


if runonloop:
    while True:
        try:
            number = (random.choice(numberlist))
            makecall()
        except KeyboardInterrupt:
            break
    print("Exiting Loop")

else:
    for number in numberlist:
        try:
            makecall()
        except KeyboardInterrupt:
            break
    print("Exiting Loop")

exit("Script Complete")