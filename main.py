import json
import requests
import yagmail

with open("./data/config.json", "r") as file:
    configs = json.load(file)
    sender = configs["sender"]
    password = configs["password"]
    recipient = configs["recipient"]
    headers = {"apikey": configs["apikey"]}


def get_rate():
    params = {"from": "HKD", "to": "IDR", "amount": "1"}
    url = f"https://api.apilayer.com/exchangerates_data/convert"
    response = requests.get(url, headers=headers, params=params)
    rate = response.json()["info"]["rate"]
    return rate


def send_email(rate):
    with yagmail.SMTP(sender, password) as yag:
        yag.send(to=recipient, subject="schedule", contents=str(rate))


def main():
    rate = get_rate()
    send_email(rate)


if __name__ == "__main__":
    main()
