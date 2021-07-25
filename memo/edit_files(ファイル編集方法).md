# 編集の手引き

## 目標

- 更新履歴を残す
- ユーザーが現代的な開発手法(git)に慣れる
  - 直接 master ブランチに push しないやり方を学ぶ

## 使用フォーマット

  - 基本的に Markdown で執筆
  - 形式で迷ったら、[原稿](../descript_files/)を参照

### 数式

  - tex形式で書く。インライン数式は`$`で囲い、ディスプレイ数式は`$$`で囲う。
  - 数式番号はtagを使ってふる。 `$$a^2+b^2=c^2 \tag{eq.1}$$`
  - 数式の引用方法 `([1](eq.1))`で ([1](eq.1))

### 図

  - 図の挿入 `![figire_caption](figure_path.png)`

## 使用言語

  - 最終的には英語。日本語で原稿を作成・DeepL Proなどの力を借りて英訳してOK。

## 編集フロー（簡易版）

ブラウザ版GitHubのDevelopブランチを直接編集する。

  - 1)developブランチに移動する。[ここをクリック](https://github.com/MIROC-DOC/model_description/tree/develop)
  - 2)3)4)ファイルを編集する。
  - 5)"Commit changes"を押す。

<img src="./210712_MIROC_GitHub_develop.key-1.png" width=800x>
  
## 編集フロー（詳細版。新しくファイルを作る場合・複数ファイルを編集する場合など）

  - 1)[issue に執筆目標を書く](https://github.com/MIROC-DOC/model_description/issues)
  - 2) 執筆用のブランチをローカルに作る
    - ローカルにGitHubのデータを持ってくる `git clone git@github.com:MIROC-DOC/model_description.git`
    - ローカルの資料を最新のdevelopブランチに `git pull origin develop`
    - 執筆担当の人は issue に基づいて develop ブランチを元に feature(章の名前など、各自で特徴的な名前を設定) ブランチを作成する`git checkout -b feature develop`。develop以外のリモートブランチを変更する場合、`git checkout -b feature feature`
    - 今いるブランチを確認する。`git branch`
  - 3)feature ブランチで執筆する。
    - a)ファイル変更が一段落するたびに、コミットする
      - コミットするファイルを選択（ステージング）`git add hogehoge`
      - 変更箇所についてコメントと共にコミット`git commit -m "add hogehoge subsection"`
      - コミット状況を確認`git status`
    - b)ローカルのファイル変更をリモートのdevelop ブランチへ反映する`git push origin develop`
  - 5)執筆が完了したら[ブラウザ版GitHub](https://github.com/MIROC-DOC/model_description)からdevelopブランチへプル・リクエストを投げる。[やり方](https://docs.github.com/ja/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request#creating-the-pull-request)
  - review が行われ、問題があれば執筆者が再度修正する
    - プルリクエストの一覧は[ここ](https://github.com/pulls)から見れる
  - review で問題が無ければ管理者がマージする
    - コンフリクトが発生している場合、管理者が解消する
  - feature ブランチを削除する。issueをcloseする。

Gitについてはブランチを切る&コミットログを残す、ができれば細かい操作は自由。[Gitの手引き](../git.md)。エディタのGUIを使うと楽[おすすめ環境](../setting.md)。
ローカルのファイル削除などしない限り、Gitの操作は大体取り返しがつく。
