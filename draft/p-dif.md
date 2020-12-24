<!-- TOC -->

- [鉛直拡散](#鉛直拡散)
  - [接地境界層](#接地境界層)
  - [雲水量の診断](#雲水量の診断)
  - [安定度関数](#安定度関数)
  - [乱流の代表的長さスケール](#乱流の代表的長さスケール)
  - [拡散係数の計算](#拡散係数の計算)
  - [フラックスの計算](#フラックスの計算)
  - [乱流量の計算](#乱流量の計算)

<!-- /TOC -->
## 鉛直拡散
本章では、サブグリッドスケールの乱流を表現する鉛直拡散スキームについて記述する。鉛直拡散スキームでは、運動量、熱、および水蒸気などのトレーサーについて、鉛直フラックスとimplicit解を得るための微分値を出力する。また、後述する乱流量について時間発展を解くために必要な生成項、散逸項、鉛直フラックスを出力する。

鉛直拡散係数の見積もりにはNakanishi and Niino (2004)の改良Mellor-Yamada Level2.5乱流クロージャーモデル(MYNNモデル)を用いる。MYNNモデルでは、熱力学変数としてliquid water potential temperature $\theta_l$ およびtotal water content $q_w$ が使用され、それぞれ以下のように定義される。
$$ \theta_l=\frac{ T - \frac{L}{C_p}q_l - \frac{L+L_{M}}{C_p}q_i }{\left(\frac{p}{p_0}\right)^\kappa } $$
$$q_w=q_v+q_l+q_i$$
また、Level2.5モデルにおいては、乱流エネルギー $q^2/2=(\langle u^2 \rangle + \langle v^2 \rangle + \langle w^2 \rangle)/2$ が予報変数となっており、この時間発展項もこのスキーム内で求められる。$\langle \ \rangle$はアンサンブル平均を表す。非標準スキームとしてMYNN Level 3モデルが存在し、その場合は $\langle {\theta_l}^2 \rangle,\langle {q_w}^2 \rangle,\langle \theta_l q_w \rangle$ が予報変数に追加されるが、ここでは省略する。

計算手順の概略は以下の通りである。

1. 摩擦速度およびMonin-Obukhov長を計算する
2. 部分凝結を考慮して雲水量を計算する [`VDFCND`]
3. 安定度関数を計算する [`VDFLEV2`]
4. 大気境界層の深さを計算する [`PBLHGT`]
5. 乱流の代表的長さスケールを計算する [`VDFMLS`]
6. 拡散係数および鉛直フラックスとその微分値を計算する [`VDFLEV3`]
7. 乱流量の生成項と散逸項を計算する [`VDFLEV3`]

### 接地境界層
摩擦速度 $u^*$ およびMonin-Obukhov長 $L_M$ はそれぞれ以下のように与えられる。

$$u^*=\left(\sqrt{{F_{u,g}}^2+{F_{v,g}}^2}/\rho \right)^\frac{1}{2}$$
$$L_M=-\frac{T_g}{\kappa g}\frac{{u^*}^3}{\langle w\theta_v \rangle_g}$$

ここで、$\langle w\theta_v \rangle_g=F_{\theta,g}/C_p\rho +\left(\frac{1}{\epsilon}-1\right)\theta_1 F_{w,g}/\rho$ は地表における仮温位の鉛直フラックスである。 $F_{u,g},F_{v,g},F_{\theta,g},F_{w,g}$ はそれぞれ運動量、熱、水蒸気の地表面フラックス、$T_g$は地表における仮温度、$\theta_1$は1層目の温位、$\kappa$はカルマン定数である。
### 雲水量の診断

### 安定度関数
大気の成層安定度の指標となるRichardson数 $Ri$ は以下のように求められる。
$$Ri=\frac{\frac{g}{\theta}\left(\beta_\theta \frac{\partial \theta}{\partial z}+\beta_q \frac{\partial q}{\partial z}\right)}{\left(\frac{\partial u}{\partial z}\right)^2+\left(\frac{\partial v}{\partial z}\right)^2}$$
フラックスRichardson数 $Rf$ は、 $Ri$ を用いて計算される。
$$Rf=R_{i1}\left(Ri+R_{i2}-\sqrt{Ri^2-R_{i3}Ri+R_{i4}}\right)$$
ただし、
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
Mellor-Yamada Level2.5スキームでは、乱流の成長段階のふるまいが悪いことが知られている(Helfand and Labraga, 1988)。そのため、MYNNモデルでは局地的に平衡が仮定されるLevel2スキームで乱流エネルギー ${q_2}^2/2$ を計算し、 $q<q_2$ すなわち乱流が成長段階にある場合に補正をかける。 $q_2$ の計算に必要なLevel2スキームで使用される安定度関数 $S_{H2},S_{M2}$ は以下のようにして求められる。
$$S_{H2}=S_{Hc}\frac{Rf_c-Rf}{1-Rf}$$
$$S_{M2}=S_{Mc}\frac{R_{f1}-Rf}{R_{f2}-Rf}S_{H2}$$
### 乱流の代表的長さスケール
master turbulence length $L$ は、接地層スケール $L_S$、対流境界層スケール $L_T$、安定層スケール $L_B$ の調和平均として決定される。ただし、MYNNモデルのこの定式化は自由大気において雲の放射効果で安定度が減少した際にふるまいが悪くなる。そこで、バルクRichardson数
$$Ri_B=\frac{\frac{g}{\theta_g}\Delta\theta_v\Delta z}{(\Delta u)^2+(\Delta v)^2}$$
について $Ri_B=0.5$ となるところを大気境界層高度 $H_{PBL}$ として、 $h=\sqrt{1.5H_{PBL}^2+H_0^2}$ より上では $L$ の扱いを変更する。標準では $H_0=500$ m である。

高度 $h$ より下においては、 $L$ は以下で与えられる。
$$\frac{1}{L}=\frac{1}{L_S}+\frac{1}{L_T}+\frac{1}{L_B}$$
ここでそれぞれのスケールは以下のように求められる。
\[L_S=\left\{
    \begin{array}{1}
      \kappa z/3.7, &\zeta\ge1\\
      \kappa z/(2.7+\zeta), &0\le\zeta\lt1\\
      \kappa z(1-\alpha_4\zeta)^{0.2}, &\zeta\lt0
    \end{array}
  \right.
\]
$$L_T=\alpha_1\frac{\int_0^h{qz}\,dz}{\int_0^h{q}\,dz}$$
\[L_B=\left\{
    \begin{array}{1}
      \alpha_2 q/N, &\partial\Theta/\partial z\gt0\quad\rm{and}\quad\zeta\ge0\\
      \left[\alpha_2+\alpha_3\sqrt{q_c/L_TN}\right]q/N, &\partial\Theta/\partial z\gt0\quad\rm{and}\quad\zeta\lt0\\
      \infty, &\partial\Theta/\partial z\le0
    \end{array}
  \right.
\]
ここで $\zeta\equiv z/L_M$ はMonin-Obukhov長 $L_M$ で規格化された高さ、$N\equiv\left[(g/\theta)(\partial\theta_v/\partial z)\right]^{1/2}$ はBrunt-V\"{a}is\"{a}l\"{a}振動数、 $q_c\equiv [(g/\theta)\langle w\theta_v \rangle_gL_T]^{1/3}$ は対流速度 $w_*$ と同様な速度スケールを表す。経験定数は
$$(\alpha_1,\alpha_2,\alpha_3,\alpha_4)=(0.23,1.0,5.0,100.0)$$
と定める。

一方、高度 $h$ より上層の自由大気においては $L$ は $L_S, L_A, L_{max}$ の調和平均で与えられる。 $L_A=f_{LB}\ q/N$ は安定成層において乱流により空気塊が鉛直方向に移動するときの長さスケールを表し、$f_{LB}=0.53$ である。  $L_{max}=100$ m は $L$ の上限を与える。

### 拡散係数の計算
乱流の時間変化項および移流拡散項を無視して計算するLevel2モデルから求める乱流エネルギーは以下の式で与えられる。
$${q_2}^2=B_1L^2\left\{S_{M2}\left[\left(\frac{\partial u}{\partial z}\right)^2+\left(\frac{\partial v}{\partial z}\right)^2\right]+S_{H2}\frac{g}{\theta}\left(\beta_\theta \frac{\partial \theta}{\partial z}+\beta_q \frac{\partial q}{\partial z}\right)\right\}$$
$q<q_2$ すなわち乱流が成長段階にある場合は、Helfand and Labraga (1998) で導入された係数 $\alpha=q/q_2$ によって安定度関数の補正を行う。
$$S_M=\alpha S_{M2},\quad S_H=\alpha S_{H2}$$
一方、 $q\ge q_2$ の場合には
$$S_M=A_1\frac{\Phi_3-3C_1\Phi_4}{D_{2.5}}$$
$$S_H=A_2\frac{\Phi_2+3C_1\Phi_5}{D_{2.5}}$$
ただし
$$\Phi_1=1-3A_2B_2(1-C_3)G_H$$
$$\Phi_2=1-9A_1A_2(1-C_2)G_H$$
$$\Phi_3=\Phi_1+9{A_2}^2(1-C_2)(1-C_5)G_H$$
$$\Phi_4=\Phi_1-12A_1A_2(1-C_2)G_H$$
$$\Phi_5=6{A_1}^2G_M$$
$$D_{2.5}=\Phi_2\Phi_4+\Phi_5\Phi_3$$
$$G_M=\frac{L^2}{q^2}\left[\left(\frac{\partial u}{\partial z}\right)^2+\left(\frac{\partial v}{\partial z}\right)^2\right]$$
$$G_H=-\frac{L^2}{q^2}\frac{g}{\theta}\left(\beta_\theta \frac{\partial \theta_l}{\partial z}+\beta_q \frac{\partial q}{\partial z}\right)$$
拡散係数 $K$ は $S_M,S_H$ から以下のように計算される。
$$K_M=LqS_M$$
$$K_q=3LqS_M$$
$$K_H=LqS_H$$
$$K_w=LqS_H$$
### フラックスの計算
以上より各物理量の鉛直フラックス $F$ およびその微分値が計算される。
$$F_{u,k-1/2}=-K_{M,k-1/2}\frac{u_{k}-u_{k-1}}{z_k-z_{k-1}}$$
$$F_{v,k-1/2}=-K_{M,k-1/2}\frac{v_{k}-v_{k-1}}{z_k-z_{k-1}}$$
$$F_{q,k-1/2}=-K_{q,k-1/2}\frac{{q^2}_{k}-{q^2}_{k-1}}{z_k-z_{k-1}}$$
$$F_{\theta,k-1/2}=-K_{H,k-1/2}\,C_p\Pi_{k-1/2}\frac{\theta_{l,k}-\theta_{l,k-1}}{z_k-z_{k-1}}$$
$$F_{w,k-1/2}=-K_{w,k-1/2}\frac{q_{w,k}-q_{w,k-1}}{z_k-z_{k-1}}$$
$$\frac{\partial F_{u,k-1/2}}{\partial u_{k-1}}=\frac{\partial F_{v,k-1/2}}{\partial v_{k-1}}=-\frac{\partial F_{u,k-1/2}}{\partial u_{k}}=-\frac{\partial F_{v,k-1/2}}{\partial v_{k}}=K_{M,k-1/2}\frac{1}{z_k-z_{k-1}}$$
$$\frac{\partial F_{q,k-1/2}}{\partial {q^2}_{k-1}}=-\frac{\partial F_{q,k-1/2}}{\partial {q^2}_{k}}=K_{q,k-1/2}\frac{1}{z_k-z_{k-1}}$$
$$\frac{\partial F_{\theta,k-1/2}}{\partial T_{k-1}}=K_{H,k-1/2}C_p\frac{\Pi_{k-1/2}}{\Pi_{k-1}}\frac{1}{z_k-z_{k-1}}$$
$$\frac{\partial F_{\theta,k-1/2}}{\partial T_{k}}=-K_{H,k-1/2}C_p\frac{\Pi_{k-1/2}}{\Pi_{k}}\frac{1}{z_k-z_{k-1}}$$
$$\frac{\partial F_{w,k-1/2}}{\partial q_{w,k-1}}=-\frac{\partial F_{w,k-1/2}}{\partial q_{w,k}}=K_{w,k-1/2}\frac{1}{z_k-z_{k-1}}$$
また、各種トレーサーについても $K_w$ を用いて同様にフラックスが計算される。
### 乱流量の計算
乱流エネルギー $q^2$ の予報式は以下で表される。
$$\frac{\partial q^2}{\partial t}=-\frac{\partial F_q}{\partial z}+2\left(P_s+P_b-\epsilon\right)$$
 $P_s,P_b,\epsilon$ はそれぞれ平均流シアによる乱流生成項、浮力による乱流生成項、エネルギー散逸項を表し
$$P_s=\frac{q^3}{L}S_MG_M$$
$$P_b=\frac{q^3}{L}S_HG_H$$
$$\epsilon=\frac{q^3}{B_1L}$$
また、Level2.5スキームでは $\langle {\theta_l}^2 \rangle,\langle {q_w}^2 \rangle,\langle \theta_l q_w \rangle$ はそれぞれ以下のようにして診断される。
$$\langle {\theta_l}^2 \rangle =B_2L^2S_H\left(\frac{\partial \theta_l}{\partial z}\right)^2$$
$$\langle {q_w}^2 \rangle =B_2L^2S_H\left(\frac{\partial q_w}{\partial z}\right)^2$$
$$\langle \theta_l q_w \rangle =B_2L^2S_H\frac{\partial \theta_l}{\partial z}\frac{\partial q_w}{\partial z}$$
ただし、鉛直勾配が必要な量は第一層についてのみMonin-Obukhovの相似則を用いて計算される。
$$P_{s,1}+P_{b,1}=\frac{{u_*}^3}{\kappa z_1}\left[\phi_m\left(\zeta_1\right)-\zeta_1\right]$$
$$\langle {\theta_l}^2 \rangle_1=\frac{\phi_h\left(\zeta_1\right)}{u_*\kappa z_1}\frac{{\langle w\theta \rangle_g}^2}{q/B_2L}$$
$$\langle {q_w}^2 \rangle_1=\frac{\phi_h\left(\zeta_1\right)}{u_*\kappa z_1}\frac{{\langle wq_v \rangle_g}^2}{q/B_2L}$$
$$\langle \theta_lq_w \rangle_1=\frac{\phi_h\left(\zeta_1\right)}{u_*\kappa z_1}\frac{\langle w\theta \rangle_g\langle wq_v \rangle_g}{q/B_2L}$$
$z_1$ は第一層の高度であり、 $\zeta_1=z_1/L_M$ 、 $\phi_m,\phi_h$ はシア関数である。
