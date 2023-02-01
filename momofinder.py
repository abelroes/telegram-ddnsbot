import os
import logging
from urllib import request, parse


if __name__ == "__main__":

    MOMO_FINDER_BOT_TOKEN = os.getenv("MOMO_FINDER_BOT_TOKEN")
    TELEGRAM_GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")

    if MOMO_FINDER_BOT_TOKEN and TELEGRAM_GROUP_ID:
    
        TELEGRAM_URL_SEND_MSG = f"https://api.telegram.org/bot{MOMO_FINDER_BOT_TOKEN}/sendMessage"

        external_ip = request.urlopen("https://ident.me").read().decode("utf8")

        LAST_IP_FILE = "last_ip.txt"
        LAST_IP = ""
        
        file = open(LAST_IP_FILE, "r")
        LAST_IP = file.read()
        file.close()

        if LAST_IP != external_ip:
            text_content = f"O novo IP do MomoFlix é: {external_ip}:8096"
            payload = {
                "chat_id":TELEGRAM_GROUP_ID,
                "text":text_content,
            }

            data = parse.urlencode(payload).encode()
            request.urlopen(request.Request(TELEGRAM_URL_SEND_MSG, data=data))

            file = open(LAST_IP_FILE, "w")
            file.write(external_ip)
            file.close()
    
    else:
        logging.error("Couldn't find envvars")
