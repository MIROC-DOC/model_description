## Horizontal discretization

The horizontal discretization is based on the spectral transformation method (Bourke, 1988). The differential terms for longitude and latitude are evaluated by the orthogonal function expansion, while the non-linear terms are calculated on the grid.

### Spectral Expansion.

As an expansion function, the spherical harmonic functions $Y_n^m(\lambda,\mu)$, which are eigenfunction of Laplacian on a sphere, are used. However, $\mu \equiv \sin\varphi$ is used. $Y_n^m$ satisfies the following equation,

$$
\nabla^{2}_{\sigma} Y_n^m(\lambda,\mu) 
= - \frac{n(n+1)}{a^{2}} Y_n^m(\lambda,\mu) 
$$


Using the Legendre jury function $P_n^m$ it is written as follows.

$$
Y_n^m(\lambda,\mu) = P_n^m (\mu) e^{im \lambda}
$$


However, it is $ n \geq | m | $.

The expansion by spherical harmonic functions is ,

$$
   {Y_n^m}_{ij} \equiv Y_n^m ( \lambda_i, \mu_j )
$$


When I write ,

$$
  X_{ij} \equiv X ( \lambda_i, \mu_j )
  =  {\mathcal R}{$\mathbf{e}$} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
        X_n^m {Y_n^m}_{ij} ,
$$


The inverse of that is ,

$$
  X_n^m 
         =  \frac{1}{4 \pi} 
             \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
               X( \lambda, \mu ) Y_n^{m *} ( \lambda, \mu ) \\
         =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               X_{ij} {Y_n^{m*}}_{ij} w_j 
$$



The formula is expressed as To evaluate by replacing the integral with a sum, we use the Gauss trapezoidal formula for the $\lambda$ integral and the Gauss-Legendre integral formula for the $\mu$ integral. $\mu_j$ is the Gauss latitude and $w_j$ is the Gauss load. Also, $\lambda_i$ is a grid of evenly spaced Gauss loads.

Using spectral expansion, the grid point values of the terms containing the derivatives can be calculated as follows.

$$
        \left(  \frac{\partial X}{\partial \lambda} \right)_{ij}
     =  
        {\mathcal R}{$\mathbf{e}$} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       im X_n^m {Y_n^m}_{ij}
$$


$$
   \left( \cos\varphi \frac{\partial X}{\partial \varphi} \right)_{ij}
     =  {\mathcal R}{$\mathbf{e}$} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       X_n^m 
       ( 1-\mu^{2} ) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}
$$


Furthermore, the grid point values of $u,v$ can be obtained from the spectral components of $\zeta$ and $D$ as follows

$$
  u_{ij}
  = \frac{1}{\cos\varphi}
     {\mathcal R}{$\mathbf{e}$} \sum_{m=-N}^{N} 
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N} 
    \left\{
             \frac{a}{n(n+1)} \zeta_n^m 
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y_n^m}_{ij}
          -  \frac{im a}{n(n+1)} D_n^m {Y_n^m}_{ij}
    \right\}
$$


$$
  v_{ij}
  = \frac{1}{\cos\varphi}
   {\mathcal R}{$\mathbf{e}$} \sum_{m=-N}^{N}
                     \sum_{\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
          -  \frac{im a}{n(n+1)} \zeta_n^m {Y_n^m}_{ij}
          -  \frac{a}{n(n+1)} D_n^m 
            (1-\mu^{2}) \frac{\partial{}}{\partial {\mu}} {Y_n^m}_{ij}
    \right\}
$$


The derivative appearing in the advection term of the equation is calculated as

$$
  \left( \frac{1}{a\cos\varphi} \frac{\partial{A}}{\partial {\lambda}} \right)_n^m 
   =  \frac{1}{4 \pi} 
        \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
          \frac{1}{a\cos\varphi} \frac{\partial{A}}{\partial {\lambda}} Y_n^{m *} \\
   =  \frac{1}{4 \pi} 
        \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda \,
          im A \cos\varphi \frac{1}{a(1-\mu^{2})} Y_n^{m *} \\
   =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im A_{ij} \cos\varphi_j
          {Y_n^{m *}}_{ij} \frac{w_j}{a(1-\mu_j^{2})} 
$$




$$
  \left( \frac{1}{a\cos\varphi} 
         \frac{\partial{}}{\partial {\varphi}} (A\cos\varphi) \right)_n^m 
    =  \frac{1}{4 \pi a} 
         \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
           \frac{\partial{}}{\partial {\mu}} (A\cos\varphi) Y_n^{m *}  \\
    =  - \frac{1}{4 \pi a} 
         \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
           A \cos\varphi \frac{\partial }{\partial \mu} Y_n^{m *}
            \\
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          A_{ij}  \cos\varphi_j
          (1-\mu_j^2)  \frac{\partial }{\partial \mu} 
          {Y_n^{m *}}_{ij} \frac{w_j}{a(1-\mu_j^{2})} 
