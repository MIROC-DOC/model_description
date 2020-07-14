# 今後の方針
**統合の2020年度後半の予算をつかって、年度末までにドキュメント完成** 
-> 詳細は[POCKIEの芳村先生資料](https://atm-phys.nies.go.jp/~fswiki/miroc/wiki.cgi?page=POCKIE%A5%DF%A1%BC%A5%C6%A5%A3%A5%F3%A5%B0+%282020%2D06%2D26%29&file=20200626%5FPOCKIE%5FMIROCdescription%2Epptx&action=ATTACH)

## タスクリスト

### 本格稼働用のGitHubリポジトリの整備
 - このリポジトリを元に、引越し先の環境を整備 -> いつまで？（なるはや
 - どこにつくるのか？管理人は誰？
 
### 業者外注/学生担当の区別化 -> 芳村先生と相談
 - 既存資料の書式変換、LaTeXアップデート、英訳 -> ツールは決まっているので機械的な作業。業者or学生
 - 書籍？としての体裁 -> 年度末にどんな形でまとめるかと関連
 
### 既存資料の収集
 - ひとまず[Google Docs](https://docs.google.com/document/d/1aCOL8jx7PzUXyGGo1XPLKr8W7igDmY-lB5Z7tDSkJr4/edit#heading=h.4580oq1i8gdv)に集約中。GitHubが整備出来次第そちらにpushしてもらうように。

## 公開範囲

- GitHubの公開リポジトリ
- 学生がGitHubを使いたい、使えるというなら、モデル本体も将来的にGitHubで使えるようにする可能性をさいとうふゆきさんが示唆？

## 誰がどうやって頑張るか

- 東大GCMセミナーのD学生。それでうまらないところは統合の先生方が検討。
- doi取得など、できるだけ実績としてオフィシャルなものになるよう先生方が検討してくださる。

---

# 開発の手引き

 - [develop.md](./memo/develop.md)
 -  ドキュメントの目次 [contesnts.md](./doc/contents.md)
      (*[texファイルが存在する既存ドキュメント](org/agcm5.4.zip)と[AGCM5.6-Tech.pdf](../org/AGCM5.6-Tech.pdf) がすでに異なるバージョンなので注意*)


---

# このプロジェクトのこれまでの経緯
## ことはじめ

[GCM セミナーのホームページ](https://ccsr.aori.u-tokyo.ac.jp/~miyakawa/limited/gcm/gcm-seminar.html)
にある[CCSR/NIES AGCM マニュアル解説編＆利用編](https://ccsr.aori.u-tokyo.ac.jp/~miyakawa/limited/gcm/documents/CCSR.NIES.AGCM.ver5.6.zip)
は 20 年以上前の資料であるにもかかわらず、いまだに学生がよく参照資料である。
ただし、非常に古い tex で作成されたため画像ファイルとなっており、使い勝手が悪い。

それを芳村さんに相談したところ、なんと、
(少なくとも Google Chrome で)command+F が可能な
[AGCM5.6-Tech.pdf](./org/AGCM5.6-Tech.pdf)
[AGCM5.6-Using.pdf](./org/AGCM5.6_Using.pdf)
及び、大元の tex ファイルを含む
[agcm5.4.tar.bz2](./org/agcm5.4.tar.bz2)
を持っていて、くれた。

## とりあえず木野が立ち上げた時点での目標

- **できるだけオープンかつ持続性のあるドキュメントを作成する**
- 理想的には：天気や気象研究ノートなどの雑誌に載せる(1 年くらい前に三浦さんがぼそっと言ってた)ことができれば、著作者を明確にしつつオープンな（ググってヒットするような）ドキュメントにできる。

## 2020.04
立ち上げ、既存資料を集めた

## 5月なかばに方針整理
- 資料整理、進行計画を立てる - [issue](https://gitlab.com/kanonundgigue/modeldescription/-/tree/structure) (木野・堀田)
  モデルの開発の歴史と照らし合わせてどこが抜けているか明示しただけでも、有用な資料になりそうだ [Table_Of_Contents.md](./doc/Table_Of_Contents.md) -> ここまでできた時点で、他の学生に展開できそう？
- 当面の目標: **MIROC6の資料としてアップデートする**
 長期的には、オープンなドキュメントを作成したい、さらには統合のMIROC7資料のコミットしたい、という野望を抱きつつも、まずはCCSRの学生にとって有用な、内輪向けのドキュメントをつくる。　
 
- 小目標: **有志でゆるゆる作業するための筋道を立てる**
  
## 2020.05.26 POCKIEで決まった方向性

- 活動期間は予算の都合上、2021.03まで
- 最終的に揃えるドキュメントは英語
- 各章の内容に詳しい先生方や研究者が、監修（査読）してくださる

## 2020.06.26 POCKIE
- 学生の積極性を好意的に受け取っていただけた、思うようにすすめられそう。
[発表資料Google slides](https://docs.google.com/presentation/d/1dHqW8_K4n0qfBhwjE8p25tSqCbfk1Sk7VRfBY8V_01U/edit)

---

moved from GitLab to GitHub on 20200521

Startup by kanonkino (kanon@aori.u-tokyo.ac.jp) on 20200416
