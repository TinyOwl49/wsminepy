import wsminepy as ws

server = ws.Server()

# clientが接続したときに呼び出されます


@server.init
async def connect():
    print("connected")


# イベントが発生したときに呼び出されます


@server.listen()
async def allEvent(eventname, data):
    # データはdict型です
    print(eventname)
    # print(data)

# イベント名を指定できます


@server.listen(event="PlayerMessage")
async def playerMessage(data):
    msg = data['message']
    sender = data['sender']
    print(f"<{sender}>{msg}")

    if msg == "#hoge":
        # コマンドを実行します
        res, _ = await server.run_command(f"kill {sender}")
        print("[system]", res.statusMessage)

        # tellコマンドを実行します
        await server.tell("hogehoge", sender)

# Portを指定します。
# デフォルトはlocalhost:7777です。
server.start("localhost", 1729)
