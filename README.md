# Python 中級
LinkedInラーニングの「Python 中級」コース用のリポジトリです。このコースは [LinkedInラーニング][lil-course-url]で視聴できます。

![Python 中級][lil-thumbnail-url] 
Pythonの扱いに慣れ、もう少し実践的なプログラミング手法を学びたいと考えていますか。forループでリストやタプルを操作することに飽きたのであれば、Pythonのよりディープな面を学ぶときです。このコースはPythonの中級コースで、一通り基本を習得している方を対象としています。まずPythonのより深い仕様や、可変長引数やキーワード専用引数などの関数を作成するときに知っておくとよい内容を解説します。そして実践的なコレクションやクラス、オブジェクトのカスタマイズ方法、さらに実用に添ったログの取り方、ラムダ式や内包表記などを説明します。このコースを学んでPythonプログラマとして次のステージに進みましょう（本コースはアメリカの人気トレーナーJoe Marini氏のコースを日本のユーザー向けに再構成したものです）。

## リポジトリの使い方
このリポジトリには必要に応じてブランチが設けられています。ブランチのポップアップメニューを使用して、使用するブランチに切り替えたあとにコースを視聴してください。またURLに`「/tree/ブランチ名」`を追加することで、アクセスしたいブランチに移動することも可能です。

## ブランチ
ブランチはレッスンごとに作成されている場合があります。その場合はブランチ名に`「章番号_レッスン番号」`が付けられています。例えば`「02_03」`という名前のブランチは、2章の上から3番目のレッスン用のブランチとなります。

レッスン前と後のコードを格納しているブランチもあります。該当ブランチには「開始時」（beginning）を表す`「b」`と、「終了時」（ending）を表す`「e」` がブランチ名についています。`「b」`のブランチにはレッスン開始時点のコードが、`「e」`のブランチにはレッスン終了時点のコードが格納されています。また「main」のブランチにはコードの最終形が格納されています。

ファイルに変更を加えた後に、エクササイズファイルのブランチを次のブランチに切り替えたさい、次のようなメッセージが表示されることがあります。

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

この問題を解決するには：
	
    次のコマンドで変更を加えます：git add .
	次のコマンドで変更をコミットします：git commit -m "some message"

## インストール
1. エクササイズファイルを利用するさいは、次のソフトウェアをインストールしておく必要があります。
	- [Python](https://www.python.org)
2. エクササイズファイルを効率よく利用するには、次のソフトウェアをインストールすることをお勧めします。VS Codeを日本語化するにはインストール後、拡張機能Japanese Language Pack for Visual Studio Codeをインストールしてしてください。
    - [VS Code](https://code.visualstudio.com)

    
3. GitHubよりダウンロードしたZIPファイルを解凍して利用してください。

### インストラクター

**金宏 和實**

_株式会社イーザー副社長、テクニカルライター_

この講師の他のコースを視聴する：[LinkedInラーニング](https://www.linkedin.com/learning/instructors/21400000)

[lil-course-url]: https://www.linkedin.com/learning/advanced-python-22157857
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQGdlmVRJq1dDQ/learning-public-crop_675_1200/0/1683231698784?e=2147483647&v=beta&t=2TqyuFf-fPW1j4bPtmvV6GBk-c5s03wbQBpp-aVVa4M
