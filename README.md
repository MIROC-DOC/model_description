**このリポジトリ内の資料は全て公開予定です(ライセンス検討中)**

# プロジェクトの目標

**統合の 2020 年度後半の予算をつかって、年度末までに MIROC6 agcm の英語ドキュメント完成**
-> 詳細は[POCKIE の芳村先生資料](https://atm-phys.nies.go.jp/~fswiki/miroc/wiki.cgi?page=POCKIE%A5%DF%A1%BC%A5%C6%A5%A3%A5%F3%A5%B0+%282020%2D06%2D26%29&file=20200626%5FPOCKIE%5FMIROCdescription%2Epptx&action=ATTACH)

## タスクリスト

### 沼口さん資料の書式変換、英訳 -> 齋藤冬樹さんにご協力いただき、概ね完了(2020.07.22)

### 年度末にどんな形でまとめるか決定

-   doi 取得など、できるだけ実績としてオフィシャルなものになるよう先生方が検討してくださる。公開範囲と関連。

### 執筆者の確定。監修者とつないで、各セクションの方針設定

## 公開範囲

-   GitHub の公開リポジトリを予定。

## 誰が作業するか

-   新規執筆は基本的に、東大の GCM セミナーに参加している博士学生。それで埋まらないところは統合の先生方が検討。
-   先生方が監修・査読してくださる。

---

# 開発の手引き

-   [develop.md](./memo/develop.md)
-   ドキュメントの目次 [contesnts.md](./reference/contents.md)
    (_tex ファイルが存在する既存ドキュメント(agcm5.4.zip;内部資料))と[AGCM5.6-Tech.pdf](./org/AGCM5.6-Tech.pdf) がすでに異なるバージョンなので注意_)

---

# 自動変換作業

## Evacuation of problematic LaTeX tokens before succeeding conversion

There are some problematic LaTeX tokens in the original source files,
which may damage the conversion at some stages. A helper script,
`parse_jp.py` can evacuate those tokens to replace with normal (safer)
words.  At the moment, only functions to save the tokens are
implemented.  In other words, restoring is not implemented in the
script, but thankfully, `embed.py` in the next section can work as an
alternate.

### Requirement

`parse_jp.py` requires `python` version 3, and the package `pyparsing`
for lexical analysis of the source.

There are two python files: `parse_jp.py` and `psitex.py`.  The former
controls replacement of those specific to MIROC document.  The latter
is a (relatively) general module to parse LaTeX sources, which is
originally developed for another objective.

Although `plastex` may work better for this purpose, the maintainer
was not familiar with `plastex` in the beginning of this (psiTeX)
project.

### Usage

A typical usage is as follows:
```bash
% ./parse_jp.py -S -L -D -M -Td -Eq -d tex_jpx tex_jp/agcm.tex
% ls tex_jpx
a-intro.tex  d-hori.tex  p-dif.tex    p-sflx.tex
a-setup.tex  d-summ.tex  p-grav.tex   p-solv.tex
agcm.json    d-time.tex  p-intro.tex  referenc.tex
agcm.tex     d-vert.tex  p-lsc.tex    summary.tex
c-intro.tex  p-adj.tex   p-rad.tex
d-basic.tex  p-cum.tex   p-sfc.tex
```
Results are written under `tex_jpx` directory.
The file `agcm.json` contains all the information for later use.

### Reference of command-line arguments

#### Math elements and environments  (`-M`)
Inline math elements, (e.g., `$u$`) are replaced with `-M` argument.

```bash
% ./parse_jp.sh -M tex_jp/a-intro.tex
```

Results:

    (original)....
    ここで, $S$ は予報変数$u,v,T,p_S,q$などの関数であるが,

    (replaced)....
    ここで, TERM00007 は予報変数 TERM00008,TERM00008 などの関数であるが,

If the element contains at least one comma (as `TERM00008`), it is
replaced with emulating multiple words, in order to prepare correct
translation into English.

```bash
% ./parse_jp.sh -M tex_jp/d-summ.textbf
unit/chem token (Jkg:^{-1}:K)
unit/chem token (Jkg:^{-1}:K)
:
```

Results:

    (original)....
    (461Jkg$^{-1}$K$^{-1}$)

    (replaced)....
    (461 TERM00007TERM00008)

If an inline math element looks like a part of unit or a chemical
term, the tokens before the element are also replaced.

Math environments such as `equation`, `eqnarray`, `displaymath` are
replaced with the same number of equations.

```bash
% ./parse_jp.sh -M tex_jp/a-intro.tex
```

