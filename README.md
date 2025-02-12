# mqtt-sample

PythonによるMQTTサンプル

## Brokerの準備

### macOS

Homebrewからインストールする。

```
brew install mosquitto
```

起動はbrew servicesを使用する。

```
brew services start mosquitto
```

停止も同様に、以下のコマンドを実行する。

```
brew services stop mosquitto
```

以上
