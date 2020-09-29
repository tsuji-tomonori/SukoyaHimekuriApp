# SukoyaHimekuriApp

その日の日付に応じて[健屋花那 ひめくりめざましボイス](https://booth.pm/ja/items/2400409) を再生するアプリ. 

この時ボイスを再生する前に電話の呼び出し音を再生することで「モーニングコール」されている雰囲気を実現.

## Install

Requirements:

* Python 3.7
* mutagen 1.44.0
* pygame 1.9.6

Install from source:

```bash
git clone https://github.com/tsuji-tomonori/SukoyaHimekuriApp.git
cd SukoyaHimekuriApp
pip install -r requirements.txt
```

## Initialize

まず, 音声ファイルを設置します.

```
SukoyaHimekuriApp/
├ config/
|    └ YYYY-MM.json
├ voice/
|    ├ se/
|       └ chakusin.mp3
|    └ 健屋花那_ひめくりめざましボイス_3月分_/
├ init.py
└ main.py
```

root直下にディレクトリ ``voice`` を作成したのち, その中に解凍したボイスをフォルダーのまま入れます.

また, ``voice`` の中に``se`` を作成したのち, その中に着信用ボイスを``chakusin.mp3`` として入れます.

---

次に, configファイルを作成します.

```
python init.py
```

すると

```
index:0 [voice\se]
index:1 [voice\健屋花那_ひめくりめざましボイス_3月分_]
index:
```

といった形で表示されるため, 今回対象とするファイルのindex (この場合は1) を入力します.

```
year:
month:
save as config\2020-03.json
```

あとは, year(2020) , month(3) に対応する値を入力します. 

### 着信音源の例

* [【効果音】携帯の着信音＃１](https://pocket-se.info/archives/1515/)

## Usage

```
python main.py
```

実行すると以下の文字列が表示されるとともに, 設定した着信音が流れます.

```
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
enter
```

あとは任意のタイミングで[Enter] を押下するとその日のボイスが再生されます.

## Attention

このプログラムは個人の趣味で作られたものであり, 健屋花那さん 及び, いちから株式会社とは一切関係がありません.

もしバグ等ございましたら, issu や Pull request をお願いします.

また, このプログラムを実行する前に, 手洗いうがいをしましょう. (#手洗いうがいしたぞ健屋)

## Link

* [YouTube](https://www.youtube.com/channel/UC8C1LLhBhf_E2IBPLSDJXlQ)
* [Twitter](https://twitter.com/sukosuko_sukoya)
* [ボイス](https://booth.pm/ja/items/2400409)