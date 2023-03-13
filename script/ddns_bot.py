import os
import logging
from urllib import request, parse


if __name__ == "__main__":
    logging.info("Started DDNS Bot")
    SERVICE_NAME = os.getenv("SERVICE_NAME", default="Service")
    SERVICE_PORT = os.getenv("SERVICE_PORT")
    DDNS_BOT_TOKEN = os.getenv("DDNS_BOT_TOKEN")
    TELEGRAM_GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")

    if DDNS_BOT_TOKEN and TELEGRAM_GROUP_ID:
        TELEGRAM_URL_SEND_MSG = f"https://api.telegram.org/bot{DDNS_BOT_TOKEN}/sendMessage"

        external_ip = request.urlopen("https://ident.me").read().decode("utf8")

        script_dir = os.path.dirname(__file__)
        file_name = "last_ip.txt"
        LAST_IP_FILE = os.path.join(script_dir, file_name)
        
        file = open(LAST_IP_FILE, "r")
        last_ip = file.read()
        file.close()

        if last_ip != external_ip:
            text_content = f"Novo endereço de IP do {SERVICE_NAME}:\n`{external_ip}" + (f":{SERVICE_PORT}`" if SERVICE_PORT else "`")
            payload = {
                "chat_id":TELEGRAM_GROUP_ID,
                "text":text_content,
            }

            logging.info("Sending DDNS Bot Telegram request...")
            data = parse.urlencode(payload).encode()
            request.urlopen(request.Request(TELEGRAM_URL_SEND_MSG, data=data))
            logging.info("DDNS Bot Telegram request sent")

            file = open(LAST_IP_FILE, "w")
            file.write(external_ip)
            file.close()
    
    else:
        logging.error("Couldn't find envvars")
