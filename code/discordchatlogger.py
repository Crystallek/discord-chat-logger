import websocket, json, threading, time, requests, colorama, emoji, os, unidecode

os.chdir(os.path.dirname(__file__))
colorama.init(convert=True)

def send_json_request(ws, request):
    try:
        ws.send(json.dumps(request))
    except Exception as e:
        print(f"{colorama.Fore.RED}An error occured: {str(e)}")
        time.sleep(.1)
        input(f"Press any key to exit the program...{colorama.Fore.RESET} ")
        exit()

def receive_json_response(ws):
    try: 
        response = ws.recv()
        if response:
            return json.loads(response)
    except Exception as e: 
        print(f"{colorama.Fore.RED}An error occured: {str(e)}")
        time.sleep(.1)
        input(f"\n{colorama.Fore.RESET}Press any key to exit the program...")
        exit()
    
def heartbeat(ws, interval):
    while True:
        heartbeatJSON = {"op": 1, "d": "null"}
        send_json_request(ws, heartbeatJSON)
        time.sleep(interval)


def main():
    print(f"""{colorama.Fore.BLUE}\n  _____ _____  _____  _____ ____  _____  _____     _____ _    _       _______   _      ____   _____  _____ ______ _____  
 |  __ \_   _|/ ____|/ ____/ __ \|  __ \|  __ \   / ____| |  | |   /\|__   __| | |    / __ \ / ____|/ ____|  ____|  __ \ 
 | |  | || | | (___ | |   | |  | | |__) | |  | | | |    | |__| |  /  \  | |    | |   | |  | | |  __| |  __| |__  | |__) |
 | |  | || |  \___ \| |   | |  | |  _  /| |  | | | |    |  __  | / /\ \ | |    | |   | |  | | | |_ | | |_ |  __| |  _  / 
 | |__| || |_ ____) | |___| |__| | | \ \| |__| | | |____| |  | |/ ____ \| |    | |___| |__| | |__| | |__| | |____| | \ \ 
 |_____/_____|_____/ \_____\____/|_|  \_\_____/   \_____|_|  |_/_/    \_\_|    |______\____/ \_____|\_____|______|_|  \_\
\n\n {colorama.Fore.RESET}Made by Crystallek#3348\n""")

    ws = websocket.WebSocket()

    try: ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
    except Exception as e:
        print(f"{colorama.Fore.RED}An error occured: {str(e)}")
        time.sleep(.1)
        input(f"Press any key to exit the program...{colorama.Fore.RESET} ")
        exit()
    
    _time = time.strftime("%d-%m-%Y")
    event = receive_json_response(ws)
    token = open("data/token.txt", "r").readlines()[0]
    payload_event = {"op": 2, "d": {"token": token, "properties": {"$os": "linux", "$browser": "chrome","$device": "pc"}}}
    payload_guild = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36','Authorization': token,'Content-Type': 'application/json'}
    heartbeat_interval = event["d"]["heartbeat_interval"] / 1000 - 5
    ids = {}

    threading.Thread(target=heartbeat, args=[ws, heartbeat_interval], daemon=True).start()
    send_json_request(ws, payload_event)
    receive_json_response(ws)

    print(f"{colorama.Fore.GREEN}Successfully connected!\nReady to receive messages.\nLogs will be written to \"log{_time}.txt\".\n{colorama.Fore.RESET}")

    while True:
        event = receive_json_response(ws)
        timeNow = time.strftime("%d.%m.%Y @ %H:%M:%S")
        try: 
            try:
                if event['d']['guild_id'] in ids:
                    response  = ids.get(event['d']['guild_id'])
                else:
                    response = json.loads(requests.get(f"https://discord.com/api/v9/guilds/{event['d']['guild_id']}/preview", headers=payload_guild).text)['name']
                    ids[event['d']['guild_id']] = response
                
                if str(event['d']['attachments']) == "[]": 
                    print(f"{colorama.Fore.BLUE}{response} | {timeNow} | {colorama.Fore.RED}{unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {colorama.Fore.RESET}{event['d']['content']}".replace("\n", ""))
                else: 
                    print(f"{colorama.Fore.BLUE}{response} | {timeNow} | {colorama.Fore.RED}{unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {colorama.Fore.RESET}{event['d']['content']} {colorama.Fore.YELLOW}| {event['d']['attachments'][0]['url']}".replace("\n", ""))

                with open(f"data/log{_time}.txt", "a", encoding="utf-8") as f:
                    if str(event['d']['attachments']) == "[]": 
                        f.write(emoji.demojize(f"{response} | {timeNow} | {unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {event['d']['content']}\n"))
                    else: 
                        f.write(emoji.demojize(f"{response} | {timeNow} | {unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {event['d']['content']} | {event['d']['attachments'][0]['url']}\n"))
                continue

            except:
                try:
                    if str(event['d']['attachments']) == "[]": 
                        print(f"{colorama.Fore.BLUE}{event['d']['guild_id']} | {timeNow} | {colorama.Fore.RED}{unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {colorama.Fore.RESET}{event['d']['content']}".replace("\n", ""))
                    else: 
                        print(f"{colorama.Fore.BLUE}{event['d']['guild_id']} | {timeNow} | {colorama.Fore.RED}{unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {colorama.Fore.RESET}{event['d']['content']} {colorama.Fore.YELLOW}| {event['d']['attachments'][0]['url']}".replace("\n", ""))

                    with open(f"data/log{_time}.txt", "a", encoding="utf-8") as f:
                        if str(event['d']['attachments']) == "[]": 
                            f.write(emoji.demojize(f"{event['d']['guild_id']} | {timeNow} | {unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {event['d']['content']}\n"))
                        else: 
                            f.write(emoji.demojize(f"{event['d']['guild_id']} | {timeNow} | {unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {event['d']['content']} | {event['d']['attachments'][0]['url']}\n"))
                    continue

                except:
                    if str(event['d']['attachments']) == "[]": 
                        print(f"{colorama.Fore.BLUE}DMS | {timeNow} | {colorama.Fore.RED}{unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {colorama.Fore.RESET}{event['d']['content']}".replace("\n", ""))
                    else: 
                        print(f"{colorama.Fore.BLUE}DMS | {timeNow} | {colorama.Fore.RED}{unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {colorama.Fore.RESET}{event['d']['content']} {colorama.Fore.YELLOW}| {event['d']['attachments'][0]['url']}".replace("\n", ""))

                    with open(f"data/log{_time}.txt", "a", encoding="utf-8") as f:
                        if str(event['d']['attachments']) == "[]": 
                            f.write(emoji.demojize(f"DMS | {timeNow} | {unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {event['d']['content']}\n"))
                        else: 
                            f.write(emoji.demojize(f"DMS | {timeNow} | {unidecode.unidecode(event['d']['author']['username'])}#{event['d']['author']['discriminator']}: {event['d']['content']} | {event['d']['attachments'][0]['url']}\n"))
                    continue
        except: 
            pass

if __name__ == "__main__":
    main()
