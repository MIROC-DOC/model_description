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

## Markdown

- [Chrome拡張](https://chrome.google.com/webstore/detail/mathjax-3-plugin-for-gith/peoghobgdhejhcmgoppjpjcidngdfkod)を入れるとブラウザのGitHubから数式プレビューできる
- [pandoc](https://pandoc.org/) を使って LaTeX に translate する → [Pandoc メモ](./pandoc.md)
- [Mathpix Snip](https://gigazine.net/news/20200106-mathpix-snip/)は数式画像をLatex形式に変換してくれる
