import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6473880018:AAHex4RTkoTPgTuMGYQSNUj8Tz4qywIc8Lk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJ8Bu0jSujAzw5Upuqmx_cLaqCELq_2wj3752-0n9gPd4qXS-Bo6mBMcXUA9RaNdfpj5VTJk5OJLYo1qmYSq1rvVA-fqpSQRti0IniyG4exTbO_fi4we6NQ1aOBA31fPsoFFqjvOO6Lfjdo8yqymPBEYd3uXx8fs11mYdbsaQ02BI4qztQtWLrHjH-DmPgR1qQOHT2jBjGt9H0AmPltPctFxDTl5Ndq3IJN_5jIK3JKnguF8fMdMM11yg-dsRtcKCGWg6GeV2TPM-FOfAtkNJnCwIki_lrBzoAGPk3BA_7kT9b6a-YA73175hZCfgQ-4dpYMBCJIajOh_PbHANx_E3Vyag0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