Results:

    (original)
    \begin{eqnarray}
      \DP{u}{t} & = & \left( {\cal F}_x \right)_D + \left( {\cal F}_x \right)_P 
      \label{struct:u-eq-1} \\
      \DP{v}{t} & = & \left( {\cal F}_y \right)_D + \left( {\cal F}_y \right)_P \\
      \DP{T}{t} & = & \left( Q \right)_D + \left( Q \right)_P \\
      \DP{p_S}{t} & = & \left( M \right)_D + \left( M \right)_P \\
      \DP{q}{t} & = & \left( S \right)_D + \left( S \right)_P \\
      \DP{T_g}{t} & = & \left( Q_g \right)_D + \left( Q_g \right)_P 
    \end{eqnarray}

    (replaced)....
    \begin{eqnarray}
    EQ=00004.
    EQ=00004.
    EQ=00004.
    EQ=00004.
    EQ=00004.
    EQ=00004.
    \end{eqnarray}

The number of equations is preserved.  `\label` macros are deleted.

#### Math environments replacement (`-Eq` `-Eqq`)

Math environments, (e.g., `equation`) can be converted to another
environments with `-E` argument (need `-M` to set).

```bash
% ./parse_jp.sh -M -Eq tex_jp/a-intro.tex
```

Results:

    (replaced)...
    \begin{quote}
    EQ=00004.
    EQ=00004.
    EQ=00004.
    EQ=00004.
    EQ=00004.
    EQ=00004.
    \end{quote}

Using `-Eq` or `-Eqq` they are converted to `quote` or `quotation`.

#### Tabular environments replacement (`-Td`)

Tabular environments, (at the moment `tabular` only) can be converted
to another environments with `-T` argument.

```bash
% ./parse_jp.sh -Td tex_jp/a-intro.tex
```
Results:

    (original)....
    \begin{tabular}{lll}
    東西風速 & $u$ ($\lambda,\varphi,\sigma$) & [m/s] \\
    南北風速 & $v$ ($\lambda,\varphi,\sigma$) & [m/s] \\
    :


    (replaced)....
    \begin{description}
    \item[TAB00000:0.0] 東西風速
    \item[TAB00000:0.1] $u$ ($\lambda,\varphi,\sigma$)
    \item[TAB00000:0.2] [m/s]
    \item[TAB00000:1.0] 南北風速
    :

Using `-Td` they are converted to `description`.

#### Dennou macros replacement (`-D`)

```bash
% ./parse_jp.sh -D tex_jp/a-intro.tex
```

Results:

    (original)....
    \begin{eqnarray}
      \DP{u}{t} & = & \left( {\cal F}_x \right)_D + \left( {\cal F}_x \right)_P 
      \label{struct:u-eq-1} \\
      \DP{v}{t} & = & \left( {\cal F}_y \right)_D + \left( {\cal F}_y \right)_P \\
      \DP{T}{t} & = & \left( Q \right)_D + \left( Q \right)_P \\
      \DP{p_S}{t} & = & \left( M \right)_D + \left( M \right)_P \\
      \DP{q}{t} & = & \left( S \right)_D + \left( S \right)_P \\
      \DP{T_g}{t} & = & \left( Q_g \right)_D + \left( Q_g \right)_P 
    \end{eqnarray}

    (replaced)....
    \begin{eqnarray}
      \frac{\partial{u}}{\partial {t}} & = & \left( {\cal F}_x \right)_D + \left( {\cal F}_x \right)_P
      \label{struct:u-eq-1} \\
      \frac{\partial{v}}{\partial {t}} & = & \left( {\cal F}_y \right)_D + \left( {\cal F}_y \right)_P \\
      \frac{\partial{T}}{\partial {t}} & = & \left( Q \right)_D + \left( Q \right)_P \\
      \frac{\partial{p_S}}{\partial {t}} & = & \left( M \right)_D + \left( M \right)_P \\
      \frac{\partial{q}}{\partial {t}} & = & \left( S \right)_D + \left( S \right)_P \\
      \frac{\partial{T_g}}{\partial {t}} & = & \left( Q_g \right)_D + \left( Q_g \right)_P
    \end{eqnarray}

Currently `\DP`, `\DD`, `\Dvect` and `\Dinclude` are expanded to
corresponding normal LaTeX macros.

#### Label and reference replacement (`-L`)

Equation numbers and their references can be converted to numbers
with `-L` argument.  In other words, `\ref{LABEL}` is replaced to
corresponding reference numbers.
Reference number starts from 1 for each input file.  If the file
inclusion is enabled (`-S`, see the next section) the numbers are kept
until the end of the document.
Since numbering is emulated as a standard LaTeX scheme, the numbers
should be identical to the original document.  If not, please inform
to the maintainer.

