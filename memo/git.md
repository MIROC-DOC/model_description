# Git ことはじめ

## 用語

- バージョン管理システム
  - git (\*)
- リポジトリ
  - リモートリポジトリ
  - ローカルリポジトリ
- ホスティングサービス = リモートリポジトリの置き場所
  - GitHub (\*) Utilityの豊富さから採用
  - GitLab
- 開発フロー = git の運用ルール
  - Git flow → 複雑
  - GitHub flow → 簡単 (\*)
  - GitLab flow → 中程度
- ホスティングサービスと開発フローは独立に選べる

## git 設定

# アカウントを作成する

https://github.com/
登録するメールアドレスは、大学や研究機関のものを推奨

```
# ユーザー名とメールアドレスを登録する
$ git config --global user.name "Haruka Hotta"
$ git config --global user.email hotta@aori.u-toyko.ac.jp
```

## 開発のやり方
開発フローには何通りかあるが、基本的にユーザは難しいことを考えず

1. ブランチを切る
2. 変更をcommit & pushする
3. プルリクエスト(マージリクエスト)を投げる

をすれば、管理者がうまくやってくれる。

## 本家からブランチを切って編集・マージリクエストするまで(コマンドライン)

```
# コードをGitHubから手元に持ってくる
$ git clone https://github.com/MIROC-DOC/model_description.git

# ブランチを確認
$ git branch
* master

# ブランチを切る
$ git branch feature/MYFEATURE master

# ブランチを変更
$ git checkout feature/MYFEATURE

# ローカルのブランチ情報をみる
$ git branch

# ファイル変更など、作業

# 変更したファイル名を確認
$ git diff --name-only

# コミットするファイルを選択
$ git add hogehoge

# コミット
$ git commit -m "commit message"

# プッシュ
$ git push origin feature/MYFEATURE

# GitHubのweb上でマージリクエストを送る。

どこかでミスをしても大概取り返せる（Git管理のメリット）ので、慌てず調べる。

```

## 基本的な操作

- fetch
- pull
- checkout
- add
- commit
- push

- バージョン番号を付けたい
  - タグを使う https://backlog.com/ja/git-tutorial/stepup/17/
