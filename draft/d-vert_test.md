Table of contents

- Vertical Discretization
  - Model levels (数式・説明をハイブリッド化済)
  - Vertical discretization (数式をハイブリッド化済)
  - Differences from $\sigma$-coordinate (新規追加)

## Vertical Discretization

Following Arakawa and Konor (1996) but in the Lorentz grid, the basic equations are discretized vertically by differences. This scheme has the following characteristics.

 - Save the total integrated mass

 - Save the total integrated energy

 - Preserving angular momentum for global integration

 - Conservation of total mass-integrated potential temperature

 - The hydrostatic pressure equation comes down to local (the altitude of the lower level is independent of the temperature of the upper level)

 - For a given temperature distribution, constant in the horizontal direction, the hydrostatic pressure equation becomes accurate and the barometric gradient force becomes zero.

 - Isothermal atmosphere stays isothermal forever

### Model levels

下の層から上へと層の番号をつける。$\zeta,D,T,q$の物理量は整数レベル(layer)で定義されるとし、鉛直速度$\dot{\eta}$は半整数レベルにおいて定義する。ただし、$\frac{1}{2}$は下端($\eta=1$)、$K+\frac{1}{2}$は上端($\eta=0$)である。さらに、半整数レベルにおける気圧$p$を以下の式で定義する。

$$
p_{k+1/2} = A_{k+1/2} +B_{k+1/2}\,p_s
$$

よって、$\sigma\equiv p/p_s$は以下のように表せる。

$$
\sigma_{k+1/2} = \frac{A_{k+1/2}}{p_s} +B_{k+1/2}
$$

また、基準地表気圧$p_0=1000\ \mathrm{hPa}$を用いて$\eta$を次の式で定義する。

$$
\eta_{k+1/2} = \frac{A_{k+1/2}}{p_0} +B_{k+1/2}
$$

整数レベルにおける気圧$p_k, (k=1,2,\ldots K)$は次の式で内挿する。

$$
 p_k = \left[ \frac{1}{1+\kappa}
                     \left( \frac{  p_{k-1/2}^{\kappa +1}
                                  - p_{k+1/2}^{\kappa +1}      }
                                  { p_{k-1/2} - p_{k+1/2} }
                     \right)
              \right]^{1/\kappa}
$$

さらに、

$$
  \Delta\sigma_k \equiv \sigma_{k-1/2} - \sigma_{k+1/2} \\
  \Delta B_k \equiv B_{k-1/2} - B_{k+1/2}
$$

を定義しておく。

### Vertical discretization

各方程式のハイブリッド座標における離散化表現は次のようになる。

1. 連続の式、鉛直速度

$$
  \frac{\partial \pi}{\partial t}
 = - \sum_{k=1}^{K} \left[ D_k \Delta\sigma_k + ({\mathbf{v}}_k \cdot \nabla \pi)\Delta B_k \right]
$$

$$
  \frac{(m\eta)_{k-1/2}}{p_s}
 = - B_{k-1/2} \frac{\partial \pi}{\partial t}
$$

$$
  \frac{(m\dot{\eta})_{k-1/2}}{p_s}
 = - B_{k-1/2} \frac{\partial \pi}{\partial t}
$$

$$
  \frac{(m\dot{\eta})_{k-1/2}}{p_s}
 = - B_{k-1/2} \frac{\partial \pi}{\partial t} - \sum_{l=k}^{K}\left[ D_l \Delta\sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l \right]
$$

$$
  \dot{\eta}_{1/2} = \dot{\eta}_{K+1/2} = 0
$$

2. 静水圧の式

$$
 \Phi_{1}  =  \Phi_{s} + C_{p} ( \sigma_{1}^{-\kappa} - 1  ) T_{v,1} \\
           =  \Phi_{s} + C_{p} \alpha_{1} T_{v,1} 
$$

$$
 \Phi_k - \Phi_{k-1} 
   =  C_{p}
   \left[ \left( \frac{ p_{k-1/2} }{ p_k } \right)^{\kappa}
          - 1 \right] T_{v,k} 
       + C_{p}
   \left[ 1- 
         \left( \frac{ p_{k-1/2} }{ p_{k-1} } \right)^{\kappa}
              \right] T_{v,k-1} \\
   =    C_{p} \alpha_k T_{v,k} + C_{p} \beta_{k-1} T_{v,k-1}
$$

ここで、

$$
 \alpha_k \equiv \left( \frac{ p_{k-1/2} }
                               { p_k } \right)^{\kappa} -1 \\
 \beta_k \equiv  1- \left( \frac{ p_{k+1/2} }
                               { p_k } \right)^{\kappa} .
$$

3. 運動方程式

$$
  \frac{\partial \zeta_k}{\partial t} 
        =   \frac{1}{a\cos\varphi} 
            \frac{\partial (A_v)_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi} 
            \frac{\partial }{\partial \varphi} (A_u \cos\varphi)_k
          - {\mathcal D}(\zeta_k) 
$$


$$
  \frac{\partial D}{\partial t} 
        =   \frac{1}{a\cos\varphi} 
            \frac{\partial (A_u)_k}{\partial \lambda}
          + \frac{1}{a\cos\varphi} 
            \frac{\partial }{\partial \varphi} (A_v \cos\varphi)_k
          - \nabla^{2}_{\sigma}
           ( \Phi_k + R\bar{T} \pi 
             + ({\mathit KE})_k )
          - {\mathcal D}(D_k) 
