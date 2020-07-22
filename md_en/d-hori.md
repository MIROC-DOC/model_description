## Horizontal discretization

The horizontal discretization of the
The spectral transformation method is used (Bourke, 1988).
The differential terms for longitude and latitude are evaluated by orthogonal function expansion,
On the other hand, non-linear terms are computed on the grid points.

### Spectral Expansion.

As an expansion function system, it is a Laplacian eigenfunction system on a sphere
The spherical harmonic function $Y_n^m(\lambda,\mu)$ are used.
with $\mu \equiv \sin\varphi$.
$Y_n^m$ satisfies the following equation,

$$
\nabla^{2}_{\sigma} Y_n^m(\lambda,\mu) 
= - \frac{n(n+1)}{a^{2}} Y_n^m(\lambda,\mu) 
$$


Using the Legendre junction number $P_n^m$ it is written as follows.

$$
Y_n^m(\lambda,\mu) = P_n^m (\mu) e^{im \lambda}
$$


but $ n \geq | m | $.

The expansion by the spherical harmonic function is written as ,

$$
   {Y_n^m}_{ij} \equiv Y_n^m ( \lambda_i, \mu_j )
$$


If you write ,

$$
  X_{ij} \equiv X ( \lambda_i, \mu_j )
  =  {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
        X_n^m {Y_n^m}_{ij} ,
$$

> <span id="Spherical Expansion" label="Spherical Expansion">\\\blur[Spherical Expansion]</span>

The inverse of that is ,

$$
  X_n^m 
         =  \frac{1}{4 \pi} 
             \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
               X( \lambda, \mu ) Y_n^{m *} ( \lambda, \mu ) \\
         =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               X_{ij} {Y_n^{m*}}_{ij} w_j 
$$
  
> <span id="Deployment Factor" label="Deployment Factor">\\\.com[Deployment Factor]</span>


.
When evaluating by replacing the integral with the sum,
See Gauss's trapezoidal formula for the $\lambda$ integral,
We use the Gauss-Legendre integral formula for the $\mu$ integral.
$\mu_j$ is the Gauss latitude and $w_j$ is the Gauss load.
Also, $\lambda_i$ is a grid of evenly spaced Gauss loads.

Using the spectral expansion, we can obtain a new formula for Gauss-Legendre integration,
The grid point values for the terms containing the derivatives are found as follows.

$$
        \left(  \frac{\partial X}{\partial \lambda} \right)_{ij}
     =  
        {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       im X_n^m {Y_n^m}_{ij}
$$

> <span id="barometric pressure x" label="barometric pressure x">\a[barometric pressure x]</span>.

$$
   \left( \cos\varphi \frac{\partial X}{\partial \varphi} \right)_{ij}
     =  {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} \sum_{n=|m|}^{N} 
       X_n^m 
       ( 1-\mu^{2} ) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}
$$

> <span id="barometric y" label="barometric y" label="barometric y">\blaze[barometric y]</span>.

Furthermore,
From the spectral components of $\zeta$ and $D$,
The grid point values for $u,v$ are obtained as follows.

$$
  u_{ij}
  = \frac{1}{\cos\varphi}
     {\mathcal R}\mathbf{e} \sum_{m=-N}^{N} 
                       \sum_{\stackrel{n=|m|}{n \neq 0}}^{N} 
    \left\{
             \frac{a}{n(n+1)} \zeta_n^m 
            (1-\mu^{2}) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}
          -  \frac{im a}{n(n+1)} D_n^m {Y_n^m}_{ij}
    \right\}
$$

> <span id="Seeking U" label="Seeking U" label="Seeking U">\\[Seeking U]</span>.

$$
  v_{ij}
  = \frac{1}{\cos\varphi}
   {\mathcal R}\mathbf{e} \sum_{m=-N}^{N}
                     \sum_{\stackrel{n=|m|}{n \neq 0}}^{N}
    \left\{
          -  \frac{im a}{n(n+1)} \zeta_n^m {Y_n^m}_{ij}
          -  \frac{a}{n(n+1)} D_n^m 
            (1-\mu^{2}) \frac{\partial }{\partial \mu} {Y_n^m}_{ij}
    \right\}
