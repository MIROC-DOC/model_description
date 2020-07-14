**このリポジトリ内の資料は全て公開予定です(ライセンス検討中)**

# プロジェクトの目標
**統合の2020年度後半の予算をつかって、年度末までにMIROC6 agcmの英語ドキュメント完成** 
-> 詳細は[POCKIEの芳村先生資料](https://atm-phys.nies.go.jp/~fswiki/miroc/wiki.cgi?page=POCKIE%A5%DF%A1%BC%A5%C6%A5%A3%A5%F3%A5%B0+%282020%2D06%2D26%29&file=20200626%5FPOCKIE%5FMIROCdescription%2Epptx&action=ATTACH)

## タスクリスト

### 本格稼働用のGitHubリポジトリの整備
 
### 既存資料の書式変換、英訳 -> 齋藤冬樹さんにご協力いただき、なるべくフローを自動化するよう作業中(2020.07)

### 年度末にどんな形でまとめるか決定
- doi取得など、できるだけ実績としてオフィシャルなものになるよう先生方が検討してくださる。公開範囲と関連。

### 既存資料の収集

## 公開範囲

- GitHubの公開リポジトリを予定。

## 誰が作業するか

- 新規執筆は基本的に、東大のGCMセミナーに参加している博士学生。それで埋まらないところは統合の先生方が検討。
- 先生方が監修・査読してくださる。

---

# 開発の手引き

- [develop.md](./memo/develop.md)
-  ドキュメントの目次 [contesnts.md](./reference/contents.md)
      (*texファイルが存在する既存ドキュメント(agcm5.4.zip;内部資料))と[AGCM5.6-Tech.pdf](./org/AGCM5.6-Tech.pdf) がすでに異なるバージョンなので注意*)


---

# このプロジェクトのこれまでの経緯
## ことはじめ

[GCM セミナーのホームページ](https://ccsr.aori.u-tokyo.ac.jp/~miyakawa/limited/gcm/gcm-seminar.html)
にある[CCSR/NIES AGCM マニュアル解説編＆利用編](https://ccsr.aori.u-tokyo.ac.jp/~miyakawa/limited/gcm/documents/CCSR.NIES.AGCM.ver5.6.zip)
は 20 年前の資料であるにも関わらず、いまだに学生がよく参照する資料である。
ただし、非常に古い tex で作成されたため画像ファイルとなっており、使い勝手が悪かった。

芳村先生が(少なくとも Google Chrome で)command+F検索が可能な
[AGCM5.6-Tech.pdf](./org/AGCM5.6-Tech.pdf)
[AGCM5.6-Using.pdf](./org/AGCM5.6_Using.pdf)
及び、大元の tex ファイルを含む
agcm5.4.zip(内部資料)
を持ってくださっていた。この内容をアップデートしたい。

## 2020年度に限らない、長期目標

- **できるだけオープンかつ持続性のあるドキュメントを作成する**
- MIROCグループ内で質問しやすい環境を作る

## 2020.04
立ち上げ、既存資料を集めた。Gitを使った作業フローを検討（木野・高野・堀田）

## 5月なかばに方針整理
- 資料整理、進行計画を立てる - (木野・堀田) モデルの開発の歴史と照らし合わせてどこが抜けているか明示しただけでも、有用な資料になりそう [Table_Of_Contents.md](./reference/Table_Of_Contents.md)
  
## 2020.05.26 POCKIEで決まった方向性

- 活動期間は予算の都合上、2021.03まで
- 最終的に揃えるドキュメントは英語
- 各章の内容に詳しい先生方や研究者が、監修（査読）してくださる

## 2020.06.26 POCKIE
- 学生の積極性を好意的に受け取っていただけた。GitHub上で作業を進められそう。
[発表資料Google slides](https://docs.google.com/presentation/d/1dHqW8_K4n0qfBhwjE8p25tSqCbfk1Sk7VRfBY8V_01U/edit)

---

moved from GitLab to GitHub on 20200521

Startup by kanonkino (kanon@aori.u-tokyo.ac.jp) on 20200416
