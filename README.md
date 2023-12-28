# Python：ヒントとテクニック
LinkedInラーニングの「Python：ヒントとテクニック」コース用のリポジトリです。このコースは [LinkedInラーニング][lil-course-url]で視聴できます。

![Python：ヒントとテクニック][lil-thumbnail-url] 
Pythonの学習を進めるさいに「Pythonだとこんなことができるんだ」という単純な驚きから、「こういう仕組みだからこういうことができるんだ」という気づきに展開することができれば、学習が発見にあふれ、楽しくなるのではないでしょうか。このコースではPythonの特徴的な仕様にフォーカスを当ててPythonを学びます。Pythonの哲学である「The Zen of Python」の説明から始まり、イテラブルの操作でのall関数やany関数の使用、浅いコピーと深いコピーの違い、そしてラムダ式の使用を解説します。それに加えデコレータやキーワード付き引数、Pythonを学習するのに役立つ関数なども紹介します。このコースでいつもとは違った角度からPythonを学習してみましょう。

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
1. Pythonをインストールしてください。
	- [Python](https://www.python.org)
2. VS Codeをインストールしてください。
    - [VS Code](https://code.visualstudio.com)    
3. VS Codeの拡張機能であるJapanese Language Pack for Visual Studio Codeをインストールしてください。インストール後にVS Codeを再起動すると日本語化されます。
4. VS Codeの拡張機能であるPython extension for Visual Studio Codeをインストールしてください。
5. Exercise Filesをドキュメントフォルダなどに配置してください。
6. VS Codeを起動して、Exercise Filesの各チャプター(Ch01など)を開いてください。

### インストラクター

**金宏 和實**

_株式会社イーザー副社長、テクニカルライター_

この講師の他のコースを視聴する：[LinkedInラーニング](https://www.linkedin.com/learning/instructors/21400000)

[lil-course-url]: https://www.linkedin.com/learning/python-tips-tricks-and-techniques
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D4D0DAQH20mG0A_sXJA/learning-public-crop_675_1200/0/1703184236382?e=2147483647&v=beta&t=Rv9lXvZwz32ZH2GTpiWAlmQfBboTfC5L-4pX-K1mmz0
