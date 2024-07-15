import os
from BeemAfrica import SMS  # Import the SMS class directly
from BeemAfrica import Authorize
from dotenv import load_dotenv

load_dotenv()

def send_sms(recipients, message):
    Authorize(os.getenv("BEEM_API_KEY"), os.getenv("SECRET_KEY"))
    return SMS.send_sms(message, recipients, sender_id='INFO')



# import os
# from BeemAfrica import Authorize, SMS
# from dotenv import load_dotenv
# # Adjust the import statement to directly import the SMS class
# from BeemAfrica import SMS


# load_dotenv()

# def send_sms(recipients, message):
#     authorize = Authorize(os.getenv("BEEM_API_KEY"), os.getenv("SECRET_KEY"))
#     sms = SMS()  # Create an instance of the SMS class
#     sms.authorize(authorize)  # Authorize the SMS instance
#     return sms.send_sms(message, recipients, sender_id='INFO')