$$




Furthermore,

$$
     \left( \nabla^{2}_{\sigma} X \right)_n^m
       =  - \frac{n(n+1)}{a^{2}} X_n^m
$$


to be used for the evaluation of the $\nabla^2$ section.

### Horizontal Diffusion Term

The horizontal diffusion term is entered in the form $\nabla^{N_D}$ as follows.

$$
  {\mathcal D}(\zeta) = K_{MH} 
                      \left[ (-1)^{N_D/2} \nabla^{N_D}
                              - \left( \frac{2}{a^2} \right)^{N_D/2} 
                      \right]
                    \zeta ,
$$


$$
     {\mathcal D}(D) = K_{MH} 
                      \left[ (-1)^{N_D/2} \nabla^{N_D}
                              - \left( \frac{2}{a^2} \right)^{N_D/2} 
                      \right]
                    D ,
$$


$$
    {\mathcal D}(T) = (-1)^{N_D/2} K_{HH} \nabla^{N_D} T ,
$$


$$
    {\mathcal D}(q) = (-1)^{N_D/2} K_{EH} \nabla^{N_D} q .
$$


This horizontal diffusion term has strong implications for computational stability. In order to represent selective horizontal diffusion on small scales, 4 $\sim$ 16 is used as $N_D$. Here, the extra term for vorticity and divergence diffusion indicates that the term of rigid body rotation in $n=1$ does not decay.

### Spectral representation of equations

1. a series of equations

$$
  \frac{\partial{\pi_m^m}}{\partial {t}}
  =  - \sum_{k=1}^{K} (D_n^m)_k \Delta  \sigma_k  \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               Z_{ij} {Y_n^{m *}}_{ij} w_j  ,
$$



 Here,

$$
Z \equiv - \sum_{k=1}^{K} {$\mathbf{v}$}_k \cdot \nabla \pi .
$$


2. equation of motion

$$
  \frac{\partial{\zeta_n^m}}{\partial {t}} 
   =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im (A_v)_{ij} \cos\varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})} 
          \\
   +    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          (A_u)_{ij} \cos\varphi_j
          (1-\mu_j^2) 
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})} 
          \\ 
   -   ({\mathcal D}_M)_n^m \zeta_n^m  \; ,
$$




$$
  \frac{\partial{\tilde{D}_n^m}}{\partial {t}} 
   =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im (A_u)_{ij} \cos\varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})} 
          \\
   -    \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          (A_v)_{ij} \cos\varphi_j
          (1-\mu_j^2) 
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})} 
          \\
   -   \frac{n(n+1)}{a^{2}} 
         \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          E_{ij} {Y_n^{m *}}_{ij} w_j
          \\ 
   +   \frac{n(n+1)}{a^{2}} 
          ( \Phi_n^m + C_{p} \hat{\kappa}_k \bar{T}_k \pi_n^m ) 
          -  ({\mathcal D}_M)_n^m D_n^m  ,
$$





 However,

$$
({\mathcal D}_M)_n^m = K_{MH} \left[ 
                            \left( \frac{n(n+1)}{a^{2}} \right)^{N_D/2}
                            - \left( \frac{2}{a^2} \right)^{N_D/2}
                            \right]  .
$$


3. thermodynamic equation

$$
  \frac{\partial{T_n^m}}{\partial {t}}
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im u_{ij} T'_{ij} \cos\varphi_j
          {Y_n^{m *}}_{ij}
         \frac{w_j}{a(1-\mu_j^{2})} 
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          v_{ij} T'_{ij} \cos\varphi_j
          (1-\mu_j^2) 
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})} 
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \left( H_{ij} + \frac{Q_{ij}+Q_{diff}}{C_{p}} \right)
          {Y_n^{m *}}_{ij} w_j
          \\ 
     - (\tilde{\mathcal D}_H)_n^m T_n^m \; ,
$$





 However,

$$
({\mathcal D}_H)_n^m 
   =  K_{HH} \left( \frac{n(n+1)}{a^{2}} \right)^{N_D/2} .
$$


4. water vapor formula

$$
  \frac{\partial{q_n^m}}{\partial {t}}
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im u_{ij} q_{ij} \cos\varphi_j
          {Y_n^{m *}}_{ij} \frac{w_j}{a(1-\mu_j^{2})} 
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          v_{ij} q_{ij} \cos\varphi_j
          (1-\mu_j^2) 
          \frac{\partial }{\partial \mu} {Y_n^{m *}}_{ij}
          \frac{w_j}{a(1-\mu_j^{2})} 
          \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          \left( \hat{R}_{ij} + S_{q,ij} \right)
          {Y_n^{m *}}_{ij} w_j
          \\ 
     + ({\mathcal D}_H)_n^m q_n^m
$$





 However,

$$
({\mathcal D}_E)_n^m 
   =  K_{EH} \left( \frac{n(n+1)}{a^{2}} \right)^{N_D/2} .
$$

