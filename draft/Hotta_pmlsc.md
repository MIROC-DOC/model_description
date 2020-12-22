# pmlsc: Large Scale Condensation

## Physical basis for statistical PDF scheme

GCMs typically adopt fractional cloud cover to realistically represent clouds because of its coarse horizontal resolution ($O(100km)$). Statistical cloud schemes assume a subgrid‐scale probability distribution function (PDF) of humidity within the grid to determine the cloud fraction and condensation. The key for statistical cloud schemes is to determine the PDF form and their moments. Assuming specific PDFs with their moments diagnosed or prognosed, integration of the PDFs will give the cloud fraction and condensate consistently.

The majority of statistical cloud schemes use the so-called "s-distribution", following Sommeria and Deardorff (1977). A single variable $s$, which considers the subgrid-scale perturbations of liquid temperature $T_l$ and total water mixing ratio $q_t$, is employed. $q_t$ is sum of water vapor and cloud water mixing ratio $q_c$.
$$
s=a_{L}\left(q_{t}^{\prime}-\alpha_{L} T_{l}^{\prime}\right)
$$
where
$$
a_{L}=1 /\left(1+L \alpha_{L} / c_{p}\right), \alpha_{L}=\partial q_{s} /\left.\partial T\right|_{T=\bar{T_l}}.
$$

By means of the "fast condensation" assumption,
$$
q_{c}=\left(q_{t}-q_{s}\right) \delta\left(q_{t}-q_{s}\right)
\tag{hpc.1}
$$
where $q_s$ denotes the saturation mixing ratio and $\delta(x)$ denotes the Heviside function of x.


The PDF of $s$ is denoted as $G(s)$. For any choice of $G(s)$, the grid-mean cloud fraction, $C$, and cloud water content, $q_c$, are obtained by integrating $G(s)$ and $(Qc + s)G(s)$, where $Qc$ denotes the grid-scale saturation deficit defined as
$$
Q_{c} \equiv a_{L}\left\{\bar{q}_{t}-q_{s}\left(\bar{T}_{l}, \bar{p}\right)\right\}.
$$
## Hybrid Prognostic Cloud (HPC) scheme

The statistical scheme implemented in MIROC6 is called Hybrid Prognostic Cloud (HPC) scheme (Watanabe et al. 2009). The HPC scheme proposes two types of shape for the PDF $G(s)$, Double-uniform PDF and Skewed-triangular PDF. We focus on Skewed-triangular because MIROC6 adoptes the shape. The physical basics of the scheme are in common with Double-uniform.


