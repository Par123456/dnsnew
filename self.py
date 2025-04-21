import os
try:
  import pyrogram
  import requests
except:
  os.system("pip install --upgrade pip && pip install pyrogram && pip install requests")
  import pyrogram
  import requests
import json
import sys
from pyrogram.raw import functions , base , types
from pyrogram import Client, filters, idle , errors ,enums
from pyrogram.types import Message , ChatPermissions
from pyrogram.raw import functions , base , types

api_id = 29042268 #  API ID
api_hash = "54a7b377dd4a04a58108639febe2f443" # HASH ID
app = Client("@AnishtayiN",api_id,api_hash)
admin = 6508600903 # ADMIN ID
 # به چیز دیگه ای دست نزنید #

if not os.path.isfile("Mode.json"):
 with open("Mode.json" , "w") as fjr:
  fjr.write('{"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0","mode_1": "0","mode_2": "0","mode_3": "0","mode_4": "0","mode_5": "0","mode_6": "0","mode_7": "0","mode_8": "0","mode_9": "0","mode_10": "0","mode_11": "0","mode_12": "0"}')
  fjr.close()

 with app:
  try:
    app.join_chat("@AnishtayiN")
    app.join_chat("@AnishtayiN")
  except:
    pass

with open("Mode.json", "r") as f:
    contents = f.read()
    data = json.loads(contents)