```bash
% ./parse_jp.sh -L tex_jp/a-intro.tex
```

Results:

    予報方程式の時間積分は,
    (\ref{struct:u-eq-1})などの
    左辺を差分で近似することによって行なう. 例えば,
    :
    \begin{eqnarray}
      \DP{u}{t} & = & \left( {\cal F}_x \right)_D + \left( {\cal F}_x \right)_P 
      \label{struct:u-eq-1} \\

    予報方程式の時間積分は,
    (1)などの
    左辺を差分で近似することによって行なう. 例えば,
    :
    \begin{eqnarray}
      \DP{u}{t} & = & \left( {\cal F}_x \right)_D + \left( {\cal F}_x \right)_P 
      \label{struct:u-eq-1}  \EQN{1}\\

`\EQN{}` is not a standard macro and used for a placeholder.

Using `-M -Eq` together, they are converted as follows:

```bash
% ./parse_jp.sh -M -Eq -L tex_jp/a-intro.tex
```

Results:

    \begin{quote}
    EQ=00004.    --- (1)
    EQ=00004.    --- (2)
    EQ=00004.    --- (3)
    EQ=00004.    --- (4)
    EQ=00004.    --- (5)
    EQ=00004.    --- (6)
    \end{quote}

#### Subfiles inclusion (`-S`)

External files (with macros `\input`, `\include`) are not parsed
default.  Using `-S`, they are also parsed and transformed.
Note that the external files using `\Dinclude`, `-D` is required.
If `-d DIRECTORY` is set, the result of each subfile is written under
`DIRECTORY`.

```bash
% ./parse_jp.sh -D -S tex_jp/agcm.tex  # to standard output
% ./parse_jp.sh -d dest -D -S tex_jp/agcm.tex  # written under dest/.
```
#### Miscellaneous

Run `./parse_jp.sh -h` to show the usage.


## 英訳 markdown へ数式・表を埋め込む

```bash
# ディレクトリに入る
cd org

# 1ファイルのみ実行
python embed.py a-intro

# ディレクトリ内の全ファイル実行
python embed.py
```

-   `org/md_enorg/*.md` 入力元の英訳ファイル
-   `org/tex_jpx/*.json` エスケープされた数式
-   `org/md_en/*.md` 出力先 (`md_en`へのシンボリックリンク)
-   `org/embed_log/*.json` 埋め込み時のアラートがはき出される

---

# このプロジェクトのこれまでの経緯

## ことはじめ

[GCM セミナーのホームページ](https://ccsr.aori.u-tokyo.ac.jp/~miyakawa/limited/gcm/gcm-seminar.html)
にある[CCSR/NIES AGCM マニュアル解説編＆利用編](https://ccsr.aori.u-tokyo.ac.jp/~miyakawa/limited/gcm/documents/CCSR.NIES.AGCM.ver5.6.zip)
は 20 年前の資料であるにも関わらず、いまだに学生がよく参照する資料である。
ただし、非常に古い tex で作成されたため画像ファイルとなっており、使い勝手が悪かった。

芳村先生が(少なくとも Google Chrome で)command+F 検索が可能な
[AGCM5.6-Tech.pdf](./org/AGCM5.6-Tech.pdf)
[AGCM5.6-Using.pdf](./org/AGCM5.6_Using.pdf)
及び、大元の tex ファイルを含む
agcm5.4.zip(内部資料)
を持ってくださっていた。この内容をアップデートしたい。

## 2020 年度に限らない、長期目標

-   **できるだけオープンかつ持続性のあるドキュメントを作成する**
-   MIROC グループ内で質問しやすい環境を作る

## 2020.04

立ち上げ、既存資料を集めた。Git を使った作業フローを検討（木野・高野・堀田）

## 5 月なかばに方針整理

-   資料整理、進行計画を立てる - (木野・堀田) モデルの開発の歴史と照らし合わせてどこが抜けているか明示しただけでも、有用な資料になりそう [Table_Of_Contents.md](./reference/Table_Of_Contents.md)

## 2020.05.26 POCKIE で決まった方向性

-   活動期間は予算の都合上、2021.03 まで
-   最終的に揃えるドキュメントは英語
-   各章の内容に詳しい先生方や研究者が、監修（査読）してくださる

## 2020.06.26 POCKIE

-   学生の積極性を好意的に受け取っていただけた。GitHub 上で作業を進められそう。
    [発表資料 Google slides](https://docs.google.com/presentation/d/1dHqW8_K4n0qfBhwjE8p25tSqCbfk1Sk7VRfBY8V_01U/edit)

---

moved from GitLab to GitHub on 20200521

Startup by kanonkino (kanon@aori.u-tokyo.ac.jp) on 20200416
