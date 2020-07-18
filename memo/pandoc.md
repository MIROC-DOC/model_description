# Pandoc メモ

- PDF 出力したい人向け。執筆者が必ずしも入れる必要はない

- インストール

  - brew よりも公式のインストーラーを使うのが早い
    - [Pandoc の比較的簡単なインストール方法](https://qiita.com/sky_y/items/3c5c46ebd319490907e8)

- 使い方

  - `pandoc -f markdown -t latex README.md -o README.tex`

  - [markdown から pandoc で tex を出力してレポートの雛形を楽につくる](https://qiita.com/mosamosa/items/da33422f2bfc37bc5904)

    - `$ pandoc README.md -o README.tex`
      - これだと section, subsection 等うまく変換されない
      - 拡張子で自働判定されて、LaTeX ではなく TeX で出力されている

  - [Markdown と Pandoc を用いた簡易 Latex 環境の構築](https://qiita.com/mountcedar/items/e7603c2eb65661369c3b)

    - テンプレートファイルを指定するとよい
      - 記事中の default.latex を template.tex という名前で保存
      - テンプレートは引数でも指定できる
        - [Pandoc で Template を使うときのためのメモ](https://mk-55.hatenablog.com/entry/2018/09/18/003718)
    - `$ pandoc --template=template.tex README.md -o README.tex`
      - こうするとプリアンブルも含めて完全なファイルとして出力される
