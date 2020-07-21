## 大気・地表系の拡散型収支式の解法

### 基本的な解法

放射, 鉛直拡散, 接地境界層・地表過程は
一括して一部の項を implicit 扱いで
時間変化項を計算し, 最後に時間積分を行なう.
ベクトル量 <span>q</span> の時間変化項として,
Euler 法で扱う項 TERM00000 と implicit 法で扱う項 TERM00001 とに分けて考える.

> EQ=00000.

一般の場合にこれを解くことは困難であるが,
近似的に TERM00002 を線形化することにより解くことが可能となる.

> EQ=00001.

のように行列 TERM00003 を用いて線形化する.
ここで,

> EQ=00002.

である.
すると,
TERM00004
と書けば,

> EQ=00003.

これは, 行列演算で原理的には簡単に解くことができる.

### 基本方程式

放射, 鉛直拡散, 接地境界層・地表過程の
方程式は, 基本的に以下のように表わされる.

> EQ=00051.  
> EQ=00051.  
> EQ=00051.  
> EQ=00051.  
> EQ=00051.

ここで, TERM00005,TERM00005 は
鉛直拡散による, それぞれ TERM00006,TERM00006
の鉛直上向きフラックス密度である.
また, TERM00007 は放射による
鉛直上向きエネルギーフラックス密度である.

大気は, TERM00008 を座標系で離散化される.
風速, 気温等は層 TERM00009 で定義される.
フラックスは, 層の境界 TERM00010 で定義される.
下層から上層に TERM00011 が増大する.
また, TERM00012,
TERM00013 である.
TERM00014 座標は, 鉛直1次元過程を考えている限りは,
定数(TERM00015)倍の違いを除いては TERM00016 座標と同じであると考えてよい.
ここで,

> EQ=00004.

> EQ=00005.

と書く.

### implicit時間差分

鉛直拡散項などの線形化できる項に関しては, implicit法を用いる.
拡散係数なども予報変数に依存するが,
その係数は最初に求めるだけで, 反復的に解くことはしない.
ただし, 安定性の向上のために時間ステップの扱いを工夫している(後述).

