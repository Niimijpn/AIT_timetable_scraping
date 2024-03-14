#　愛知工業大学　個人時間割スクレイピングプログラム
## 内容
### 愛知工業大学の個人時間割をcsvに変換するプログラムです．
### スクレイピングを使って遊ぼうとした時の試験的に作成したプログラムです．
### node.jsを使用している意味はありません．過去にnode.jsを使って発展させようとした痕跡です．
### スクレイピング機能の全てはlogin.pyです．
## 使用にあたって
### スクレイピングを行う際は対象のサーバーに負荷をかけすぎないようにしましょう．
### seleniumがインストールしてあることが前提です．仮想環境などを利用して，seleniumをインストールしてください．
### seleniumをインストールする際の注意点は以下を参照
### https://qiita.com/niimi_t0t/items/45e6dce80bf281069a09

## 使い方
### login.py　line 7,8 のUSERとPASSの値を自身のものに変更してください.
### seleniumが利用できる環境でnode.jsの実行，もしくはroutes/login.pyを実行するとpublic/csvにclass_schedule.csvが生成されます．
