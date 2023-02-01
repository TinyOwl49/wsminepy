# wsminepy

### Description
Minecraft統合版を操作するWebsocketサーバーを構築するPythonライブラリです。
### Install
```
pip3 install git+https://github.com/TinyOwl49/wsminepy.git
```

### Usage
```py
import wsminepy as ws

server = ws.Server()

# clientが接続したときに呼び出されます
@server.init
def connect():
	print("connected")

# イベントが発生したときに呼び出されます
@server.listen()
async def allEvent(data):
	# データはdict型です
	print(data)
	
# イベント名を指定できます
@server.listen(event="PlayerMessage")
async def playerMessage(data):
	msg = data['message']
        sender = data['sender']
        print(f"<{sender}>{msg}")

	if msg == "#hoge":
		# コマンドを実行します
		await server.run_command(f"kill {sender}")
		# tellコマンドを実行します
		await server.tell("hogehoge", sender)

# Portを指定します。
# デフォルトはlocalhost:7777です。
server.start("localhost", 1729)
```
Pythonを実行した後、以下のコマンドをMinecraftで実行してください。
```mc
/wsserver localhost:1729
```

### TODO
- [x] Minecraft内のイベントを取得
- [x] コマンドの送信
- [ ] データ構造のオブジェクト化 
- [ ] 最新のイベントリストの取得

### Licence
[MIT](https://github.com/TinyOwl49/wsminepy/blob/main/LICENSE)

### Author
[TinyOwl](https://github.com/TinyOwl49)
