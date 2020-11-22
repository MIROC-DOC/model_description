# Mechanical Processes.

## Basic Equations.

### Basic Equations.

The fundamental equations are a system of primitive equations at the spherical ($\lambda,\varphi$) and $\eta$ coordinates, given as follows (Arakawa and Konor 1996).

1. a series of equations

$$
  \frac{\partial m}{\partial t}
    + \nabla_{\eta} \cdot (m\mathbf{v}_H)+ \frac{\partial (m\dot{\eta})}{\partial \eta} = 0
$$

2. hydrostatic pressure formula

$$
  \frac{\partial \Phi}{\partial \eta} = - \frac{RT_v}{p} m
$$


3. equation of motion

$$
  \frac{\partial \zeta}{\partial t} 
     =   \frac{1}{a\cos\varphi}
            \frac{\partial A_v}{\partial \lambda}
          - \frac{1}{a\cos \varphi}
            \frac{\partial}{\partial \varphi} ( A_u \cos\varphi )
          - {\mathcal D}(\zeta) 
$$

$$
  \frac{\partial D}{\partial t} 
     =    \frac{1}{a\cos\varphi}
            \frac{\partial A_u}{\partial \lambda}
          + \frac{1}{a\cos\varphi}
            \frac{\partial }{\partial \varphi} ( A_v \cos\varphi )
          - \nabla^{2}_{\eta}
           ( \Phi + R \bar{T} \pi + E ) 
          - {\mathcal D}(D) 
$$

4. thermodynamic equation

コメント：$B$は離散化後だけに出てくる変数だと思っていたが、ここでは使わざるを得ない($\dot{p}$を使っていいなら不要だが)

$$
  \frac{\partial T}{\partial t}
     =  - \frac{1}{a\cos\varphi}
               \frac{\partial uT'}{\partial \lambda}
          - \frac{1}{a}
               \frac{\partial }{\partial \varphi} ( vT' \cos\varphi )
          + T' D  \\
        - \dot{\eta} 
              \frac{\partial T }{\partial \eta}
          + \frac{\kappa T}{\sigma} \left[ B\left( \frac{\partial \pi}{\partial t}
                            + {\mathbf{v}}_{H} \cdot \nabla_{\eta}\pi \right)
                            + \frac{ m\dot{\eta} }{ p_s }
                     \right]
          + \frac{Q}{C_{p}}
          + \frac{Q_{diff}}{C_{p}}
          - {\mathcal D}(T) 
$$

5. water vapor formula

$$
  \frac{\partial q}{\partial t}
   =  - \frac{1}{a\cos\varphi}
               \frac{\partial uq}{\partial \lambda}
          - \frac{1}{a\cos\varphi}
               \frac{\partial }{\partial \varphi} (vq \cos\varphi)
          + q D  \\
        - \dot{\eta} \frac{\partial q }{\partial \eta}
          + S_{q}
          - {\mathcal D}(q) 
$$



Here,

$$
m \equiv \left(\frac{\partial p}{\partial \eta}\right)_{p_s} \\
\theta  \equiv  T \left( p/p_{0} \right)^{-\kappa} \\
\kappa  \equiv  R/C_{p} \\
  \Phi  \equiv  gz \\
   \pi  \equiv  \ln p_{S} \\
%
 \dot{\eta}  \equiv   \frac{d \eta}{d t} \\
%
     T_v  \equiv  T ( 1+\epsilon_v q ) \\
     T  \equiv   \bar{T} + T^{\prime} \\
%
 \zeta  \equiv  \frac{1}{a \cos\varphi }
                    \frac{\partial v}{\partial \lambda} 
             -    \frac{1}{a \cos\varphi }
                    \frac{\partial }{\partial \varphi}
                    ( u \cos\varphi ) \\
%
     D  \equiv  \frac{1}{a \cos\varphi }
                    \frac{\partial u}{\partial \lambda} 
             +    \frac{1}{a \cos\varphi }
                    \frac{\partial }{\partial \varphi}
                    ( v \cos\varphi ) \\
%
    A_u  \equiv   ( \zeta + f ) v
             - \dot{\eta} \frac{\partial u}{\partial \eta} 
             - \frac{RT^{\prime}}{a\cos\varphi} 
                  \frac{\partial \pi}{\partial \lambda} 
             + {\mathcal F}_x \\
%
    A_v  \equiv  - ( \zeta + f ) u
             - \dot{\eta} \frac{\partial v}{\partial \eta} 
             - \frac{RT^{\prime}}{a}
                  \frac{\partial \pi}{\partial \varphi} 
             + {\mathcal F}_y \\
%
     E  \equiv   \frac{u^{2}+v^{2}}{2} \\
%
 {\mathbf{v}}_{H} \cdot \nabla
        \equiv  \frac{u}{a \cos \varphi} 
         \left( \frac{\partial }{\partial \lambda} \right)_{\sigma}
     + \frac{v}{a}
         \left( \frac{\partial }{\partial \varphi} \right)_{\sigma} 
            \\
  \nabla^{2}_{\eta}  
        \equiv  
               \frac{1}{a^{2}\cos^2\varphi} 
                 \frac{\partial^{2} }{\partial \lambda^{2}} 
             + \frac{1}{a^{2}\cos\varphi} 
                 \frac{\partial }{\partial \varphi}
                 \left[ \cos\varphi
                       \frac{\partial }{\partial \varphi} \right]  .
$$

${\mathcal D}(\zeta), {\mathcal D}(D), {\mathcal D}(T), {\mathcal D}(q)$ are horizontal diffusion terms, ${\mathcal F}_\lambda, {\mathcal F}_\varphi$ are forces due to small-scale kinetic processes (treated as 'physical processes'), $Q$ are forces due to radiation, condensation, small-scale kinetic processes, etc. Heating and temperature change due to 'physical processes', and $S_q$ is a water vapor source term due to 'physical processes' such as condensation and small-scale motion. $Q_{diff}$ is the heat of friction and

$$
  Q_{diff}
 = - {\mathbf{v}} \cdot  ( \frac{\partial {\mathbf{v}}}{\partial t} )_{diff} .
$$


$( \frac{\partial {\mathbf{v}}}{\partial t} )_{diff}$ is a time-varying term of $u,v$ due to horizontal and vertical diffusion.

### 境界条件

鉛直流に関する上下端の境界条件は以下の通りである：

$$
  \dot{\eta} = 0  \ \ \ at \ \ \eta = 0 , \ 1 .
$$

これを用いて連続の式を鉛直積分することで、$p_s$の予報方程式と、$\dot\eta$の診断方程式が導かれる。

なお、実際の離散化においては$\eta$を陽に用いない表式を用いている。例えば、鉛直移流項$\dot\eta (\partial/\partial\eta)$は以下の等式を利用して、$(m\dot{\eta}/p_s)(\partial/\partial\sigma)$に置き換えて離散化している。

$$
  \dot{\eta}\frac{\partial}{\partial \eta}
  =\dot{\eta}\frac{\partial p}{\partial \eta}\frac{\partial}{\partial p}
  =m\dot{\eta}\frac{\partial}{\partial p}
  =m\dot{\eta}\frac{\partial}{\partial (p_s \sigma)}
  =\frac{m\dot{\eta}}{p_s}\frac{\partial}{\partial \sigma}
$$