$$

> <span id="Seeking V" label="Seeking V">\\\[V seeking]</span>

The derivative that appears in the advection term of the equation is,
It is required as follows.

> <span id="A integral" label="A integral" label="A integral">\[A integral]</span>
$$
  \left( \frac{1}{a\cos\varphi} \frac{\partial A}{\partial \lambda} \right)_n^m 
   =  \frac{1}{4 \pi} 
        \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
          \frac{1}{a\cos\varphi} \frac{\partial A}{\partial \lambda} Y_n^{m *} \\
   =  \frac{1}{4 \pi} 
        \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda \,
          im A \cos\varphi \frac{1}{a(1-\mu^{2})} Y_n^{m *} \\
   =  \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          im A_{ij} \cos\varphi_j
          {Y_n^{m *}}_{ij} \frac{w_j}{a(1-\mu_j^{2})} 
$$
  
  


> <span id="B integral" label="B integral" label="B integral">B integral\blazer\blazer]</span>.
$$
  \left( \frac{1}{a\cos\varphi} 
         \frac{\partial }{\partial \varphi} (A\cos\varphi) \right)_n^m 
    =  \frac{1}{4 \pi a} 
         \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
           \frac{\partial }{\partial \mu} (A\cos\varphi) Y_n^{m *}  \\
    =  - \frac{1}{4 \pi a} 
         \int_{-1}^{1} d \mu \int_{0}^{\pi} d \lambda 
           A \cos\varphi \frac{\partial }{\partial \mu} Y_n^{m *}
            \\
   =  - \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
          A_{ij}  \cos\varphi_j
          (1-\mu_j^2)  \frac{\partial }{\partial \mu} 
          {Y_n^{m *}}_{ij} \frac{w_j}{a(1-\mu_j^{2})} 
$$
  
  


Further ,

$$
     \left( \nabla^{2}_{\sigma} X \right)_n^m
       =  - \frac{n(n+1)}{a^{2}} X_n^m
$$


to evaluate the term $\nabla^2$.

### Horizontal Diffusion Term.

The horizontal diffusion term is entered in the form $\nabla^{N_D}$ as follows.

$$
  {\mathcal D}(\zeta) = K_{MH} 
                      \left[ (-1)^{N_D/2} \nabla^{N_D}
                              - \left( \frac{2}{a^2} \right)^{N_D/2} 
                      \right]
                    \zeta ,
$$

> <span id="Horizontal Diffusion" label="Horizontal Diffusion">Regular\[Horizontal Diffusion]</span>.

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


This horizontal diffusion term has strong implications for computational stability.
In order to represent selective horizontal diffusion on small scales,
For $N_D$, 4 $\sim$ 16 is used.
The extra terms on the diffusion of vorticity and divergence are
It represents that the term for rigid body rotation in $n=1$ does not decay.

### Spectral representation of the equation

1. a series of equations

$$
  \frac{\partial \pi_m^m}{\partial t}
  =  - \sum_{k=1}^{K} (D_n^m)_k \Delta  \sigma_k  \\
     + \frac{1}{I} \sum_{i=1}^{I} \sum_{j=1}^{J}  
               Z_{ij} {Y_n^{m *}}_{ij} w_j  ,
$$
  


    Here,

$$
Z \equiv - \sum_{k=1}^{K} \mathbf{v}_k \cdot \nabla \pi .
$$


2. equation of motion

$$
  \frac{\partial \zeta_n^m}{\partial t} 
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
  \frac{\partial \tilde{D}_n^m}{\partial t} 
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
  \frac{\partial T_n^m}{\partial t}
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
  \frac{\partial q_n^m}{\partial t}
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


