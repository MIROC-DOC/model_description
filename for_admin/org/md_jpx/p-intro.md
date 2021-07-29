# 物理過程

## 物理過程の概要

物理過程として, 以下のような過程を考える

  - 積雲対流過程

  - 大規模凝結過程

  - 放射過程

  - 鉛直拡散過程

  - 地表フラックス

  - 地表面・地中過程

  - 重力波抵抗

これらの過程による予報変数の時間変化項 TERM00436,TERM00436 を計算し, 時間積分を行なう. また, 大気・地表フラックスを評価するために 地表面サブモデルを利用する. 地表面サブモデルにおいては, 地中温度 TERM00437, 地中水分 TERM00438, 積雪量 TERM00439 などを 予報変数として用いている.

### 基本方程式

TERM00440 座標系の大気の運動方程式, 熱力学の式, 水蒸気などの物質の連続の式を考える. 運動量, 熱, 水蒸気等の鉛直方向のフラックスを考慮し, その収束による時間変化を求める. 鉛直フラックスは全て上向きを正とする.

1.  運動方程式
    
        EQ=00157.
    
        EQ=00158.
    
    TERM00441,TERM00441: 東西, 南北風; TERM00442,TERM00442: それらの鉛直フラックス.

2.  熱力学の式
    
        EQ=00159.
    
    TERM00443: 温度; TERM00444: 定圧比熱; TERM00445: 温位; TERM00446: 鉛直顕熱フラックス; TERM00447: 鉛直放射フラックス.
    
    ここで, TERM00448 とおくと, これは,
    
        EQ=00160.
    
    鉛直1次元過程を考える限りにおいては, TERM00449 の代わりに TERM00450 を考えればよい. 以下, 簡単のために, 混同のおそれがない限り, TERM00451 を TERM00452 と書く.

3.  水蒸気の連続の式
    
        EQ=00161.
    
    TERM00453: 比湿; TERM00454: 鉛直水蒸気フラックス.
    
    ### 地中の基本方程式
    
    下向きを正とした TERM00455 座標で考える. やはり鉛直フラックスは全て上向きを正とする.

4.  熱の式
    
        EQ=00162.
    
    TERM00456: 地中温度; TERM00457: 定圧比熱; TERM00458: 鉛直熱フラックス; TERM00459; 加熱項(相変化などによる).

5.  地中水分の式
    
        EQ=00163.
    
    TERM00460: 地中水分; TERM00461: 鉛直水フラックス; TERM00462; 水のソース(流出など).

6.  エネルギーの収支式
    
    地表表面で, エネルギーのバランスが成立する.
    
        EQ=00164.
    
    TERM00463: 蒸発の潜熱; TERM00464: 地表エネルギーバランス(相変化などにともなう).

7.  地表の水の収支
    
        EQ=00165.
    
    TERM00465: 降水; TERM00466: 表面流出.

8.  雪の収支
    
        EQ=00166.
    
    TERM00467: 積雪量(kg/TERM00468); TERM00469: 降雪; TERM00470: 昇華; TERM00471: 融雪.

### 物理過程の時間積分法

予報変数の時間積分の観点から物理過程を分類すると, 実行順に以下の3つに分けることができる.

1.  積雲対流および大規模凝結

2.  放射, 鉛直拡散, 接地境界層・地表過程

3.  重力波抵抗, 質量調節, 乾燥対流調節

積雲対流および大規模凝結は,

    EQ=00167.

    EQ=00168.

のように, 通常の Euler 差分によって値を順次更新する. 大規模凝結スキームには, 積雲対流スキームによって更新された値が受け渡されることに注意. 実際には, 積雲対流や大規模凝結のルーチンでは加熱率等が出力され, 時間積分はその直後の `MODULE:[GDINTG]` によって行なわれる.

次のグループの放射, 鉛直拡散, 接地境界層・地表過程 の計算は, 基本的には全てこの更新された値 ( TERM00472,TERM00472 等 ) を用いて行なわれる. ただし, 一部の項を implicit 扱いで計算するために, これらの項を全て一括して加熱率等を計算して, 最後に時間積分を行なう. すなわち, シンボリックに書けば,

    EQ=00169.

となる.

重力波抵抗, 質量調節, 乾燥対流調節に関しては, 積雲対流および大規模凝結と同様である.

    EQ=00170.

### 各種の物理量

予報変数から簡単な計算で求められる 各種の物理量の定義を示す. このうちいくつかは, `MODULE:[PSETUP]` で計算される.

1.  仮温度
    
    仮温度 TERM00473 は,
    
        EQ=00171.

2.  大気密度
    
    大気密度 TERM00474 は, 以下のように計算される.
    
        EQ=00172.

3.  高度
    
    高度 TERM00475 は, 力学過程での ジオポテンシャルの計算と同じ方式によって評価する.
    
        EQ=00173.
    
        EQ=00174.
    
        EQ=00175.

4.  層の境界の温度
    
    層の境界の温度は, TERM00476 すなわち TERM00477 に対する 線形補間を行なって計算する.
    
        EQ=00176.

5.  飽和比湿
    
    飽和比湿 TERM00478,TERM00478 は飽和蒸気圧 TERM00479 を用いて近似的に,
    
        EQ=00177.
    
    ここで, TERM00480 であり,
    
        EQ=00178.
    
    よって, 蒸発の潜熱 TERM00481, 水蒸気の気体定数 TERM00482 を一定とすれば,
    
        EQ=00179.
    
    TERM00483 \[Pa\] である.
    
    (199)より,
    
        EQ=00180.
    
    ここで, 温度が氷点 273.15K よりも低い場合には, 潜熱 TERM00484 として昇華の潜熱 TERM00485 を用いる.

6.  乾燥静的エネルギー, 湿潤静的エネルギー
    
    乾燥静的エネルギー TERM00486 は
    
        EQ=00181.
    
    湿潤静的エネルギー TERM00487 は
    
        EQ=00182.
    
    で定義される.