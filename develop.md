# 開発の手引き

## 目標

- 更新履歴を残す
- ユーザーが現代的な開発手法(git)に慣れる
  - 直接 master ブランチに push しないやり方を学ぶ

## Git に慣れてない人向け解説

- [Git ことはじめ](./git.md)

## GitHub の準備とリポジトリのクローン

- GitHub のアカウント作成

  - https://github.com/
  - 無料。大学や研究機関のメールアドレスで作る
  - Google や GitLab のアカウントに紐付けて作れる

- GitHub  への公開鍵の登録
  - 作業したい環境で、公開鍵を生成・登録する
  - [GitHubでssh接続する手順~公開鍵・秘密鍵の生成から~](https://qiita.com/shizuma/items/2b2f873a0034839e47ce)
  - [GitHubに公開鍵認証方式でSSH接続する](https://hacknote.jp/archives/56523/)
- .ssh/config の編集

  ```ssh:config
  Host github.com
      User git
      HostName github.com
      identitiesonly yes
      identityFile ~/.ssh/id_rsa
  ```

- リポジトリを clone する(リモートからローカルへ資料を引っ張ってくる)
  - `git clone https://github.com/MIROC-DOC/model_description.git`

- 練習用のリポジトリは何しても大丈夫です
  - `git clone https://github.com/MIROC-DOC/SandBox.git`

## テキストエディタのインストール

- かならず必要なわけではないが、出来れば一度試してほしい

- 基本的な欲しい機能

  - git の管理 (fetch, pull, add, commit, push) が GUI でできる
  - Markdown のプレビューができる

- 最近のおすすめ
  - [VS Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/) (\*)
    - Japanese Language Package for Visual Studio Code 日本語化
    - Git History 履歴を表示する拡張
    - Markdown All in One マークダウン用拡張
    - [VS Code で Markdown をプレビューするには？](https://www.atmarkit.co.jp/ait/articles/1804/20/news030.html)
    - LaTeX language support LaTeX のシンタックスハイライト
  - [Atom](https://atom.io/)
    - Git の GUI はこちらのほうが直観的かも
    - ~/.atom/packagesのおすすめは?以下、木野の場合
      - markdown-scroll-sync
      - markdown-writer
      - tool-bar-markdown-writer
      - tool-bar
      - markdown-to-pdf
      - tree-view-copy-relative-path
      - japanese-menu
      - atom-html-preview
      - markdown-preview-enhanced
      - markdown-table-formatter
      - highlight-line

## Git リポジトリの運用

- 使用フォーマット

  - 新たに書く原稿は、基本的に Markdown or Latex
  - 形式で迷ったら、[Markdown原稿](./org/md_en/)や[Latex原稿](./org/tex_en/)を参照
  - Markdownで書く場合
    - エディタ上でリアルタイムにプレビューできる
    - [pandoc](https://pandoc.org/) を使って LaTeX に translate する → [Pandoc メモ](./pandoc.md)
  - LaTeX ファイルは、章ごとあるいは全体をまとめてタイプセットできるようにする

- 使用言語

  - 最終的には英語で原稿を揃えるが、日本語で原稿を作成してOK。
  - DeepL Proの力を借りて英訳する。

- ディレクトリ構成

  - md/ Markdown 形式の原稿ファイルを置く
  - tex/ LaTeX 形式の原稿ファイルを置く
    - markdown から変換された LaTeX はここに出力される
  - pdf/ 変換された PDF を置く
  - memo/ 主に Markdown で書かれたプロジェクトに関するメモ書き
  - org/ CCSR/NIES AGCMマニュアルやその英訳
  - reference/ 公開しても問題ない、既存の参考資料

- 開発フロー

  1. [issue に執筆目標を書く](https://github.com/MIROC-DOC/model_description/issues)
  2. ローカルの資料を最新に `git pull`
  3. 執筆担当の人は issue に基づき master ブランチを元に feature/MYFEATURE ブランチを切る(./git.md)`git checkout -b feature/MYFEATURE origin`
  - 今いるブランチを確認する。`git branch`
  4. feature/MYFEATURE ブランチで執筆する。abcの手順で共同編集者でファイルをやり取りする。
    1. ファイル変更が一段落するたびに、コミットする
      - コミットするファイルを選択（ステージング）`git add hogehoge`
      - 変更箇所についてコメントと共にコミット`git commit -m "add hogehoge subsection"`
      - コミット状況を確認`git status`
    2. ローカルのファイル変更をリモートのfeature/MYFEATURE ブランチへ反映する  そのブランチにおける初めてのpush。リモートにbranchを作成する`git push -u origin feature/MYFEATURE`  ２回目以降のpush`git push origin feature/MYFEATURE`
    3. 共同編集者が最新のfeature/MYFEATURE ブランチをローカルに反映する。feature/MYFEATURE ブランチにて`git pull`
  5. 執筆が完了したら[ブラウザ版GitHub](https://github.com/MIROC-DOC/model_description)からプル・リクエストを投げる。[やり方](https://docs.github.com/ja/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request#creating-the-pull-request)
  - review が行われ、問題があれば執筆者が再度修正する
    - プルリクエストの一覧は[ここ](https://github.com/pulls)から見れる
  - review で問題が無ければ管理者がマージする
    - コンフリクトが発生している場合、管理者が解消する
  - feature ブランチを削除する。issueをcloseする。

GUIでの操作も積極的に活用すべし。  
ローカルのファイルを削除したりしない限り、作業をミスしても大体取り返しがつく。

[編集者の作業フロー](../assets/memo_develop_GitHub_flow.png)

## 関連項目

- [Pandoc メモ](./pandoc.md)
- [LaTeX メモ](./latex.md)
