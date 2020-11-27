<!-- TOC -->

- [鉛直拡散](#鉛直拡散)
  - [接地境界層](#接地境界層)
  - [雲水量の診断](#雲水量の診断)
  - [安定度関数](#安定度関数)
  - [乱流の代表的長さスケール](#乱流の代表的長さスケール)
  - [大気境界層による補正](#大気境界層による補正)
  - [乱流量の予報式](#乱流量の予報式)
  - [乱流の生成散逸項](#乱流の生成散逸項)
  - [拡散係数の計算](#拡散係数の計算)
  - [フラックスの計算](#フラックスの計算)

<!-- /TOC -->
## 鉛直拡散
本章では、サブグリッドスケールの乱流を表現する鉛直拡散スキームについて記述する。鉛直拡散スキームでは、運動量、熱、および水蒸気などのトレーサーについて、鉛直フラックスとimplicit解を得るための微分値を出力する。また、後述する乱流量について時間発展を解くために必要な生成項、散逸項、鉛直フラックスを出力する。

鉛直拡散係数の見積もりにはNakanishi and Niino (2004)の改良Mellor-Yamada Level3乱流クロージャーモデル(MYNNモデル)を用いる。MYNNモデルでは、熱力学変数としてliquid water potential temperature $\theta_l$ およびtotal water content $q_w$ が使用され、それぞれ以下のように定義される。
$$ \theta_l=\frac{ T - \frac{L}{C_p}q_l - \frac{L+L_{M}}{C_p}q_i }{\left(\frac{p}{p_0}\right)^\kappa } $$
$$q_w=q_v+q_l+q_i$$
また、Level3モデルにおいては、乱流エネルギー $q^2/2=(\langle u^2 \rangle + \langle v^2 \rangle + \langle w^2 \rangle)/2$ および $\langle {\theta_l}^2 \rangle,\langle {q_w}^2 \rangle,\langle \theta_l q_w \rangle$ が予報変数となっており、これらの時間発展項もこのスキーム内で求められる。$\langle \ \rangle$はアンサンブル平均を表す。

計算手順の概略は以下の通りである。

1. 摩擦速度およびMonin-Obukhov長を計算する
2. 部分凝結を考慮して雲水量を計算する [`VDFCND`]
3. 安定度関数を計算する [`VDFLEV2`]
4. 大気境界層の深さを計算する [`PBLHGT`]
5. 乱流の代表的長さスケールを計算する [`VDFMLS`]
6. 乱流量の生成項と散逸項を計算する [`VDFLEV3`]
7. 拡散係数および鉛直フラックスとその微分値を計算する [`VDFLEV3`]

### 接地境界層
摩擦速度 $u^*$ およびMonin-Obukhov長 $L_M$ はそれぞれ以下のように与えられる。

$$u^*=\left(\sqrt{{F_u}^2+{F_v}^2}/\rho \right)^\frac{1}{2}$$
$$L_M=-\frac{T_0}{\kappa g}\frac{{u^*}^3}{F_\theta+\left(\frac{1}{\epsilon}-1\right)\theta F_q}$$

ここで、$F_u,F_v,F_\theta,F_q$はそれぞれ運動量、熱、水蒸気の地表面フラックスであり、$T_0$は地表気温、$\theta$は1層目の温位、$\kappa$はカルマン定数である。
### 雲水量の診断

### 安定度関数
大気の成層安定度の指標となるバルクRichardson数 $Ri$ は、風速の鉛直シア
$$G_M=\left(\frac{\Delta u}{\Delta z}\right)^2+\left(\frac{\Delta v}{\Delta z}\right)^2$$
と浮力
$$G_H=-\frac{g}{\theta}\left(\beta_\theta \frac{\Delta \theta}{\Delta z}+\beta_q \frac{\Delta q}{\Delta z}\right)$$
の比として定義される。
$$Ri=-\frac{G_H}{G_M}$$
フラックスRichardson数 $Rf$ は
$$Rf=R_{i1}\left(Ri+R_{i2}-\sqrt{Ri^2-R_{i3}Ri+R_{i4}}\right)$$
ただし、クロージャー定数
$$(Pr,\gamma_1,B_1,B_2,C_2,C_3,C_4,C_5)=(0.74,0.235,24.0,15.0,0.7,0.323,0.0,0.2)$$
に対して
$$A_1=B_1\frac{1-3\gamma_1}{6}$$
$$C_1=\gamma_1-\frac{1}{3A_1{B_1}^{\frac{1}{3}}}$$
$$A_2=A_1\frac{\gamma_1-C_1}{\gamma_1 Pr}$$
$$\gamma_2=\frac{B_2}{B_1}\left(1-C_3\right)+2\frac{A_1}{B_1}\left(3-2C_2\right)$$
$$F_1=B_1(\gamma_1-C_1)+2A_1(3-2C_2)+3A_2(1-C_2)(1-C_5)$$
$$F_2=B_1(\gamma_1+\gamma_2)-3A_1(1-C_2)$$
$$R_{f1}=B_1\frac{\gamma_1-C_1}{F_1}$$
$$R_{f2}=B_1\frac{\gamma_1}{F_2}$$
$$Rf_c=\frac{\gamma_1}{\gamma_1+\gamma_2}$$
$$S_{Mc}=\frac{A_1}{A_2}\frac{F_1}{F_2}$$
$$S_{Hc}=3A_2(\gamma_1+\gamma_2)$$
$$R_{i1}=\frac{1}{2S_{Mc}}$$
$$R_{i2}=R_{f1}S_{Mc}$$
$$R_{i3}=4R_{f2}S_{Mc}-2R_{i2}$$
$$R_{i4}={R_{i2}}^2$$
さらに、Level2スキームで使用される安定度関数 $S_{H2},S_{M2}$ も以下のようにして計算される。
$$S_{H2}=S_{Hc}\frac{Rf_c-Rf}{1-Rf}$$
$$S_{M2}=S_{Mc}\frac{R_{f1}-Rf}{R_{f2}-Rf}S_{H2}$$
### 乱流の代表的長さスケール

### 大気境界層による補正

### 乱流量の予報式

### 乱流の生成散逸項

### 拡散係数の計算

### フラックスの計算
