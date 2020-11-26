# pmlsc: Large Scale Condensation

## Physical basis for statistical PDF scheme

GCMs typically adopt fractional cloud cover to realistically represent clouds because of its coarse horizontal resolution ($O(100km)$).
A common approach to calculating the grid-mean cloud cover is to assume that there is a subgrid‐scale distribution of humidity within the grid and to calculate the cloud cover from the portion of the distribution that is above saturation.
Sophisticated cloud schemes that predict higher moments like variance and skewness and are called statistical cloud schemes.
The majority of statistical cloud schemes use the so-called "s-distribution", following Sommeria and Deardorff (1977).
A single variable $s$, which considers the subgrid-scale perturbations of liquid temperature $T_l$ and total water $q_t$, is employed.
$q_t$ is sum of water vapor and cloud water.


$$
q_{c}=\left(q_{t}-q_{s}\right) \delta\left(q_{t}-q_{s}\right)
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

Watanabe et al. 2009にならう

The shape of the PDF is represented by a skewed-triangular function.
The model preicts variance and skewness of the PDF, which are affected by cumulus convection, cloud microphysics, turbulent mixing, and advection.

## Equation solving procedures

(Watanabe et al. 2009)にならう。
陰解法を用いた解き方について、江守さんのメモを参照する。