![](https://cdn.mathpix.com/snip/images/sT9QRiYBjSFFuHN6tYy1yHx4Md81UVA2xIGKupuEoLE.original.fullsize.png)

Example of the basis PDF for HPC: skewed-triangular functions.
Copied from Fig.1 in Watanabe et al. 2009.

The scheme preicts variance ($V$) and skewness ($S$) of the PDF. $V$, $S$, the second moment $\mu_2$, and the third moment $\mu_3$ are defined as follows.
$$
\mu_{2} \equiv V=\int_{-\infty}^{\infty} s^{2} G(s) d s
$$
$$
\mu_{3} \equiv \mu_{2}^{3 / 2} S=\int_{-\infty}^{\infty} s^{3} G(s) d s
$$
$V$ and $S$ are affected by cumulus convection, cloud microphysics, turbulent mixing, and advection.

The the integrals to obtain $C$ and $q_c$ is symbolically expressed as
$$
C=I_{C}\left(\bar{p}, \bar{T}_{l}, \bar{q}_{t}, \mathcal{V}, \mathcal{S}\right)
\tag{W09-1}
$$
$$
\bar{q}_{c}=I_{q}\left(\bar{p}, \bar{T}_{l}, \bar{q}_{t}, \mathcal{V}, \mathcal{S}\right)
\tag{W09-2}
$$

where $\bar{p}$ denotes the pressure. The overbars denote the grid-mean quantity.

If the PDF is not too complicated, (1, 2) can be analytically solved for $V$ and $S$ by defining integrand functions, ${\tilde{I}}$ as

$$
\mathcal{V}=\tilde{I}_{\mathcal{V}} \left(\bar{p}, \bar{T}_{l}, \bar{{q}}_{v}, \bar{q}_{c}, C\right)
$$
$$
\mathcal{S}=\tilde{I}_{\mathcal{VS}} \left(\bar{p}, \bar{T}_{l}, \bar{{q}}_{v}, \bar{q}_{c}, C\right)
$$

The relationship between (1, 2) and (4, 5) is quasireversible. The double-uniform function and skewed-triangular function PDFs are selected for $G(s)$ because of their feasibility in deriving ${\tilde{I}}$.

## PDF change through processes

The cloud scheme is composed using prognostic equations for four
variables determining $I$, namely, $T_l$,$q_t$, $V$, and $S$. The prognostic variables can also be $T_l$, $q_t$, $C$, and $q_c$ that determine $\tilde {I}$.
Everytime after the processes that affects cloud water PDF take place in the model, $G(s)$ is updated.  Thus $G(s)$ is modified several times within a single time step.
### Cumulus convection

The total effect of cumulus convection to the PDF moments is written as

$$
\left.\frac{\Delta \mathcal{V}}{\Delta t}\right|_{\mathrm{conv} .}=M_{c} \frac{\partial \mathcal{V}}{\partial z}+\frac{\Delta \tilde{I}_{\mathcal{V}}}{\Delta t}
\tag{W09-14}
$$

$$
\left.\frac{\Delta \mathcal{S}}{\Delta t}\right|_{\mathrm{conv} .}=M_{c} \frac{\partial \mathcal{S}}{\partial z}+\frac{\Delta \tilde{I}_{\mathcal{S}}}{\Delta t}
\tag{W09-15}
$$

$M_c$ is the cumulus mass-flux including downdraft.
The vertical transport of the PDF moments is represented by the first terms on the right side hand of (14, 15).

Cumulus convections modify the grid-mean $T_l$,$q_t$, and $q_c$ by upward transportation in the convective tower and subsidence in the environment. Detrainment also change these variables. The detrainment of the cloudy air mass is included, as in Bushell et al.

$$
\left.\frac{\partial C}{\partial t}\right|_{\mathrm{conv} .}=D(1-C)
$$

The second terms on the right hand side of (14, 15) indicates the changes in the PDF moments consistent with the changes in the grid-scale temperature, humidity, cloud water, and cloud fraction.

$$
\Delta \tilde{I}_{\mathcal{X}}= \tilde{I}_{\mathcal{X}}\left(\bar{p}, \bar{T}_{l}+\Delta \bar{T}_{l}, \bar{q}_{v}+\Delta \bar{q}_{v}, \bar{q}_{c}+\Delta \bar{q}_{c}, C+\Delta C\right)
-\tilde{I}_{\mathcal{X}}\left(\bar{p}, \bar{T}_{l,} \bar{q}_{v}, \bar{q}_{c}, C\right)
$$

$$
\tag{W09-16}
$$
where $\mathcal{X}$ is either $\mathcal{V}$ or $\mathcal{S}$.

[](D=g/P*CBMFX)
[](tracerinCUMFXR)
### Cloud Microphysics

The tendency due to microphysical processes can be written in a similar manner to the cumulus effect

$$
\left.\frac{\Delta \mathcal{V}}{\Delta t}\right|_{\text {micro. }}=\frac{\Delta \tilde{I}_{\mathcal{V}}}{\Delta t}
$$

$$
\left.\frac{\Delta \mathcal{S}}{\Delta t}\right|_{\text {micro. }}=\frac{\Delta \tilde{I}_{\mathcal{S}}}{\Delta t}
$$

Changes in $\bar{T}_{l}, \bar{q}_{v}, \text{and } \bar{q}_{c} $  are derived from microphysical tendency terms including precipitation, evaporation, melting/freezing.
### Turbulent mixing

From the definition of s , the PDF variance $V$ becomes
$$
\mathcal{V}=a_{L}^{2}\left(\overline{q_{t}^{\prime 2}}+\alpha_{L}^{2} \Pi \overline{\theta_{l}^{\prime 2}}-2 \alpha_{L} \Pi \overline{q_{t}^{\prime} \theta_{l}^{\prime}}\right)
$$

,where $\Pi$ is the Exner function. From the level-2 closure in by Nakanishi and Niino (2004), the time change of $V$ can be derived as

$$
\begin{aligned}
\left.\frac{\Delta \mathcal{V}}{\Delta t}\right|_{\text {turb. }}=& 2 a_{L}^{2}\left[\left(\alpha_{L} \Pi\right)^{2} K_{H}\left(\frac{\partial \bar{\theta}_{l}}{\partial z}\right)^{2}+K_{q}\left(\frac{\partial \bar{q}_{t}}{\partial z}\right)^{2}\right.\\
&\left.-\alpha_{L} \Pi\left(K_{H}+K_{q}\right) \frac{\partial \bar{\theta}_{l}}{\partial z} \frac{\partial \bar{q}_{t}}{\partial z}\right]-\frac{2 q}{\Lambda_{2}} \mathcal{V},
\end{aligned}
$$
where $K_H$ and $K_q$ are the mixing coefficients for sensible
heat and moisture, respectively. $q^{2}=\overline{u^{\prime 2}+v^{\prime 2}+w^{\prime 2}}$ denotes the turbulent kinetic energy. The other symbols follow the original notation.
Since the turbulence production does not affect the PDF shape parameter defined by the third moment (cf. Tompkins 2002), the skewness change $\Delta \mathcal{S} /\left.\Delta t\right|_{\text {turb. }}$ is simply calculated due to the variance change in (28).

### Subgrid-scale horizontal eddy

In the planetary boundary layer, the subgrid-scale inhomogeneity is dissipated due to the turbulent mixing. In free atmosphere, the grid box will be homogenized mainly due to mesoscale motions, which are expressed by the Newtonian damping as in (Tompkins 2002): $\varepsilon_{\mathcal{V}}=\frac{\mathcal{V}}{\tau_{h}}, \varepsilon_{\mathcal{S}}=\frac{\mathcal{S}}{\tau_{h}}$
where the relaxation timescale is (as it represents the subgrid-scale eddy viscous diffusion) parameterized by the horizontal wind shear as
$$
\tau_{h}^{-1}=C_{s}^{2}\left\{\left(\frac{\partial \bar{u}}{\partial x}\right)^{2}+\left(\frac{\partial \bar{v}}{\partial y}\right)^{2}\right\}^{1 / 2}
$$
where the coefficient $C_{s}$ is set to 0.23 following (Tompkins 2002).
### Other physical processes

Radiation, mass source, and dissipation heating processes change the grid-mean temperature and humidity. Such effect is included in the same way as cloud microphysics.
## Equation solving procedures

The scheme needs two main subroutines PDF2CLD and CLD2PDF.
The subroutine PDF2CLD calculates $C$ and $\bar{q}_{c}$ from $\bar{p}, T_{l,} \bar{q}_{t}, \mathcal{V}, \mathcal{S}$.
The subroutine CLD2PDF calculates $\mathcal{V}$ and $\mathcal{S}$ from $\bar{p}, T_{l,} \bar{q}_{t}, \bar{q}_{c}, C$.

(Watanabe et al. 2009)にならう。
陰解法を用いた解き方について、江守さんのメモを参照する。

### PDF2CLD

#### a,b,q

$$
\mu_{1}=\quad \int_{q-a}^{q+b} x p(x) d x \quad=q+\frac{b-a}{3}
$$

$$
\mu_{2}=\int_{q-a}^{q+b}\left(x-\mu_{1}\right)^{2} p(x) d x=\frac{a^{2}+a b+b^{2}}{18}
$$

$$
\mu_{3}=\int_{q-a}^{q+b}\left(x-\mu_{1}\right)^{3} p(x) d x=\frac{(b-a)\left(2 a^{2}+5 a b+2 b^{2}\right)}{270}
$$

Given $\mu_{1}, \mu_{2}, \mu_{3}$,

We define $\delta \equiv b-a, \beta \equiv a b$.

$$
\delta^{2}+3 \beta=18 \mu_{2}
$$

$$
\delta\left(\beta+12 \mu_{2}\right)=90 \mu_{3}
$$

変形すると

$$
\delta^{3}-54 \mu_{2} \delta+270 \mu_{3}=0
$$

$$
\beta=6 \mu_{2}-\frac{1}{3} \delta^{2}
$$

三次方程式の解の公式を用いて
$$
\delta=2 \sqrt{18 \mu_{2}} \cos \left(\frac{1}{3} \cos ^{-1}\left(\frac{-135 \mu_{3}}{\sqrt{\left(18 \mu_{2}\right)^{3}}}\right)+\frac{4}{3} \pi\right)
$$

$\alpha \equiv a+b$とおけば

$$
\alpha=\sqrt{\delta^{2}+4 \beta}
$$
$$
a=(\alpha-\delta) / 2
$$

$$
b=(\alpha+\delta) / 2
$$

$$
q=\mu_{1}-\delta / 3
$$

とa,b,qが求まった。

#### PDF to C and qc

$$
C=\left\{\begin{array}{ll}
0 & \text { if } b<-Q_{c} \\
\frac{\left(Q_{c}+b\right)^{2}}{(b-q)(b-a)} & \text { if } q \leq-Q_{c} \leq b \\
\frac{\left(Q_{c}+a\right)^{2}}{(q-a)(b-a)} & \text { if } a \leq-Q_{c} \leq q \\
1 & \text { if }-Q_{c}<a
\end{array}\right.
$$

$$
\bar{q}_{c}=\left\{\begin{array}{ll}
0 & \text { if } b<-Q_{c} \\
\frac{1}{3} C\left(Q_{c}+b\right) & \text { if } q \leq-Q_{c} \leq b \\
Q_{c}-\frac{1}{3}(1-C)\left(Q_{c}+a\right) & \text { if } a \leq-Q_{c} \leq q \\
Q_{c} & \text { if }-Q_{c}<a
\end{array}\right.
$$


### CLD2PDF

#### from qc, C to a,b,q

$\left(A \leq-Q_{c} \leq Q\right)$の場合

$$
A=\frac{3\left(Q_{c}-q_{c}\right)}{1-C}-Q_{c}
$$
からAが求まる。

二次方程式
$$
B^{2}+A B-2 A^{2}+\left(Q_{c}+A\right)^{2} /(1-C)=0
$$
のうち意味のある解Bは
$$
B=\left(-A+\sqrt{9 A^{2}-4\left(Q_{c}+A\right)^{2} /(1-C)}\right) / 2
$$

$\left(Q \leq-Q_{c} \leq B\right)$ の場合
$$
B=\frac{3 q_{c}}{C}-Q_{c}
$$

$$
A^{2}+B A-2 B^{2}+\left(Q_{c}+B\right)^{2} / C=0
$$

$$
A=\left(-B-\sqrt{9 B^{2}-4\left(Q_{c}+B\right)^{2} / C}\right) / 2
$$


#### from a,b,q to moment

$$
\mu_{2}=\frac{A^{2}+A B+B^{2}}{6}
$$

$$
\mu_{3}=\frac{Q A B}{10}=\frac{-(A+B) A B}{10}
$$


## Treatment of cloud ice

Cloud ice volume does not change in the process of cloud volume diagnosis.
At first the cloud fraction and cloud water is diagnosed.

1. qc>qi



1. qc<qi

## In-cloud water vapor