$$

ここで、$\bar{T}$はリファレンスとなる気温であり、デフォルトでは全層で300Kである。また、

$$
  (A_u)_k
    =  ( \zeta_k + f ) v_k 
             - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{u_{k-1} - u_k}{\Delta\sigma_{k-1}+\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{u_k   - u_{k+1}}{\Delta\sigma_{k}+\Delta\sigma_{k+1}} \right]
            \\
           - \frac{1}{a\cos\varphi} \frac{\partial \pi}{\partial \lambda}(C_p T_{v,k}\hat{\kappa}-R\bar{T})
             + {\mathcal F}_x
$$

$$
  (A_v)_k
    =  - ( \zeta_k + f ) u_k 
             - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{v_{k-1} - v_k}{\Delta\sigma_{k-1}+\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{v_k   - v_{k+1}}{\Delta\sigma_{k}+\Delta\sigma_{k+1}} \right]
            \\
           - \frac{1}{a} \frac{\partial \pi}{\partial \varphi}(C_p T_{v,k}\hat{\kappa}-R\bar{T})
             + {\mathcal F}_y
$$

$$
   \hat{\kappa}_k 
    = \frac{ B_{k-1/2} \alpha_k + B_{k+1/2} \beta_k }
            { \Delta\sigma_k                                  } 
$$

4. 熱力学方程式

$$
  \frac{\partial T_k}{\partial t}
     =  - \frac{1}{a\cos\varphi}
               \frac{\partial u_k T'_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (v_k T'_k \cos\varphi)
          + H_k  \\
        + \frac{Q_k}{C_{p}}
          + \frac{(Q_{diff})_k}{C_p} 
          - {\mathcal D}(T_k)  \\
$$

ここで、

$$
   H_k 
     \equiv  T_k' D_k
              - \left[   \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{\hat{T}_{k-1/2} - T_k}{\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{T_k - \hat{T}_{k+1/2}}{\Delta\sigma_k} \right]
                \\
        + \frac{1}{\Delta \sigma_k} T_{v,k}\ \alpha_k
                    \left[ B_{k-1/2} {\mathbf{v}}_k \cdot \nabla \pi
                          - \sum_{l=k}^{K} 
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                    \right] \\
          + \frac{1}{\Delta \sigma_k} T_{v,k}\ \beta_k
                     \left[ B_{k+1/2} {\mathbf{v}}_k \cdot \nabla \pi
                          - \sum_{l=k+1}^{K} 
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                    \right] \\
%
     =  T_k' D_k 
          - \left[ \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{\hat{T}_{k-1/2} - T_k}{\Delta \sigma_l}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{T_k - \hat{T}_{k+1/2}}{\Delta \sigma_l} \right]
                \\
        + \hat{\kappa}_k {\mathbf{v}}_k \cdot \nabla \pi T_{v,k} 
                \\
        - \alpha_k \sum_{l=k}^{K} 
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                            \frac{T_{v,k}}{\Delta \sigma_k} 
                \\
        - \beta_k \sum_{l=k+1}^{K} 
                           (D_l \Delta \sigma_l + ({\mathbf{v}}_l \cdot \nabla \pi)\Delta B_l)
                            \frac{T_{v,k}}{\Delta \sigma_k}
$$

$$
  \hat{T}_{k-1/2}
   = a_k T_k + b_{k-1} T_{k-1}
$$

$$
  a_k  =  \alpha_k 
              \left[ 1- \left( \frac{ p_k }{ p_{k-1} }
                        \right)^{\kappa} \right]^{-1}   \\
  b_k  =  \beta_k 
              \left[ \left( \frac{ p_k }{ p_{k+1} } 
                     \right)^{\kappa} - 1 \right]^{-1} .  
$$

5. 水蒸気の時間発展方程式

$$
  \frac{\partial q_k}{\partial t}
      =   - \frac{1}{a\cos\varphi} 
               \frac{\partial u_k q_k}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} ( v_k q_k\cos\varphi)
          + R_k 
          + S_{q,k}
          - {\mathcal D}(q_k) 
$$

$$
R_k  =  q_k D_k 
       - \frac{1}{2} 
             \left[   \frac{(m\dot{\eta})_{k-1/2}}{p_s} \frac{q_{k-1} - q_k}{\Delta\sigma_k}
               + \frac{(m\dot{\eta})_{k+1/2}}{p_s} \frac{q_k   - q_{k+1}}{\Delta\sigma_k} \right]
$$

### Differences from $\sigma$-coordinate

ここではハイブリッド座標を、できるだけ$\sigma$座標に近い表式で離散化したため、両者の差は比較的少ない。重要な対応関係を以下に挙げる。

- 全層で$A_{k+1/2}=0$とすれば、ハイブリッド座標は$\sigma$座標に帰着する。
- ハイブリッド座標における$\Delta B_k$と$\Delta \sigma_k$は、$\sigma$座標系においては両者とも$\Delta \sigma_k$に対応する。
- ハイブリッド座標における$m\dot{\eta}/p_s$は、$\sigma$座標系における$\dot{\sigma}$に対応する。