# PokeControllerForCircuitPython

Poke Controller ModifiedとSwitch間を中継するCircuitPythonソフトウェア

# 導入方法

必要なもの

    Raspberry Pi Pico 1台
    USB-UART変換機 1台
    USB ケーブル 2本（PCとUSB-UART変換、Raspberry Pi Pico と Switchを接続するのに必要）

動作環境

    CircuitPython 8.0.0-rc.2


参考URL:https://circuitpython.org/board/raspberry_pi_pico/

# 使い方

## 事前準備

Raspberry Pi PicoでCircuitPythonが使えるようにして下さい

## ライブラリのダウンロード

1. [https://circuitpython.org/libraries](https://circuitpython.org/libraries)からCircuitPythonのライブラリ(Bundle for Version 8.x)をダウンロードし展開する
2. このリポジトリをダウンロードし展開する

## 書き込み

1. Raspberry Pi PicoをPCに接続。CIRCUITPYドライブとして認識
2. CircuitPythonのライブラリの中のadafruit_hidフォルダをCIRCUITPYドライブのlibフォルダへコピーする
3. CIRCUITPYドライブにこのリポジトリのboot.py, code.py, switchcontroller.py, pokecon.pyをコピーする

フォルダ構成
~~~
CIRCUITPY
  |-- lib
  |    |-- adafruit_hid
  |
  |-- boot.py
  |-- code.py
  |-- switchcontroller.py
  |-- pokecon.py
~~~

4. Raspberry Pi PicoをSwitchに接続
5. Raspberry Pi PicoとUSB-UART変換を接続する

~~~
Raspberry Pi Pico 1番ピン(UART0TX) <-------> USB-UART変換 RX
Raspberry Pi Pico 2番ピン(UART0RX) <-------> USB-UART変換 TX
Raspberry Pi Pico 3番ピン(GND)　　 <-------> USB-UART変換 GND
~~~

6. USB-UAR変換をPCと接続

Poke Controller側のCOM Port番号をUSB-UART変換のものに合わせてSwitch Controller Simulatorなどでボタンを押して動作確認してください

# 注意

MCUコマンド、キーボード入力には対応してません

# Lisence

このプロジェクトのライセンスはMITライセンスです。詳細はLICENSEをご覧ください
