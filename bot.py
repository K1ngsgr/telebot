from telegram import Bot
from config import BOT_TOKEN, CHANNEL_USERNAME
from fetch_sofascore import fetch_live_tennis_matches
import schedule
import time

bot = Bot(token=BOT_TOKEN)
sent_ids = set()

def post_live_matches():
    matches = fetch_live_tennis_matches()
    for match in matches:
        if match['id'] not in sent_ids:
            msg = f"🎾 {match['tournament']} – {match['match']}
📊 Status: {match['score']}"
            bot.send_message(chat_id=CHANNEL_USERNAME, text=msg)
            sent_ids.add(match['id'])

schedule.every(2).minutes.do(post_live_matches)

print("🤖 Bot is running...")

while True:
    schedule.run_pending()
    time.sleep(1)