例えば, 離散化した TERM00017 の方程式([\[u-eq.orig\]](#u-eq.orig))は,

> EQ=00006.

ここで, TERM00018 は時間ステップである.
TERM00019 等は, TERM00020 の関数であるから, その依存性を線形化して,

> EQ=00007.
> <span id="u-flux.next" label="u-flux.next">\[u-flux.next\]</span>

従って, TERM00021 と置くと,

> EQ=00008.

すなわち,

> EQ=00009.

これは, 以下のような行列形式で書くことができる.

> EQ=00010.

> EQ=00011.
> <span id="u-matrix" label="u-matrix">\[u-matrix\]</span>

これを LU 分解などの方法で解けば良い.
通常は, TERM00022 は3重対角となるので, 簡単に解ける.
解いた後は, ([\[u-flux.next\]](#u-flux.next))を用いて
この方法にコンシステントなフラックスを計算しておく.
TERM00023 についても全く同様である.

### implicit時間差分の結合

気温, 比湿, 地中温度については, 前節のように簡単にはいかない.

> EQ=00052.  
> <span id="deq-theta" label="deq-theta">\[deq-theta\]</span>
> EQ=00052.

> EQ=00012.
> <span id="deq-q" label="deq-q">\[deq-q\]</span>

> EQ=00013.
> <span id="deq-g" label="deq-g">\[deq-g\]</span>

ここで, 上記の式における TERM00024, TERM00025 は
TERM00026, TERM00027 から取っていることに注意. なぜならば,
地表でのフラックスは, 以下のようになるからである.

> EQ=00014.

> EQ=00015.

> EQ=00016.

ここで, 地表面表皮温度を TERM00028 とすると,
TERM00029, TERM00030 (飽和比湿), TERM00031 である.
これらは, 全て, TERM00032 に依存する.
また, TERM00033 は, 全ての TERM00034 での値が TERM00035 に依存する.

([\[u-matrix\]](#u-matrix)) と同様に, 行列 TERM00036,TERM00036 を用いて
([\[deq-theta\]](#deq-theta)), ([\[deq-q\]](#deq-q)), ([\[deq-g\]](#deq-g)) を書き直すと,
TERM00037 (TERM00038,TERM00038 について) または TERM00039 (TERM00040 について) のとき,

> EQ=00053.  
> <span id="comb-theta2" label="comb-theta2">\[comb-theta2\]</span>
> EQ=00053.

> EQ=00017.
> <span id="comb-q2" label="comb-q2">\[comb-q2\]</span>

> EQ=00018.
> <span id="comb-g2" label="comb-g2">\[comb-g2\]</span>

ただし,

> EQ=00019.

> EQ=00020.

> EQ=00021.

TERM00041 (TERM00042,TERM00042 について) または TERM00043 (TERM00044 について) のとき,

> EQ=00054.  
> EQ=00054.  
> <span id="comb-theta" label="comb-theta">\[comb-theta\]</span>
> EQ=00054.

> EQ=00022.
> <span id="comb-q" label="comb-q">\[comb-q\]</span>

> EQ=00055.  
> EQ=00055.  
> <span id="comb-g" label="comb-g">\[comb-g\]</span>
> EQ=00055.

ただし,

> EQ=00023.

> EQ=00024.

> EQ=00025.

ただし, ([\[comb-g\]](#comb-g))は, 地表面のバランスの条件

> EQ=00026.

を, 土壌温度の式の TERM00045 の場合として扱ったもので,
([\[deq-g\]](#deq-g))の表式には含まれていないことに注意.

これら,
([\[comb-theta2\]](#comb-theta2)), ([\[comb-q2\]](#comb-q2)), ([\[comb-g2\]](#comb-g2)),
([\[comb-theta\]](#comb-theta)), ([\[comb-q\]](#comb-q)), ([\[comb-g\]](#comb-g))
を連立すると, TERM00046 個の未知変数に関して,
同数の方程式があるので, 解くことができる.
実際の解法としては, LU分解を用いて行なうことができる.

解いた後は,
([\[u-flux.next\]](#u-flux.next)) と同様に,
コンシステントなフラックスを求めておく.

### 時間差分の結合式の解法

([\[comb-theta\]](#comb-theta)) などは, 以下のように書ける.

> EQ=00027.

ここで, TERM00047,TERM00047
の項は地表フラックスに伴う項,
その他は鉛直拡散に伴う項である.
ここで, 上下を逆にして行列で表現すると, 以下のようになる.

> EQ=00028.

いま, 表記の簡単のために, TERM00048 とする. 以後の議論は, これによって一般性
を失うことはない.

> EQ=00029.

ここで,
TERM00049,TERM00049 としたときの式,
(地表でのフラックス交換を考えない場合にあたる)
を LU 分解で解くことを考える.

> EQ=00030.
> <span id="solve-0" label="solve-0">\[solve-0\]</span>

LU 分解すると,

> EQ=00031.

これから,

> EQ=00032.
> <span id="solve-z" label="solve-z">\[solve-z\]</span>

を TERM00050 について解き(TERM00051 から出発すれば, 簡単に解ける),
それから,

> EQ=00033.

を, TERM00052 について, TERM00053 から出発して順に解くことができる.

TERM00054,TERM00054 だと, LU 分解は,

> EQ=00034.

これから,

> EQ=00035.

だが, これと, ([\[solve-z\]](#solve-z)) を見比べると, 以下の関係があることがわかる.

> EQ=00036.

これを用いると,

> EQ=00037.
> <span id="solve-x" label="solve-x">\[solve-x\]</span>

となる. すなわち,

> EQ=00038.
> <span id="solve-1" label="solve-1">\[solve-1\]</span>

ここで, TERM00055 および, TERM00056 は,
TERM00057 とおいた式([\[solve-0\]](#solve-0)),
すなわち, 地表フラックスの項を考慮しない式で
LU分解を行なうことによって得られることに注意したい.
これらの項の物理的な意味としては,
地表面とのフラックス交換過程において,
大気全体が, 熱容量 TERM00058 を持ち,
上からフラックス TERM00059 が
供給される1つの層とみなすことができることを示す.

([\[comb-theta2\]](#comb-theta2))および([\[comb-theta\]](#comb-theta)),
([\[comb-q2\]](#comb-q2))および([\[comb-q\]](#comb-q)),
([\[comb-g2\]](#comb-g2))および([\[comb-g\]](#comb-g)) のそれぞれにおいて
([\[solve-1\]](#solve-1)) に対応する式が得られ, 以下のようになる.

> EQ=00039.

> EQ=00040.

> EQ=00041.

従って, 上の3式を連立させれば,
未知変数 TERM00060,TERM00060 を解くことができる.
これらが解ければ, 後は
([\[solve-x\]](#solve-x)) を順次 TERM00061,TERM00061 と解くことができる.
その後, 得られた温度にコンシステントなフラックスを

> EQ=00056.  
> EQ=00056.

として計算する.
ここでは, TERM00062 が一般行列の場合を示したが,
実際には3重対角行列となるので, さらに簡単である.

プログラム中においては,
`MODULE:[VFTND1(pimtx.F)]` で大気部分について,
`MODULE:[GNDHT1(pggnd.F)]` で地中部分について, LU分解解法の前半
(TERM00063 を求めるところ)を行ない,
`MODULE:[SLVSFC(pgslv.F)]` において, TERM00064 の方程式を解き,
TERM00065,TERM00065 を求めている.
その後, `MODULE:[GNDHT2(pggnd.F)]` において
LU分解解法の後半を行ない, 地中について温度変化率を解き,
収支が合うようにフラックスを補正する.
また, `MODULE:[VFTND2(pimtx.F)]` において大気中について
温度変化率を解き,
`MODULE:[FLXCOR(pimtx.F)]` でフラックスを補正している.

### 時間差分の結合式

TERM00066,TERM00066 を求める結合式は,
以下の様に条件を変えながら 3回解く.

1.  地表湿潤度 TERM00067 を 1 として解く. 地表温度は変数.

2.  `MODULE:[GNDBET]` で得られた地表湿潤度で解く.
    地表温度は変数.

3.  `MODULE:[GNDBET]` で得られた地表湿潤度で解く.
    融雪等の場合, 地表温度は氷点に固定.

1 回目の計算は, 可能蒸発量 TERM00068 を見積もるために行なわれる.
(地表湿潤度が小さいときに, モデルのエネルギーバランスから
得られた TERM00069 を用いて, 可能蒸発量を
TERM00070
として診断すると, 非現実的な大きな値になってしまう.)
可能蒸発量は,

> EQ=00057.

となる.
添字 TERM00071 は, 補正後の意味で,
これが得られた温度等にコンシステントなフラックスである.

2 回目以降の計算では,

1.  1回めの計算で求めた可能蒸発量に
    地表湿潤度(蒸発効率) TERM00072 を
    かけたものを蒸発量 TERM00073 とする.
    
    > EQ=00042.

2.  蒸発量 TERM00074 は
    
    > EQ=00043.
    
    で求められるものとして,
    改めてエネルギーバランスを解き直す.

の2通りの蒸発量の計算方法を用いることができる
(標準では1.の方法を用いる).
3 回目の計算は, 融雪, 融氷のときや, 混合層海洋で海氷が生成するときに
地表温度を氷点などに固定してエネルギーバランスを解くために行なう.
このとき, 融雪などの水の相変化に使われるエネルギー量が診断的に求まり,
後で融雪量などを計算する際に用いられる.

結合式の具体的な形は以下の様である.

> EQ=00058.  
> <span id="combin-eq" label="combin-eq">\[combin-eq\]</span>
> EQ=00058.

ここで, TERM00075,TERM00075 および TERM00076,TERM00076 は,
LU分解解法の前半を行なって得られる, 行列およびベクトルの成分である.
地表面が雪または氷に覆われているときには, 潜熱 TERM00077 の代わりに
昇華の潜熱 TERM00078 を用いる. TERM00079 は水の融解の潜熱である.
ただし, 第2回めの計算で,
蒸発の見積もりとして第一の方法を用いた場合は, 以下のようになる.

> EQ=00059.  
> EQ=00059.

3 回目の計算で, 地表温度を固定した場合の結合式は,

> EQ=00060.  
> <span id="combin-eq3" label="combin-eq3">\[combin-eq3\]</span>
> EQ=00060.

ここで, TERM00080 は固定する温度までの変化率で,

> EQ=00044.

TERM00081 は, 融雪, 融氷の場合は 273.15K,
海氷の生成の場合は 271.15K である.
また, 蒸発計算の第2の方法を用いる場合には,
同様に TERM00082 のかわりに TERM00083 を用い,
TERM00084 の微分項を 0 として計算する.
このとき,

> EQ=00061.  
> EQ=00061.

で計算される TERM00085 は地表エネルギーバランスで,
水の相変化に使われる分のエネルギーである.

### implicit 時間差分における時間ステップの扱い

鉛直拡散項の時間差分には implicit 法を用いているが,
一般に拡散係数が非線形であり, この係数を explicit に評価している
ことにより, 数値不安定の問題が生じ得る.
安定性の向上のために, Kalnay and Kanamitsu (19??) にならって
時間ステップの扱いを工夫している.

簡単化のために以下の常微分方程式を例に取って説明する.

> EQ=00045.

係数 TERM00086 が非線形性を表す.
係数のみ explicit に評価して素直に implicit 差分化すると次式のようになる.

> EQ=00046.
> <span id="normal-fd" label="normal-fd">\[normal-fd\]</span>

ところが, ここでは 2ステップ先の TERM00087 の値 TERM00088 を考えて,

> EQ=00047.
> <span id="modify-fd1" label="modify-fd1">\[modify-fd1\]</span>

> EQ=00048.
> <span id="modify-fd2" label="modify-fd2">\[modify-fd2\]</span>

とする.
一般に, ([\[modify-fd1\]](#modify-fd1)), ([\[modify-fd2\]](#modify-fd2)) のようにする方が
([\[normal-fd\]](#normal-fd))よりも安定性が良いことが知られている.

([\[modify-fd1\]](#modify-fd1)), ([\[modify-fd2\]](#modify-fd2)) を, 時間変化率を求める
形に書き直すと以下を得る.

> EQ=00049.

> EQ=00050.

すなわち, 時間変化率を求める際の時間ステップには,
時間積分のステップの 2 倍を用いる.