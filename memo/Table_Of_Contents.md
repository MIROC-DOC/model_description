## goal
* 従来のドキュメントに"そもそも存在してない"セクションがあるので、それらを整理して書き出す
* 大幅な更新の必要なセクションとそうでもないセクションの整理

## note

ドキュメント作成の元とするソースコードはOFP上の
/work/gi55/c24266/share/MIROC/MIROC6.0+O.tar.gz
を展開して、初期設定のままmakeしたときに、コンパイルされるファイル
論文の内容とソースコードが食い違う場合（多々ある）、コードを優先する。

MIROC3m, MIROC3h, MIROC4hの基本ドキュメントはHasumi and Emori, 2004
[https://ccsr.aori.u-tokyo.ac.jp/~hasumi/miroc_description.pdf](https://ccsr.aori.u-tokyo.ac.jp/~hasumi/miroc_description.pdf)
MIROC4mを使用するときは「Hasumi and Emori 2004 の地表面運動量フラックスのバグが修正されたバージョン」と記述しているので、記述論文はないはず

MIROC4hの記述論文はSakamoto et al. 2012
[https://www.jstage.jst.go.jp/article/jmsj/90/3/90_2012-301/_pdf/-char/ja](https://www.jstage.jst.go.jp/article/jmsj/90/3/90_2012-301/_pdf/-char/ja)

MIROC5の記述論文はWatanabe et al. 2010
[https://journals.ametsoc.org/doi/full/10.1175/2010JCLI3679.1](https://journals.ametsoc.org/doi/full/10.1175/2010JCLI3679.1)

MIROC6の記述論文はTatebe et al. 2019
[https://www.geosci-model-dev.net/12/2727/2019/](https://www.geosci-model-dev.net/12/2727/2019/gmd-12-2727-2019.pdf)

## history
2020/05/18 Haruka Hotta created this file
2020/05/20 Kanon Kino added some info.


## 力学過程 $GCMDIR/src/dynamics/
### 鉛直離散化
2003年にσ座標からhybrid σ-p座標へ
Arakawa and Konor 1996
[https://journals.ametsoc.org/doi/10.1175/1520-0493%281996%29124%3C0511%3AVDOTPE%3E2.0.CO%3B2](https://journals.ametsoc.org/doi/10.1175/1520-0493%281996%29124%3C0511%3AVDOTPE%3E2.0.CO%3B2)

### 水平離散化
### 時間離散化
### 拡散項等

## 物理過程 $GCMDIR/src/physics/
### 積雲対流(Chikira) pcumc.F 
Chikira and Sugiyama 2010; Chikira 2010
[https://journals.ametsoc.org/doi/full/10.1175/2010JAS3316.1](https://journals.ametsoc.org/doi/full/10.1175/2010JAS3316.1)
[https://journals.ametsoc.org/doi/full/10.1175/2010JAS3317.1](https://journals.ametsoc.org/doi/full/10.1175/2010JAS3317.1)

格子内にアンサンブルを仮定する、積雲対流の基本的な概念は共通
定式化は2000verと全く別

### 浅い積雲 pshcn.F
Park and Bretherton 2009
[https://journals.ametsoc.org/doi/full/10.1175/2008JCLI2557.1](https://journals.ametsoc.org/doi/full/10.1175/2008JCLI2557.1)
2000verには存在しない

### 大規模凝結 pmlsc.F
Watanabe et al. 2009
[https://link.springer.com/article/10.1007/s00382-008-0489-0](https://link.springer.com/article/10.1007/s00382-008-0489-0)
基礎となる考え方は2000verと共通
具体的な定式化は全く別

### 雲微物理 pcldphys.F
Wilson and Ballard 1998
[https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.49712555707](https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.49712555707)
2000verとは全く別

今後はMichibata et al. 2019も使われるようになっていく見込み。
[https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018MS001596](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018MS001596)
これはMIROC6とも別。

### 放射 pradmX.F, pradtX.F
Nakajima et al. 2000; Sekiguchi and Nakajima 2008
[https://www.osapublishing.org/ao/abstract.cfm?uri=ao-39-27-4869](https://www.osapublishing.org/ao/abstract.cfm?uri=ao-39-27-4869)
[https://www.sciencedirect.com/science/article/abs/pii/S0022407308001635?via%3Dihub](https://www.sciencedirect.com/science/article/abs/pii/S0022407308001635?via%3Dihub)
基本的概念・定式化は、2000verとほぼ一緒

### 乱流 pvdfm.F
2000verでは拡散フラックスの章に対応


### 地表フラックス
MIROC6では扱いなし
Hasumi and Emori (2004)以降、運動量フラックスも含めて、陸モデル&海洋モデルからカップラーを通して受け取るように仕様変更された。

### 地表モデル
MIROC6では扱いなし
Hasumi and Emori (2004)以降、AGCMの物理過程としての扱いはなくなった。->陸モデルMATSIRO(Takata et al. 2003)

### implicit 解法

### 重力波抵抗 pigwd.F

## モジュール的コンポーネント

### MATSIRO $GCMDIR/src/extensions/matsiro
2000verには存在しない

江守さんが書いた、MATSIROだけのドキュメントがある
[matsiro-description.tex](doc/matsiro-description.tex)

記述論文はTakata et al. 2003
[https://www.sciencedirect.com/science/article/pii/S0921818103000304](https://www.sciencedirect.com/science/article/pii/S0921818103000304)
MIROC6において、Nitta et al. 2014; 2017の内容がアップデートされた。（詳細にはTatebe et al 2019の記述を参照)
[https://doi.org/10.1175/JCLI-D-13-00310.1](https://doi.org/10.1175/JCLI-D-13-00310.1)
[https://journals.ametsoc.org/doi/10.1175/JHM-D-16-0105.1](https://journals.ametsoc.org/doi/10.1175/JHM-D-16-0105.1)

### SPRINTARS $GCMDIR/src/extensions/sprintars
エアロゾルモデル
Takemura et al. 2000;2002;2005;2009
[https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900265](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900265)
[https://journals.ametsoc.org/doi/full/10.1175/1520-0442%282002%29015%3C0333%3ASSAARF%3E2.0.CO%3B2](https://journals.ametsoc.org/doi/full/10.1175/1520-0442%282002%29015%3C0333%3ASSAARF%3E2.0.CO%3B2)
[https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2004JD005029](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2004JD005029)
[https://www.atmos-chem-phys.net/9/3061/2009/acp-9-3061-2009.html](https://www.atmos-chem-phys.net/9/3061/2009/acp-9-3061-2009.html)
2000verには存在しない

### COSP $GCMDIR/src/extensions/cosp*
雲のオンライン診断ツールで、モデルの結果に影響を与えるものではない。
Bodas et al, 2011; Swales et al. 2018
[https://journals.ametsoc.org/doi/pdf/10.1175/2011BAMS2856.1](https://journals.ametsoc.org/doi/pdf/10.1175/2011BAMS2856.1)
[https://www.geosci-model-dev.net/11/77/2018/](https://www.geosci-model-dev.net/11/77/2018/)
2000verには存在しない。中身や使い方の大まかな説明があってもよい。

### 海洋モデル(COCO?) $GCMDIR/src/ocean

英語だけど最強感ある Hasumi et al. 2015
[https://pdfs.semanticscholar.org/9e06/bd98573c875d8934f73944a9b89ae212f990.pdf](https://pdfs.semanticscholar.org/9e06/bd98573c875d8934f73944a9b89ae212f990.pdf)

##モデルの構造・コーディングルール・変数一覧
付録的なやつが意外と役に立つ説
