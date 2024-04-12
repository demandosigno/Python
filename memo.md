* **3-3.条件式**
**3-3.条件式**
比較演算子、in演算子、真偽値、論理演算子
**3-4.分岐構文のバリエーション
if-else, if-elif, 三項演算子p.399
**4-1.繰り返し**
while, for..in, range(), break, continue
**5-1.オリジナルの関数**
ローカル変数
関数の引数、戻り値
複数の戻り値、暗黙のタプル
デフォルト引数、キーワード指定、可変長引数
グローバル変数
**6 オブジェクト**
すべての値はオブジェクト。関数さえオブジェクト
オブジェクトの設計図、class
オブジェクトに属するデータを属性、関数をメソッドという
オリジナルのクラス定義
オブジェクトのidentity、参照
関数の引数や戻り値にidentityが受け渡されると、変数の独立性が崩れる可能性がある→防御的コピー
int, str, tupleなどは不変オブジェクト
**7 モジュール**
組み込み関数。ファイル入力、文字コード。
import as
from モジュール名 import 変数名または関数名 as 別名
特定の変数や関数だけを取り込んだり、別名を付けたり
from モジュール名 import * でワイルドカードも使えるが非推奨
パッケージ
import http.client（httpパッケージのclientモジュール）
from http import client
from http.client import HTTPConnection