import requests


def send_telegram(text: str):
    token = "5906286565:AAF71BxPYkX6sWpgz1wGTdtyKlnffROO3zE"
    url = "https://api.telegram.org/bot"
    channel_id = "-1001858191181" #@SmartHouseChannel
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")
        pass


if __name__ == '__main__':
    send_telegram("hello world!")
