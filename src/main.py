import json
# from datetime import datetime
from chat_downloader import ChatDownloader

URL = ""
INIT_AMOUNT = 0
OUTPUT_FILE_ROUTE = ""


def update_amount(amount: int):
    with open(file=OUTPUT_FILE_ROUTE, mode="w") as FILE:
        FILE.write(str(amount))


def log(chat):
    print(f"{chat['author']['name']}　{chat['money']['text']}　{chat['message']}")


def init_setting():
    global URL, INIT_AMOUNT, OUTPUT_FILE_ROUTE
    with open("./setting.json", mode="r") as setting_file:
        settings = json.load(setting_file)
        URL = settings['url']
        INIT_AMOUNT = settings['initial_amount']
        OUTPUT_FILE_ROUTE = settings['output_file_route']


if __name__ == "__main__":
    init_setting()

    downloader = ChatDownloader()
    # super_chats = downloader.get_chat(url=URL, output=f"./{str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))}.json", message_types=["paid_message"])
    super_chats = downloader.get_chat(url=URL, output=f"./res.json", message_types=["paid_message"])

    amount_count = INIT_AMOUNT

    for chat in super_chats:
        if chat['money']['currency'] == "TWD":
            amount_count += int(chat['money']['amount'])
            update_amount(amount_count)
        else:
            print("Not TWD.")

        log(chat=chat)
