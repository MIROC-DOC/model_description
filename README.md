# Model Description for MIROC6-AGCM

## GitHub directory structure

### [convert](./convert)

Tools to compile md and tex files in [descript](./descript) to single pdf file in [draft](./draft), etc.

### [descript](./descript)

Md and tex files. These are part of Model Description for MIROC6-AGCM.

### [draft](./draft)

Compiled PDF file "Model Description for MIROC6-AGCM".

### [memo](./memo)

### [org](./org)

Original old files for the AGCM.

## Help us with updating [Model Description for MIROC6-AGCM](https://github.com/MIROC-DOC/model_description/blob/master/draft/agcm.pdf)

- Create your GitHub account and contact MIROC-DOC Admin via e-mail to miroc.github.info [at] gmail.com.
- Edit the file on GitHub Blowser(easy way, [procedure](https://github.com/MIROC-DOC/model_description/blob/develop/memo/develop.md#%E9%96%8B%E7%99%BA%E3%83%95%E3%83%AD%E3%83%BC%E7%B0%A1%E6%98%93%E7%89%88)) or your local([procedure](https://github.com/MIROC-DOC/model_description/blob/develop/memo/develop.md#%E9%96%8B%E7%99%BA%E3%83%95%E3%83%AD%E3%83%BC%E8%A9%B3%E7%B4%B0%E7%89%88%E6%96%B0%E3%81%97%E3%81%8F%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E4%BD%9C%E3%82%8B%E5%A0%B4%E5%90%88%E8%A4%87%E6%95%B0%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E7%B7%A8%E9%9B%86%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88%E3%81%AA%E3%81%A9)).

Otherwise, send an e-mail to miroc.github.info [at] gmail.com.
If the content of your email is not relevant to the case, we may not respond.

## Contents
1. Introduction 概論
- 1.1 [Characteristics of MIROC6 AGCM](draft/summary.md)
- 1.2 [Features and Structure of the Model](descript/a-intro.md)
- 1.3 [Basic Settings](draft/a.0-setup.md)

2. Dynamics 力学過程
- 2.1  [Basic Equations (基礎方程式)](draft/d.1-basic.tex)
- 2.2  [Vertical Discretization (鉛直離散化)](draft/d.2-vert.tex)
- 2.3  [Horizontal Descretization (水平離散化)](draft/d.3-hori.md)
- 2.4  [Time Integration　（時間積分）](draft/d.4-time.tex)
- 2.5  [Tracer Advection Scheme (トレーサー流)](draft/d.5-tracer.tex)
- 2.6  [Summary of the Dynamical Core (力学過程のまとめ)](draft/d.6-summ.md)
- 2.7  [Computational Flow of Dynamical Core](draft/d.7-routine.md)

3. Physics 物理過程
- 3.1 [Overview of Physical Parameterizations](draft/p-intro.md)
- 3.2 [Cumulus Scheme (積雲対流)](draft/p-cum.md)
- 3.3 [Shallow Convection Scheme (浅い対流)](draft/shallowconv_en.tex)
- 3.4 [Large Scale Condensation (大規模凝結)](draft/Hotta_pmlsc.md)
- 3.5 [Cloud Microphysics (雲微物理)](draft/Hotta_pcldphys.md)
- 3.6 [Radiation Scheme (放射)](draft/p-rad.md)
- 3.7 [Turbulance Scheme (乱流)](draft/p-dif_en.md)
- 3.8 [Surface Flux Scheme (地表フラックス)](draft/p-sfc.md) *陸面(地表)過程については、[ILS-DOC](https://github.com/integrated-land-simulator/model_description)を参照のこと*
- 3.9 [Gravity Waves (重力波)](draft/p-grav.md)

4. Miscellaneous その他
- 4.1 [Coupler](draft/AO-coupler.md)
- 4.2 [Definition of Land-Sea Distribution](draft/Model-Grid.md)

5. [References 引用文献](draft/referenc.tex)


# リンク集
-   [Wiki](../../wiki)
    -   [自動変換作業](../../wiki/自動変換作業)
    -   [コンパイルの方法](../../wiki/コンパイルの方法)
    -   [これまでの経緯](../../wiki/これまでの経緯)
    -   [管理者の仕事](../../wiki/管理者の仕事)
