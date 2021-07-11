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
  - Gitの操作はmodel_descriptionディレクトリで

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
  - 形式で迷ったら、[原稿](../descript/)を参照
  - Markdownで書く場合
    - エディタ上でリアルタイムにプレビューできる
    - [Chrome拡張](https://chrome.google.com/webstore/detail/mathjax-3-plugin-for-gith/peoghobgdhejhcmgoppjpjcidngdfkod)を入れるとブラウザのGitHubから数式プレビューできる
    - [pandoc](https://pandoc.org/) を使って LaTeX に translate する → [Pandoc メモ](./pandoc.md)
  - [Mathpix Snip](https://gigazine.net/news/20200106-mathpix-snip/)は数式画像をLatex形式に変換してくれる

- 使用言語

  - 最終的には英語で原稿を揃えるが、日本語で原稿を作成・DeepL Proなどの力を借りて英訳してOK。

- ディレクトリ構成

  - draft/ 原稿ファイルを置く
  - memo/ 主に Markdown で書かれたプロジェクトに関するメモ書き
  - org/ 既存のCCSR/NIES AGCMマニュアルやその英訳
  
- 開発フロー（執筆者）

  - 1)[issue に執筆目標を書く](https://github.com/MIROC-DOC/model_description/issues)
  - 2)ローカルの資料を最新のdevelopに `git pull origin develop`
  - 3)執筆担当の人は issue に基づいて develop ブランチを元に featureE(章の名前など、各自で特徴的な名前を設定) ブランチを作成する(./git.md)`git checkout -b feature develop`。すでにあるリモートブランチを変更する場合、`git checkout -b feature feature`
  - 今いるブランチを確認する。`git branch`
  - 4)feature ブランチで執筆する。
    - a)ファイル変更が一段落するたびに、コミットする
      - コミットするファイルを選択（ステージング）`git add hogehoge`
      - 変更箇所についてコメントと共にコミット`git commit -m "add hogehoge subsection"`
      - コミット状況を確認`git status`
    - b)ローカルのファイル変更をリモートのfeature ブランチへ反映する`git push origin feature`
  - 5)執筆が完了したら[ブラウザ版GitHub](https://github.com/MIROC-DOC/model_description)からdevelopブランチへプル・リクエストを投げる。[やり方](https://docs.github.com/ja/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request#creating-the-pull-request)
  - review が行われ、問題があれば執筆者が再度修正する
    - プルリクエストの一覧は[ここ](https://github.com/pulls)から見れる
  - review で問題が無ければ管理者がマージする
    - コンフリクトが発生している場合、管理者が解消する
  - feature ブランチを削除する。issueをcloseする。

Gitについてはブランチを切る&コミットログを残す、ができれば細かい操作は自由。エディタのGUIを使うと楽。
ローカルのファイル削除などしない限り、Gitの操作は大体取り返しがつく。


## 関連項目

- [Pandoc メモ](./pandoc.md)
- [LaTeX メモ](./latex.md)