@app.on_message(filters.user(admin))
def admins(client , message):
 me = app.get_me()
 if message.text == ".help":
  app.edit_message_text(message.chat.id,message.id,f"""
پنل راهنمای @AnishtayiN :

`.s` → on / off => خط روی متن
`.b` → on / off => متن درشت
`.m` → on / off => منشن
`.sp` → on / off => اسپویلر
`.i` → on / off => خط کج
`.u` → on / off => خط زیر متن
`.c` → on / off => کپی با ضربه
`.p` → on / off => حالت PHP
`.h` → on / off => حالت HTML

`.gpt` → text => صحبت با هوش مصنوعی
`.arz` => دریافت نرخ ارز
`.time` => دریافت اطلاعات زمانی

`.fun1` => دستور فان 1
`.fun2` => دستور فان 2
`.fun3` => دستور فان 3
`.fun4` => دستور فان 4
`.fun5` => دستور فان 5
`.love` => دستور فان 6
`.dodol` => دستور فان 7
`.no` => دستور فان 8

`.ban` → reply or username or userid => بن کاربر ( فقط گروه )
`.unban` → reply or username or userid => حذف بن کاربر ( فقط گروه )
`.block` → reply or username or userid => مسدود کردن کاربر ( در پیوی )
`.unblock` → reply or username or userid => لغو مسدودیت کاربر
`.setname` → text => تنظیم نام
`.setname2` → text => تنظیم فامیلی
`.clearname2` => حذف فامیلی
`.setusername` → text => تنظیم یوزرنیم
`.setbio` → text => تنظیم بیوگرافی
`.clearbio` => حذف بیوگرافی
`.me` => دریافت اطلاعات اکانت خود
`.id` → reply or username or userid => دریافت اطلاعات کاربر مورد نظر


PARSA No1.  https://t.me/AnishtayiN
""")


 elif message.text.startswith(".s "):
  if message.text.split()[1] == "on":
   data.update({"strike": "1", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith(".b "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "1", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")


# اپن شده در افغانستان سورس

 elif message.text.startswith(".m "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "1", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")
# اپن شده در افغانستان سورس
 elif message.text.startswith(".sp "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "1", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith(".i "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "1", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")
# اپن شده در افغانستان سورس
 elif message.text.startswith(".u "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "1", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith(".c "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "1", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")
# اپن شده در افغانستان سورس
 elif message.text.startswith(".p "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "1", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith(".h "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

# اپن شده در افغانستان سورس

 elif message.text == ".restart":
  app.edit_message_text(message.chat.id, message.id,f"<b>❋ Restart The Self . . .</b>")
  python = sys.executable
  os.execl(python, python, *sys.argv)

 elif message.text == ".block" or message.text.startswith(".block "):
  app.block_user(message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1])
  app.edit_message_text(message.chat.id,message.id,f"**~ User Blocked**")

 elif message.text == ".unblock" or message.text.startswith(".unblock "):
  app.unblock_user(message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1])
  app.edit_message_text(message.chat.id,message.id,f"**~ User Unblocked**")

 elif message.text == ".ban" or message.text.startswith(".ban "):
   try:
    app.ban_chat_member(message.chat.id , (message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1]))
    app.edit_message_text(message.chat.id,message.id,f"**~ User Baned**")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

# اپن شده در افغانستان سورس

 elif message.text == ".unban" or message.text.startswith(".unban "):
  app.ban_chat_member(message.chat.id , (message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1]))
  app.edit_message_text(message.chat.id,message.id,f"**~ User Unbaned**")

 elif message.text.startswith(".setname "):
  app.edit_message_text(message.chat.id,message.id,f"**~ Your name was changed from ( `{me.first_name}` ) to ( `{message.text.replace('.setname','')[1::]}` )**")
  app.update_profile(first_name=message.text.replace(".setname","")[1::])
 
 elif message.text.startswith(".setname2 "):
  app.edit_message_text(message.chat.id,message.id,f"**~ Your Last name was changed from ( `{me.last_name}` ) to ( `{message.text.replace('.setname2','')[1::]}` )**")
  app.update_profile(last_name=message.text.replace(".setname2","")[1::])

 elif message.text == ".clearname2":
  app.edit_message_text(message.chat.id,message.id,f"**~ Your Last name is clear**")
  app.update_profile(last_name="")

 elif message.text.startswith(".setusername "):
   try:
    app.set_username(message.text.replace('.setusername','')[1::])
    app.edit_message_text(message.chat.id,message.id,f"**~ Your Last name was changed from ( `{me.username}` ) to ( `{message.text.replace('.setusername','')[1::]}` )**")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

 elif message.text.startswith(".setbio "):
   try:
    app.update_profile(first_name=me.first_name, bio=message.text.replace('.setbio','')[1::])
    app.edit_message_text(message.chat.id,message.id,f"**~ Your bio was changed to ( `{message.text.replace('.setbio','')[1::]}` )**")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")
# اپن شده در افغانستان سورس
 elif message.text == ".clearbio":
   app.update_profile(first_name=me.first_name, bio="")
   app.edit_message_text(message.chat.id,message.id,f"**~ Your bio is clear**")

 elif message.text == ".fun1":
  app.edit_message_text(message.chat.id,message.id,""" ⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")
  app.edit_message_text(message.chat.id,message.id,"""⠄⠄⠄⠄⠄⠄⠄⢸⣉⠉⠉⠄⢀⠈⠉⢏⠁⠄⠄
 ⠄⠄⠄⠄⠄⠄⡰⠃⠄⠄⠄⠄⢸⠄⠄⢸⣧⠄⠄
 ⠄⠄⠄⠄⠄⣼⣧⠄⠄⠄⠄⠄⣼⠄⠄⡘⣿⡆⠄
 ⠄⠄⠄⢀⣼⣿⡙⣷⡄⠄⠄⠄⠃⠄⢠⣿⢸⣿⡀
 ⠄⠄⢀⣾⣿⣿⣷⣝⠿⡀⠄⠄⠄⢀⡞⢍⣼⣿⠇
 ⠄⠄⣼⣿⣿⣿⣿⣿⣷⣄⠄⠄⠠⡊⠴⠋⠹⡜⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")
  app.edit_message_text(message.chat.id,message.id,"""⠄⠄⠘⣿⣿⣿⣦⣤⡀⢿⣿⣿⣿⣄⠄⠄⠄⠄⠄
 ⠄⠄⠄⠈⢿⣿⣿⣿⣿⣷⣯⣿⣿⣷⣾⣿⣷⡄⠄
 ⠄⠄⠄⠄⠄⢻⠏⣼⣿⣿⣿⣿⡿⣿⣿⣏⢾⠇⠄
 ⠄⠄⠄⠄⠄⠈⡼⠿⠿⢿⣿⣦⡝⣿⣿⣿⠷⢀⠄
 ⠄⠄⠄⠄⠄⠄⡇⠄⠄⠄⠈⠻⠇⠿⠋⠄⠄⢘⡆
 ⠄⠄⠄⠄⠄⠄⠱⣀⠄⠄⠄⣀⢼⡀⠄⢀⣀⡜⠄
⠄⠄⠄⠄⠄⠄⠄⢸⣉⠉⠉⠄⢀⠈⠉⢏⠁⠄⠄
 ⠄⠄⠄⠄⠄⠄⡰⠃⠄⠄⠄⠄⢸⠄⠄⢸⣧⠄⠄
 ⠄⠄⠄⠄⠄⣼⣧⠄⠄⠄⠄⠄⣼⠄⠄⡘⣿⡆⠄
 ⠄⠄⠄⢀⣼⣿⡙⣷⡄⠄⠄⠄⠃⠄⢠⣿⢸⣿⡀
 ⠄⠄⢀⣾⣿⣿⣷⣝⠿⡀⠄⠄⠄⢀⡞⢍⣼⣿⠇
 ⠄⠄⣼⣿⣿⣿⣿⣿⣷⣄⠄⠄⠠⡊⠴⠋⠹⡜⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")
# اپن شده در افغانستان سورس
  app.edit_message_text(message.chat.id,message.id,""" : ⠄⠄⠄⠄ ⠄⠄⠄⠄ ⠄⠄⠄⠄
 ⠄⠄⡔⠙⠢⡀⠄⠄⠄⢀⠼⠅⠈⢂⠄⠄⠄⠄
 ⠄⠄⡌⠄⢰⠉⢙⢗⣲⡖⡋⢐⡺⡄⠈⢆⠄⠄⠄
 ⠄⡜⠄⢀⠆⢠⣿⣿⣿⣿⢡⢣⢿⡱⡀⠈⠆⠄⠄
 ⠄⠧⠤⠂⠄⣼⢧⢻⣿⣿⣞⢸⣮⠳⣕⢤⡆⠄⠄
 ⢺⣿⣿⣶⣦⡇⡌⣰⣍⠚⢿⠄⢩⣧⠉⢷⡇⠄⠄
 ⠘⣿⣿⣯⡙⣧⢎⢨⣶⣶⣶⣶⢸⣼⡻⡎⡇⠄⠄
 ⠄⠘⣿⣿⣷⡀⠎⡮⡙⠶⠟⣫⣶⠛⠧⠁⠄⠄⠄
 ⠄⠄⠘⣿⣿⣿⣦⣤⡀⢿⣿⣿⣿⣄⠄⠄⠄⠄⠄
 ⠄⠄⠄⠈⢿⣿⣿⣿⣿⣷⣯⣿⣿⣷⣾⣿⣷⡄⠄
 ⠄⠄⠄⠄⠄⢻⠏⣼⣿⣿⣿⣿⡿⣿⣿⣏⢾⠇⠄
 ⠄⠄⠄⠄⠄⠈⡼⠿⠿⢿⣿⣦⡝⣿⣿⣿⠷⢀⠄
 ⠄⠄⠄⠄⠄⠄⡇⠄⠄⠄⠈⠻⠇⠿⠋⠄⠄⢘⡆
 ⠄⠄⠄⠄⠄⠄⠱⣀⠄⠄⠄⣀⢼⡀⠄⢀⣀⡜⠄
⠄⠄⠄⠄⠄⠄⠄⢸⣉⠉⠉⠄⢀⠈⠉⢏⠁⠄⠄
 ⠄⠄⠄⠄⠄⠄⡰⠃⠄⠄⠄⠄⢸⠄⠄⢸⣧⠄⠄
 ⠄⠄⠄⠄⠄⣼⣧⠄⠄⠄⠄⠄⣼⠄⠄⡘⣿⡆⠄
 ⠄⠄⠄⢀⣼⣿⡙⣷⡄⠄⠄⠄⠃⠄⢠⣿⢸⣿⡀
 ⠄⠄⢀⣾⣿⣿⣷⣝⠿⡀⠄⠄⠄⢀⡞⢍⣼⣿⠇
 ⠄⠄⣼⣿⣿⣿⣿⣿⣷⣄⠄⠄⠠⡊⠴⠋⠹⡜⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")
  app.send_message(message.chat.id,"اینم عکس ننش داش 🤤🤤" ,reply_to_message_id=message.id)

 elif message.text.startswith(".gpt "):
   try:
    text = message.text.replace(".gpt ","")[1::]
    result = requests.get(f"https://alpha-web.ir/nexapi/?license=nexapi&text={text}").json()['result']['GPT']
    app.send_message(message.chat.id,result,reply_to_message_id=message.id,disable_web_page_preview=True)
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

 elif message.text == ".arz":
   try:
    r = requests.get(f"https://api.pamickweb.ir/API/arz2.php").json()['result']
    app.app.edit_message_text(message.chat.id,message.id,f"<b>~ Digital Currency Price:\n\n• TRX <code>{r['TRX']}</code>\n• ADA <code>{r['ADA']}</code>\n• XRP <code>{r['XRP']}</code>\n• BTC <code>{r['BTC']}</code>\n• ETH <code>{r['ETH']}</code>\n• USDT <code>{r['USDT']}</code></b>")
# اپن شده در افغانستان سورس
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

 elif message.text.startswith(".id "):
   try:
     user_id_get = (message.reply_to_message.from_user.id if message.reply_to_message else app.get_users(message.text.split()[1]).id)
     user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
     count_photo = app.get_chat_photos_count(user_id_get)
     app.edit_message_text(message.chat.id,message.id,f"""<b>User Info : <code>{user.users[0].first_name if user.users[0].first_name else "خطا در دریافت"}</code>\n\n- first name : <code>{user.users[0].first_name if user.users[0].first_name else "خطا در دریافت"}</code>\n- last name : <code>{user.users[0].last_name if user.users[0].last_name else "Null"}</code>\n- user id : <code>{user.users[0].id if user.users[0].id else "Null"}</code>\n- username : <code>{f"<code>@{user.users[0].username}</code>" if user.users[0].username else "Null"}\n\n- profile picture count : <code>{count_photo}</code>\n- common chats count : <code>{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}</code>\n\n- bio : <code>{user.full_user.about if user.full_user.about else "Null"}</code>\n- scam : <code>{user.users[0].scam}</code>\n- can pin message : <code>{user.full_user.can_pin_message}</code>\n- contact : <code>{user.users[0].contact}</code>\n- bot : <code>{user.users[0].bot}</code>\n- verified : <code>{user.users[0].verified}</code>\n- deleted : <code>{user.users[0].deleted}</code>\n- phone calls available : <code>{user.full_user.phone_calls_available}</code>\n- phone calls private : <code>{user.full_user.phone_calls_private}</code>\n- video calls available : <code>{user.full_user.video_calls_available}</code>\n- access hash : <code>{user.users[0].access_hash}</code>\n- blocked : <code>{user.full_user.blocked}</code>\n\n{f"- current chat_id : <code>{message.chat.id}</code>" if message.chat.id != user.users[0].id else ""}</b>""")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

# اپن شده در افغانستان سورس

 elif message.text == ".me":
  user = app.get_me()
  app.edit_message_text(message.chat.id,message.id,f'<b>My Account Info :\n\n- first name : <code>{user.first_name}</code>\n- last name : <code>{user.last_name if user.last_name else "Null"}</code>\n- user id : <code>{user.id}</code>\n- username : <code>{f"@{user.username}" if user.username else "Null"}\n\n- language code : <code>{user.language_code}</code>\n- premium : <code>{user.is_premium}</code>\n- scam : <code>{user.is_scam}</code>\n- verified : <code>{user.is_verified}</code></b>')

 elif message.text == ".fun2": 
  app.edit_message_text(message.chat.id,message.id,"😛")
  app.edit_message_text(message.chat.id,message.id,"😝")
  app.edit_message_text(message.chat.id,message.id,"😜")
  app.edit_message_text(message.chat.id,message.id,"🤪")
  app.edit_message_text(message.chat.id,message.id,"🥴")

 elif message.text == ".fun3": 
  app.edit_message_text(message.chat.id,message.id,"=✊===>")
  app.edit_message_text(message.chat.id,message.id,"==✊==>")
  app.edit_message_text(message.chat.id,message.id,"===✊=>")
  app.edit_message_text(message.chat.id,message.id,"====✊>")
  app.edit_message_text(message.chat.id,message.id,"=✊===>")
  app.edit_message_text(message.chat.id,message.id,"==✊==>💦")
  app.edit_message_text(message.chat.id,message.id,"===✊=>💦💦")
  app.edit_message_text(message.chat.id,message.id,"====✊>💦💦")
  app.edit_message_text(message.chat.id,message.id,"=✊===>💦💦💦")
  app.edit_message_text(message.chat.id,message.id,"==✊==>💦💦💦💦")
  app.edit_message_text(message.chat.id,message.id,"===✊=>💦💦💦💦💦")
  app.edit_message_text(message.chat.id,message.id,"🥴 ohhhh 💦💦💦")

# اپن شده در افغانستان سورس

 elif message.text == ".fun4":
  app.edit_message_text(message.chat.id,message.id,"❤️")
  app.edit_message_text(message.chat.id,message.id,"🧡")
  app.edit_message_text(message.chat.id,message.id,"💛")
  app.edit_message_text(message.chat.id,message.id,"💚")
  app.edit_message_text(message.chat.id,message.id,"💙")
  app.edit_message_text(message.chat.id,message.id,"💜")
  app.edit_message_text(message.chat.id,message.id,"🤎")
  app.edit_message_text(message.chat.id,message.id,"🖤")
  app.edit_message_text(message.chat.id,message.id,"🤍")
  app.edit_message_text(message.chat.id,message.id,"💘")
  app.edit_message_text(message.chat.id,message.id,"💝")
  app.edit_message_text(message.chat.id,message.id,"💖")
  app.edit_message_text(message.chat.id,message.id,"💗")
  app.edit_message_text(message.chat.id,message.id,"💞")
  app.edit_message_text(message.chat.id,message.id,"💕")
  app.edit_message_text(message.chat.id,message.id,"❤️‍🩹❤️‍🔥💋")

 elif message.text == ".fun5":
  app.edit_message_text(message.chat.id,message.id,""" ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁""")
 elif message.text == ".love":
   app.edit_message_text(message.chat.id,message.id,"""♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡
♡┏┓┈╭━━╮┓┏┓━━┓♡
♡┃┃┉┃╭╮┃┃┃┃┏━┛♡
♡┃┃┈┃┃┃┃┃┃┃┗━┓♡
♡┃┃┉┃┃┃┃┃┃┃┏━┛♡
♡┃┗━┓╰╯┃╰╯┃┗━┓♡
♡┗━━┛━━╯━━╯━━┛♡
♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡""")

# اپن شده در افغانستان سورس

 elif message.text == ".dodol":
  app.edit_message_text(message.chat.id,message.id,"""⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⠟⠠⡰⣕⣗⣷⣧⣀⣅⠘⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⠃⣠⣳⣟⣿⣿⣷⣿⡿⣜⠄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡿⠁⠄⣳⢷⣿⣿⣿⣿⡿⣝⠖⠄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⠃⠄⢢⡹⣿⢷⣯⢿⢷⡫⣗⠍⢰⣿⣿⣿⣿⣿ 
⣿⣿⣿⡏⢀⢄⠤⣁⠋⠿⣗⣟⡯⡏⢎⠁⢸⣿⣿⣿⣿⣿ 
⣿⣿⣿⠄⢔⢕⣯⣿⣿⡲⡤⡄⡤⠄⡀⢠⣿⣿⣿⣿⣿⣿ 
⣿⣿⠇⠠⡳⣯⣿⣿⣾⢵⣫⢎⢎⠆⢀⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢨⣫⣿⣿⡿⣿⣻⢎⡗⡕⡅⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢜⢾⣾⣿⣿⣟⣗⢯⡪⡳⡀⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢸⢽⣿⣷⣿⣻⡮⡧⡳⡱⡁⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡇⢀⢗⣿⣿⣿⣿⡿⣞⡵⡣⣊⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⡀⡣⣗⣿⣿⣿⣿⣯⡯⡺⣼⠎⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣧⠐⡵⣻⣟⣯⣿⣷⣟⣝⢞⡿⢹⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡆⢘⡺⣽⢿⣻⣿⣗⡷⣹⢩⢃⢿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣷⠄⠪⣯⣟⣿⢯⣿⣻⣜⢎⢆⠜⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⡆⠄⢣⣻⣽⣿⣿⣟⣾⡮⡺⡸⠸⣿⣿⣿⣿ 
⣿⣿⡿⠛⠉⠁⠄⢕⡳⣽⡾⣿⢽⣯⡿⣮⢚⣅⠹⣿⣿⣿ 
⡿⠋⠄⠄⠄⠄⢀⠒⠝⣞⢿⡿⣿⣽⢿⡽⣧⣳⡅⠌⠻⣿""")

 elif message.text == ".no":
   app.edit_message_text(message.chat.id,message.id,"""😥┈┈┈┈😫┈┈😒😣😒
😒😒┈┈😒┈😒┈┈┈┈😲
😩┈😢┈😲┈⁣😤┈┈┈┈😠
😒┈┈😒😒┈😞┈┈┈┈😤
😭┈┈┈┈😖--😒😔😫
""")

## -_-_-_-_-_-_-_-_-_-_##

# اپن شده در افغانستان سورس

 elif (data["strike"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<s>{message.text}</s>")
  data.update({"strike": "1", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})

 elif (data["bold"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<b>{message.text}</b>")

 elif (data["mention"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>")

# اپن شده در افغانستان سورس

 elif (data["spoiler"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"||{message.text}||")

 elif (data["italic"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<i>{message.text}</i>")

 elif (data["underline"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<u>{message.text}</u>")
  
 elif (data["code"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<code>{message.text}</code>")

 elif (data["php"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"```php\n' {message.text} '\n```")

# اپن شده در افغانستان سورس

 elif (data["html"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"```html\n <- {message.text} ->\n```")

app.start(), print("Self Bot is STARTED . . .\n@AFGHANISTANSOURCE"), app.send_message("me" , "<b>Hi Sir . . .\nThe account manager bot ( <u>@AFGHANISTANSOURCE</u> ) was activated successfully.\n\nDevloped by : @AFGHANISTANSOURCE\nPublisher : @AFGHANISTANSOURCE</b>"),idle(), app.stop()

# اپن شده در افغانستان سورس



