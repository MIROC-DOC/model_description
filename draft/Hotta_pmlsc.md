# pmlsc: Large Scale Condensation

## Physical basis for statistical PDF scheme

GCMs typically adopt fractional cloud cover to realistically represent clouds because of its coarse horizontal resolution ($O(100km)$).
A common approach to calculating the grid-mean cloud cover is to assume that there is a subgrid‐scale distribution of humidity within the grid and to calculate the cloud cover from the portion of the distribution that is above saturation.
PDF
Sophisticated cloud schemes that predict higher moments like variance and skewness and are called statistical cloud schemes.
The majority of statistical cloud schemes use the so-called "s-distribution", following Sommeria and Deardorff (1977).
A single variable $s$, which considers the subgrid-scale perturbations of liquid temperature $T_l$ and total water $q_t$, is employed.
$q_t$ is sum of water vapor and cloud water.


$$
q_{c}=\left(q_{t}-q_{s}\right) \delta\left(q_{t}-q_{s}\right)
\tag{hpc.1}
$$


For any choice of $G(s)$, the grid-mean cloud fraction, $C$, and cloud water content, $qc$, are obtained by integrating $G(s)$ and $(Qc + s)G(s)$, where $Qc$ denotes the grid-scale saturation deficit.

$$
\begin{aligned}
&q_{c}=\left\{\begin{array}{ll}
Q_{c}+s & \text { for }-Q_{c}<s \\
0 & \text { for }-Q_{c} \geq s
\end{array}\right.\\
&\text { where }\\
&s=a_{L}\left(q_{t}^{\prime}-\alpha_{L} T_{l}^{\prime}\right)
\end{aligned}
$$


## Hybrid Prognostic Cloud (HPC) scheme

The statistical scheme implemented in MIROC6 is called Hybrid Prognostic Cloud (HPC) scheme (Watanabe et al. 2009).
The shape of the PDF is represented by a skewed-triangular function.

![](https://cdn.mathpix.com/snip/images/sT9QRiYBjSFFuHN6tYy1yHx4Md81UVA2xIGKupuEoLE.original.fullsize.png)


The model preicts variance ($V$) and skewness ($S$) of the PDF, which are affected by cumulus convection, cloud microphysics, turbulent mixing, and advection.

## Processes

Everytime after the processes that affects cloud water PDF,

### Dynamical Process
### Cumulus convection

Cumulus convections modify the grid-mean enthalpy and total water by transporting the net moist energy upward.

$$
\left.\frac{\Delta \mathcal{V}}{\Delta t}\right|_{\mathrm{conv} .}=M_{c} \frac{\partial \mathcal{V}}{\partial z}+\frac{\Delta \tilde{I}_{\mathcal{V}}}{\Delta t}
$$

$$
\left.\frac{\Delta \mathcal{S}}{\Delta t}\right|_{\mathrm{conv} .}=M_{c} \frac{\partial \mathcal{S}}{\partial z}+\frac{\Delta \tilde{I}_{\mathcal{S}}}{\Delta t}
$$


$$
\left.\frac{\partial \bar{h}}{\partial t}\right|_{\mathrm{conv} .}=M_{c} \frac{\partial \bar{h}}{\partial z}+D\left(h^{t}-\bar{h}\right)
$$

$$
\left.\frac{\partial \bar{q}_{v}}{\partial t}\right|_{\mathrm{conv} .}=M_{c} \frac{\partial \bar{q}_{v}}{\partial z}+D\left(q_{v}^{t}-\bar{q}_{v}\right)
$$

$$
\left.\frac{\partial \bar{q}_{c}}{\partial t}\right|_{\mathrm{conv} .}=M_{c} \frac{\partial \bar{q}_{c}}{\partial z}+D\left(q_{c}^{t}-\bar{q}_{c}\right)
$$

the detrainment of the cloudy air mass is included, as in Bushell et al.

$$
\left.\frac{\partial C}{\partial t}\right|_{\mathrm{conv} .}=D(1-C)
$$

D = g/P*CBMFX

tracer in CUMFXR

### Cloud Microphysics

The tendency due to microphysical processes can be
written in a similar manner to the cumulus effect

$$
\left.\frac{\Delta \mathcal{V}}{\Delta t}\right|_{\text {micro. }}=\frac{\Delta \tilde{I}_{\mathcal{V}}}{\Delta t}
$$

$$
\left.\frac{\Delta \mathcal{S}}{\Delta t}\right|_{\text {micro. }}=\frac{\Delta \tilde{I}_{\mathcal{S}}}{\Delta t}
$$

Changes in $\bar{T}_{l}, \bar{q}_{v}, \text{and } \bar{q}_{c} $  are derived from microphysical tendency terms including precipitation, evaporation, melting/freezing.

$\Delta C$ is assumed to be 0.

### Turbulent mixing and Subgrid-scale horizontal eddy

From the definition of s (see Appendix 1), the PDF
variance becomes
$$
\mathcal{V}=a_{L}^{2}\left(\overline{q_{t}^{\prime 2}}+\alpha_{L}^{2} \Pi \overline{\theta_{l}^{\prime 2}}-2 \alpha_{L} \Pi \overline{q_{t}^{\prime} \theta_{l}^{\prime}}\right)
$$

### Other physical processes

radiation/mass src/dry conv


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

