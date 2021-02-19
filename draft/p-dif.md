<!-- TOC -->

- [乱流](#乱流)
  - [接地境界層](#接地境界層)
  - [浮力係数の診断](#浮力係数の診断)
  - [レベル2の安定度関数](#レベル2の安定度関数)
  - [乱流の代表的長さスケール](#乱流の代表的長さスケール)
  - [拡散係数の計算](#拡散係数の計算)
  - [フラックスの計算](#フラックスの計算)
  - [乱流量の計算](#乱流量の計算)
  - [Time integration with implicit scheme](#time-integration-with-implicit-scheme)

<!-- /TOC -->
## 乱流
本章では、サブグリッドスケールの乱流の格子平均量への影響を表現する乱流スキームについて記述する。乱流スキームは、乱流による運動量、熱、水およびその他のトレーサーの鉛直拡散を計算する。MIROCではバージョン5以降、乱流スキームとして、Mellor-Yamadaスキーム（Mellor 1973; Mellor and Yamada 1974; Mellor and Yamada 1982）の改良版であるMellor-Yamada-Nakanishi-Niinoスキーム（MYNNスキーム; Nakanishi 2001; Nakanishi and Niino 2004）が採用されている。クロージャーレベルは2.5である。レベル3も使用可能であるが、計算量の増大に見合うパフォーマンスの向上が得られないため、非標準オプションとなっている。

MYNNスキームでは、熱力学変数としてliquid water potential temperature $\theta_l$ およびtotal water $q_w$ が使用され、それぞれ以下のように定義される。これらは水の相変化によらず保存される量である。

$$ \theta_l \equiv \left(T - \frac{L_v}{C_p}q_l - \frac{L_v+L_f}{C_p}q_i \right) \left(\frac{p_s}{p}\right)^{\frac{R_d}{C_p}} $$

$$ q_w \equiv q_v+q_l+q_i $$

ここで、$T$, $p$は、それぞれ温度と圧力、$q_v$, $q_l$, $q_i$は、それぞれ比湿、雲水、雲氷、$C_p$, $R_d$は、それぞれ乾燥空気の定圧比熱および気体定数、$L_v$, $L_f$は、それぞれ単位質量あたりの水蒸気の凝結熱および水の凝固熱である。$p_s$は1000hPaである。

また、Level2.5においては、乱流の運動エネルギーを2倍した量である

$$q^2 \equiv \langle u^2 + v^2 + w^2 \rangle$$

が予報変数となっており、この時間発展もこのスキーム内で計算される。ここで、$u$, $v$, $w$は、それぞれ東西方向、南北方向、鉛直方向の風速である。本章では、大文字の変数で格子平均量を表し、小文字の変数で格子平均からのずれを表すこととする。$\langle \ \rangle$はアンサンブル平均を表す。レベル3の場合、$\langle {\theta_l}^2 \rangle,\langle {q_w}^2 \rangle,\langle \theta_l q_w \rangle$ が予報変数に追加されるが、ここでは省略する。

計算手順の概略は以下の通りである。

1. 摩擦速度およびMonin-Obukhov長を計算する
2. 部分凝結を考慮して浮力係数を計算する [`VDFCND`]
3. レベル2の安定度関数を計算する [`VDFLEV2`]
4. 大気境界層の深さを計算する [`PBLHGT`]
5. 乱流の代表的長さスケールを計算する [`VDFMLS`]
6. 拡散係数および鉛直フラックスとその微分値を計算する [`VDFLEV3`]
7. 乱流量の生成項と散逸項を計算する [`VDFLEV3`]
8. 予報変数のimplicit時間積分を計算する

### 接地境界層
摩擦速度 $u_*$ およびMonin-Obukhov長 $L_M$ はそれぞれ以下のように与えられる。

$$u_*=\left({\langle uw \rangle_g}^2+{\langle vw \rangle_g}^2 \right)^\frac{1}{4}$$

$$L_M=-\frac{\Theta_{v,g} {u_*}^3}{kg \langle w\theta_v \rangle_g}$$

ここで、下付文字$g$は、地表付近での値であることを表す。$\Theta_v$, $\theta_v$は仮温位、$k$, $g$は、それぞれ、Von Karman定数および重力加速度である。

### 浮力係数の診断

乱流の方程式に現れる浮力項の計算には $\langle w\theta_v \rangle$ の値が必要である。Mellor (1982)に従い、$\theta_l$, $q_w$のグリッド内の確率分布を仮定すると、この項は、

$$\langle w\theta_v \rangle=\beta_\theta \langle w\theta_l \rangle + \beta_q \langle wq_w \rangle$$

と書ける。ただし、確率分布は、Mellor (1982), Nakanishi and Niino (2004)とは異なり、ガウス分布ではなく、PDF予報型大規模凝結スキーム（Watanabe et al. 2008）が与える三角形状の分布である。係数 $\beta_\theta , \beta_q$ は、以下のように表される。

$$\beta_\theta=1+\epsilon Q_w-(1+\epsilon)Q_l-Q_i-\tilde{R}abc$$

$$\beta_q=\epsilon \Theta +\tilde{R}ac$$

ここで、$\epsilon=R_v/R_d-1$であり、$R_d$, $R_v$はそれぞれ、乾燥大気および水蒸気の気体定数である。また、

$$a=\left(1+\frac{L_v}{C_p}\left.\frac{\partial Q_s}{\partial T}\right|_{T=T_l}\right)^{-1}$$

$$b=\frac{T}{\Theta}\left.\frac{\partial Q_s}{\partial T}\right|_{T=T_l}$$

$$c=\frac{\Theta}{T}\frac{L_v}{C_p}\left[1+\epsilon Q_w-(1+\epsilon)Q_l-Q_i\right]-(1+\epsilon)\Theta$$

$$\tilde{R}=R\left\{1-a\left[Q_w-Q_s(T_l)\right]\frac{Q_l}{2\sigma_s}\right\}-\frac{{Q_l}^2}{4{\sigma_s}^2}$$

$${\sigma_s}^2=\langle {q_w}^2 \rangle -2b \langle \theta_l q_w \rangle + b^2\langle {\theta_l}^2 \rangle$$

である。ここで、$R,Q_l$ はそれぞれグリッド内の確率分布から診断される雲量および液水量、$Q_s$は、飽和水蒸気量を表す。また、$\sigma_s$の計算に用いられる$q_w$, $\theta_l$は、大規模凝結スキームで予報される量ではなく、MYNNスキーム内で診断される量であることに注意されたい（その診断式は後述）。

### レベル2の安定度関数

Mellor-YamadaスキームのLevel2.5では、乱流の成長段階のふるまいが悪いことが知られている(Helfand and Labraga 1988)。そのため、MYNNスキームでは局所的に平衡が仮定されるLevel2の乱流の運動エネルギー、${q_2}^2/2$ を計算し、$q<q_2$ すなわち乱流が成長段階にある場合に補正をかける。$q_2$の計算に必要なLevel2の安定度関数 $S_{H2},S_{M2}$ は以下のように求められる。

$$S_{H2}=S_{HC}\frac{Rf_c-Rf}{1-Rf}$$

$$S_{M2}=S_{MC}\frac{R_{f1}-Rf}{R_{f2}-Rf}S_{H2}$$

ここで、$Rf$は、フラックスRichardson数であり、以下のように計算される。

$$Rf=R_{i1}\left(Ri+R_{i2}-\sqrt{Ri^2-R_{i3}Ri+R_{i4}}\right)$$

$Ri$はgradient Richardson数であり、以下のように計算される。

$$Ri=\frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right) \Bigg/ \left[ \left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2 \right]$$

その他の記号は、環境場に依存しない量であり、以下のように与えられる。

$$S_{HC}=3A_2(\gamma_1+\gamma_2)$$

$$S_{MC}=\frac{A_1}{A_2}\frac{F_1}{F_2}$$

$$Rf_c=\frac{\gamma_1}{\gamma_1+\gamma_2}$$

$$R_{f1}=B_1\frac{\gamma_1-C_1}{F_1}$$

$$R_{f2}=B_1\frac{\gamma_1}{F_2}$$

$$R_{i1}=\frac{1}{2S_{Mc}}$$

$$R_{i2}=R_{f1}S_{MC}$$

$$R_{i3}=4R_{f2}S_{MC}-2R_{i2}$$

$$R_{i4}={R_{i2}}^2$$

ここで、

$$A_1=B_1\frac{1-3\gamma_1}{6}$$

$$A_2=A_1\frac{\gamma_1-C_1}{\gamma_1 Pr}$$

$$C_1=\gamma_1-\frac{1}{3A_1{B_1}^{\frac{1}{3}}}$$

$$F_1=B_1(\gamma_1-C_1)+2A_1(3-2C_2)+3A_2(1-C_2)(1-C_5)$$

$$F_2=B_1(\gamma_1+\gamma_2)-3A_1(1-C_2)$$

$$\gamma_2=\frac{B_2}{B_1}\left(1-C_3\right)+\frac{2A_1}{B_1}\left(3-2C_2\right)$$

また、

$$
(Pr,\gamma_1,B_1,B_2,C_2,C_3,C_4,C_5)=(0.74,0.235,24.0,15.0,0.7,0.323,0.0,0.2)
$$

### 乱流の代表的長さスケール

#### Nakanishi (2001)の定式化
Nakanishi (2001)は、master length scale $L$ として以下の式を提案している。
$$\frac{1}{L}=\frac{1}{L_S}+\frac{1}{L_T}+\frac{1}{L_B} \tag{1} $$

$L_S,L_T,L_B$ はそれぞれ接地層、対流混合層、安定成層における長さスケールを表し、以下のように定式化されている。
$$
L_S=\left\{
    \begin{array}{lr}
      kz/3.7, &\zeta\ge 1\\
      kz/(2.7+\zeta), &0\le\zeta< 1\\
      kz(1-\alpha_4\zeta)^{0.2}, &\zeta< 0\\
    \end{array}
  \right.
$$

$$L_T=\alpha_1\frac{\displaystyle \int_0^\infty{qz}\,dz}{\displaystyle \int_0^\infty{q}\,dz}$$

$$
L_B=\left\{
    \begin{array}{ll}
      \alpha_2 q/N, &\partial\Theta_v/\partial z> 0 \quad\rm{and}\quad\zeta\ge 0\\
      \left[\alpha_2+\alpha_3\sqrt{q_c/L_TN}\right]q/N, &\partial\Theta_v/\partial z> 0 \quad\rm{and}\quad\zeta< 0\\
      \infty, &\partial\Theta_v/\partial z\le 0\\
    \end{array}
  \right.
$$

ここで $\zeta\equiv z/L_M$ はMonin-Obukhov長 $L_M$ で規格化された高さ、$N\equiv\left[(g/\Theta)(\partial\Theta_v/\partial z)\right]^{1/2}$ はBrunt-Väisälä振動数、 $q_c\equiv [(g/\Theta)\langle w\theta_v \rangle_gL_T]^{1/3}$ は対流混合層内の速度スケールを表す。経験定数はLarge Eddy Simulationの結果に基づき、
$$(\alpha_1,\alpha_2,\alpha_3,\alpha_4)=(0.23,1.0,5.0,100.0)$$

と定められている。

#### MIROCへの実装上の修正

Nakanishi (2001)における以上の定式化は、モデルの領域が大気境界層とその周辺域に限られている場合、適切な値をとる。しかし、モデルが対流圏上層まで含む場合、条件によっては、対流混合層の長さスケールである$L_T$が自由大気で使われてしまう、$L_T$の計算における$q$として自由大気の乱流エネルギーも含まれてしまう、などの問題が生じる。

そこで、MIROCへの実装に当たり、対流混合層の上端の高さ$H_{PBL}$を見積もり、$h=\sqrt{(F_H H_{PBL})^2+H_0^2}$ より下の領域を境界層乱流が卓越する領域とみなす。ここで$F_H=1.5$、$H_0=500$mである。

高度$h$以下では、master length scaleとして(1)式を用いるが、$L_T$において、積分の範囲を以下のように修正する。

$$L_T=\alpha_1\frac{\displaystyle \int_0^h{qz}\,dz}{\displaystyle \int_0^h{q}\,dz}$$

高度 $h$ より上では、$L$ は以下のように計算する。

$$\frac{1}{L}=\frac{1}{L_S}+\frac{1}{L_A}+\frac{1}{L_{max}}$$

ここで、$L_A=\alpha_5\,q/N$ は、安定成層において乱流により空気塊が鉛直方向に移動するときの長さスケールを表す。$\alpha_5$は散逸の効果を表し、$\alpha_5=0.53$ である。  $L_{max}=500$mは$L$の上限を与える。

#### 対流混合層の上端の高さの見積もり

$H_{PBL}$の見積もりはHoltslag and Boville (1993)に基づき、バルクRichardson数

$$Ri_B=\frac{[g/\Theta_v(z_1)][\Theta_v(z_k)-\Theta_{v,g}](z_k-z_g)}{[U(z_k)-U(z_1)]^2+[V(z_k)-V(z_1)]^2+F_u{u_*}^2}$$

を用いて計算する。ここで、$z_k$は下からk番目の層のフルレベルの高度を表し、$z_1$はモデル最下層のフルレベルの高度、$z_g$は地表高度である。$F_u$は無次元のチューニングパラメータである。また、

$$\Theta_{v,g}=\Theta_v(z_1)+F_b \frac{\langle w\theta_v \rangle_g}{w_m}$$

$$w_m=u_*/\phi_m$$

$$\phi_m=\left(1-15\frac{z_s}{L_M}\right)^{-\frac{1}{3}}$$

であり、$z_s$は接地層の高度で、$z_s=0.1H_{PBL}$としている。$F_b$は無次元のチューニングパラメータである。

$k=2$から上に向かって$Ri_B$を順番に計算し、$Ri_B>0.5$ となる層とそのすぐ下の層の間で$Ri_B$を線形内挿し、ちょうど$Ri_B=0.5$となる高さを$H_{PBL}$とする。$z_s$の計算に$H_{PBL}$が必要であるため、最初に仮の値$H_{PBL}=z_1-z_g$を代入した$z_s$を使って$H_{PBL}$計算し、この$H_{PBL}$を代入した$z_s$を用いて真の$H_{PBL}$を再計算する。

### 拡散係数の計算

#### レベル2の乱流の運動エネルギー

レベル2の乱流の運動エネルギー${q_2}^2/2$ は、乱流の運動エネルギーの時間発展式において、時間微分項、移流項、拡散項を無視した以下の式から計算される。

$$ P_s + P_b - \varepsilon = 0 \tag{2} $$

ここで、$P_s$, $P_b$, $\varepsilon$は、それぞれシアーによる生成項、浮力による生成項、消散項である。$P_s$, $P_b$は、以下のように表される。

$$ P_s = -\langle wu \rangle \frac{\partial U}{\partial z} - \langle wv \rangle \frac{\partial V}{\partial z} $$

$$ P_b = \frac{g}{\Theta}\langle w\theta_v \rangle $$

MYNNスキームのレベル2ではこれらは以下のように表される。

$$ P_s = LqS_{M2} \left[ \left(\frac{\partial U}{\partial z}\right)^2 + \left(\frac{\partial V}{\partial z}\right)^2 \right] \tag{3} $$

$$ P_b = LqS_{H2} \frac{g}{\Theta}\left[ \beta_\theta \frac{\partial \Theta_l}{\partial z} + \beta_q \frac{\partial Q_w}{\partial z} \right] \tag{4} $$

$$ \varepsilon = \frac{q^3}{B_1 L} \tag{5} $$

(2), (3), (4), (5)より、${q_2}^2$は以下のように計算される。

$${q_2}^2=B_1L^2\left\{S_{M2}\left[\left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2\right]+S_{H2}\frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right)\right\}$$

#### レベル2.5の安定度関数

$q<q_2$ すなわち乱流が成長段階にある場合は、Helfand and Labraga (1998) で導入された係数 $\alpha=q/q_2$ を使って、レベル2.5の安定度関数、$S_M$, $S_H$を以下のように計算する。
$$S_M=\alpha S_{M2},\quad S_H=\alpha S_{H2}$$

一方、$q \geq q_2$のときは、$S_M$, $S_H$は、以下のように計算される。以下の式は、Nakanishi (2001)のものとは記述法が異なるが、より少ない計算量で同等の結果を与えるものである。

$$S_M=A_1\frac{E_3-3C_1 E_4}{E_2 E_4+E_5 E_3}$$

$$S_H=A_2\frac{E_2+3C_1 E_5}{E_2 E_4+E_5 E_3}$$

ここで、

$$E_1=1-3A_2B_2(1-C_3)G_H$$

$$E_2=1-9A_1A_2(1-C_2)G_H$$

$$E_3=E_1+9{A_2}^2(1-C_2)(1-C_5)G_H$$

$$E_4=E_1-12A_1A_2(1-C_2)G_H$$

$$E_5=6{A_1}^2G_M$$

$$G_M=\frac{L^2}{q^2}\left[\left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2\right]$$

$$G_H=-\frac{L^2}{q^2}\frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right)$$

#### 拡散係数の計算

風速, 乱流エネルギー, 熱, 水に対する拡散係数 $K_M$, $K_q$, $K_H$, $K_w$ は、 $S_M,S_H$ から以下のように計算される。
$$K_M=LqS_M$$

$$K_q=3LqS_M$$

$$K_H=LqS_H$$

$$K_w=LqS_H$$

### フラックスの計算

各物理量の鉛直フラックス $F$ は以下のように計算される。

$$F_{u,k-1/2}=-\rho_{k-1/2}K_{M,k-1/2}\frac{U_{k}-U_{k-1}}{\Delta z_{k-1/2}}$$

$$F_{v,k-1/2}=-\rho_{k-1/2}K_{M,k-1/2}\frac{V_{k}-V_{k-1}}{\Delta z_{k-1/2}}$$

$$F_{q,k-1/2}=-\rho_{k-1/2}K_{q,k-1/2}\frac{{q^2}_ {k}-{q^2}_ {k-1}}{\Delta z_{k-1/2}}$$

$$F_{T,k-1/2}=-\rho_{k-1/2}K_{H,k-1/2}\,C_p\Pi_{k-1/2}\frac{\Theta_{l,k}-\Theta_{l,k-1}}{\Delta z_{k-1/2}}$$

$$F_{w,k-1/2}=-\rho_{k-1/2}K_{w,k-1/2}\frac{Q_{w,k}-Q_{w,k-1}}{\Delta z_{k-1/2}}$$

また、implicit法による時間積分を行うために、各鉛直フラックスの微分値を以下のように求めておく。

$$\frac{\partial F_{u,k-1/2}}{\partial U_{k-1}}=\frac{\partial F_{v,k-1/2}}{\partial V_{k-1}}=-\frac{\partial F_{u,k-1/2}}{\partial U_{k}}=-\frac{\partial F_{v,k-1/2}}{\partial V_{k}}=\rho_{k-1/2}K_{M,k-1/2}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{q,k-1/2}}{\partial {q^2}_ {k-1}}=-\frac{\partial F_{q,k-1/2}}{\partial {q^2}_ {k}}=\rho_{k-1/2}K_{q,k-1/2}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{T,k-1/2}}{\partial T_{k-1}}=\rho_{k-1/2}K_{H,k-1/2}C_p\frac{\Pi_{k-1/2}}{\Pi_{k-1}}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{T,k-1/2}}{\partial T_{k}}=-\rho_{k-1/2}K_{H,k-1/2}C_p\frac{\Pi_{k-1/2}}{\Pi_{k}}\frac{1}{\Delta z_{k-1/2}}$$

$$\frac{\partial F_{w,k-1/2}}{\partial Q_{w,k-1}}=-\frac{\partial F_{w,k-1/2}}{\partial Q_{w,k}}=\rho_{k-1/2}K_{w,k-1/2}\frac{1}{\Delta z_{k-1/2}}$$

ここで、$\Delta z_{k-1/2}=z_k-z_{k-1}$である。各種トレーサーについても、 $K_w$ を用いて同様にフラックスが計算される。

### 乱流量の計算

#### 乱流の運動エネルギーの計算

$q^2$ の予報式は以下で表される。
$$ \frac{d q^2}{dt}=-\frac{1}{\rho}\frac{\partial F_q}{\partial z}+2\left(P_s+P_b-\varepsilon\right) $$

 $P_s,P_b,\varepsilon$ は、レベル2.5では以下のように表される。

$$P_s=Lq S_M \left[\left(\frac{\partial U}{\partial z}\right)^2+\left(\frac{\partial V}{\partial z}\right)^2\right]$$

$$P_b=Lq S_H \frac{g}{\Theta}\left(\beta_\theta \frac{\partial \Theta_l}{\partial z}+\beta_q \frac{\partial Q_w}{\partial z}\right)$$

$$\varepsilon=\frac{q^3}{B_1L}$$

移流項は、力学スキームにおいてトレーサーの輸送ルーチンを使って計算される。乱流スキームでは、$q^2$の拡散項、生成項、消散項による時間発展がimplicit法を用いて計算される。

#### 分散および共分散の診断

また、$\langle {\theta_l}^2 \rangle,\langle {q_w}^2 \rangle,\langle \theta_l q_w \rangle$ の予報方程式は以下のように表される。

$$
\frac{d\left\langle{\theta_l}^{2}\right\rangle}{d t}=-\frac{\partial}{\partial z}\left\langle w \theta_{l}^{2}\right\rangle-2\left\langle w \theta_{l}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-2 \varepsilon_{\theta l}
$$

$$
\frac{d\left\langle {q_w}^{2}\right\rangle}{d t}=-\frac{\partial}{\partial z}\left\langle w q_{w}^{2}\right\rangle-2\left\langle w q_{w}\right\rangle \frac{\partial Q_{w}}{\partial z}-2 \varepsilon_{q w}
$$

$$
\frac{d\left\langle\theta_{l} q_{w}\right\rangle}{d t}=-\frac{\partial}{\partial z}\left\langle w \theta_{l} q_{w}\right\rangle-\left\langle w q_{w}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-\left\langle w \theta_{l}\right\rangle \frac{\partial Q_{w}}{\partial z}-2 \varepsilon_{\theta q}
$$

レベル2.5では、これらの式で、時間微分項、移流項、拡散項を無視し、局所的に以下のバランスが成立していると仮定する。

$$ -\left\langle w \theta_{l}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-\varepsilon_{\theta l} = 0 \tag{6}$$

$$ -\left\langle w q_{w}\right\rangle \frac{\partial Q_{w}}{\partial z}-\varepsilon_{q w} = 0 \tag{7}$$

$$ -\left\langle w q_{w}\right\rangle \frac{\partial \Theta_{l}}{\partial z}-\left\langle w \theta_{l}\right\rangle \frac{\partial Q_{w}}{\partial z}-2 \varepsilon_{\theta q} = 0 \tag{8}$$

MYNNスキームのレベル2.5では、$-\left\langle w \theta_{l}\right\rangle$, $-\left\langle w q_{w}\right\rangle$, $\varepsilon_{\theta l}$, $\varepsilon_{q w}$, $\varepsilon_{\theta q}$は以下のように表される。

$$ -\left\langle w \theta_{l}\right\rangle = LqS_H \frac{\partial \Theta_{l}}{\partial z} \tag{9}$$

$$ -\left\langle w q_{w}\right\rangle = LqS_H \frac{\partial Q_{w}}{\partial z} \tag{10}$$

$$
\varepsilon_{\theta l}=\frac{q}{B_{2} L}\left\langle\theta_{l}^{2}\right\rangle \tag{11}
$$

$$
\varepsilon_{q w}=\frac{q}{B_{2} L}\left\langle q_{w}^{2}\right\rangle \tag{12}
$$

$$
\varepsilon_{\theta q}=\frac{q}{B_{2} L}\left\langle\theta_{l} q_{w}\right\rangle \tag{13}
$$

(6)-(13)より、$\langle {\theta_l}^2 \rangle$, $\langle {q_w}^2 \rangle$, $\langle \theta_l q_w \rangle$は以下のように診断的に計算される。

$$\langle {\theta_l}^2 \rangle =B_2L^2S_H\left(\frac{\partial \Theta_l}{\partial z}\right)^2$$

$$\langle {q_w}^2 \rangle =B_2L^2S_H\left(\frac{\partial Q_w}{\partial z}\right)^2$$

$$\langle \theta_l q_w \rangle =B_2L^2S_H\frac{\partial \Theta_l}{\partial z}\frac{\partial Q_w}{\partial z}$$

#### モデル最下層の扱い

モデル最下層は、物理量の鉛直勾配が急激に変化する接地層に相当するため、鉛直勾配を精度良く評価するために、以下のMonin-Obukhov相似則を用いる。

$$ \frac{\partial M}{\partial z} = \frac{u_*}{kz}\phi_m \tag{14}$$

$$ \frac{\partial \Theta}{\partial z} = \frac{\theta_*}{kz}\phi_h \tag{15}$$

$$ \frac{\partial Q_v}{\partial z} = \frac{q_{v*}}{kz}\phi_h \tag{16}$$

ここで、$M$は接地層における水平風の向きに横軸をとったときの風速を表す。$\phi_m$, $\phi_h$は、それぞれ運動量と熱に対する無次元勾配関数である。$\theta_*$, $q_{v*}$は、それぞれ、接地層における温位と水蒸気のスケールであり、以下の関係を満たす。

$$ \langle wm \rangle_g = -u_*^2 \tag{17}$$

$$ \langle w\theta \rangle_g = -u_*\theta_* \tag{18}$$

$$ \langle wq_v \rangle_g = -u_*q_{v*} \tag{19}$$

$m$は$M$の格子平均からのズレである。$M$, $m$を用いると、乱流エネルギーの生成項は、以下のように書ける。

$$ P_s + P_b = \langle wm \rangle \frac{\partial M}{\partial z} + \frac{g}{\Theta} \langle w\theta_v \rangle $$

これは、(14), (17)およびMonin-Obukhov長の定義式を用いると、以下のように計算できる。

$$ P_s + P_b = \frac{u_*^3}{kz_1}\left[\phi_m\left(\zeta_1\right)-\zeta_1\right] $$

ここで、$\zeta_1$は、モデル最下層のフルレベルでの$\zeta$である。

接地層では雲粒がないと仮定し、$\langle {\theta_l}^2\rangle$, $\langle {q_w}^2\rangle$, $\langle \theta_lq_w\rangle$は、(6)-(8), (11)-(13), (15), (16), (18), (19)より、以下のように診断的に計算できる。

$$\langle {\theta_l}^2\rangle=\frac{\phi_h\left(\zeta_1\right)}{u_*kz_1}{\langle w\theta \rangle_g}^2 \bigg/ \frac{q}{B_2L} $$

$$\langle {q_w}^2\rangle=\frac{\phi_h\left(\zeta_1\right)}{u_*kz_1}{\langle wq_v\rangle_g}^2 \bigg/ \frac{q}{B_2L} $$

$$\langle \theta_lq_w\rangle=\frac{\phi_h\left(\zeta_1\right)}{u_*kz_1}\langle w\theta \rangle_g\langle wq_v \rangle_g \bigg/ \frac{q}{B_2L} $$

$\phi_m,\phi_h$ は、Businger et al. (1971)に基づき以下のように定式化されている。
$$
\phi_m(\zeta)=\left\{
    \begin{array}{lr}
      1+\beta_1\zeta, &\zeta\ge 0\\
      \left(1-\gamma_1\zeta\right)^{-1/4}, &\zeta< 0\\
    \end{array}
  \right.
$$

$$
\phi_h(\zeta)=\left\{
    \begin{array}{lr}
      \beta_2+\beta_1\zeta, &\zeta\ge 0\\
      \beta_2\left(1-\gamma_2\zeta\right)^{-1/2}, &\zeta< 0\\
    \end{array}
  \right.
$$

$$(\beta_1,\beta_2,\gamma_1,\gamma_2)=(4.7,0.74,15.0,9.0)$$

### Time integration with implicit scheme

The prognostic equation for $q^2$ is discretized as

$$ \frac{q^2_{k,n+1}-q^2_{k,n}}{\Delta t} = -\frac{1}{\rho_k\Delta z_k}\left(F_{q,k+1/2,n+1}-F_{q,k-1/2,n+1}\right) +2\left( P_{s,k,n} + P_{b,k,n} - \frac{q_{k,n}}{B_1L}q^2_{k,n+1}\right) $$

where $n$ and $n+1$ indicate the current and next time steps respectively. $\rho$ is density and $\Delta z_k \equiv z_{k+1/2}-z_{k-1/2}$. $F_q$ at $n+1$ is represented by

$$ F_{q,k-1/2,n+1} = F_{q,k-1/2,n} + \frac{\partial F_{q,k-1/2}}{\partial q^2_k}(q^2_{k,n+1}-q^2_{k,n}) +  \frac{\partial F_{q,k-1/2}}{\partial q^2_{k-1}}(q^2_{k-1,n+1}-q^2_{k-1,n})$$