# Model Description for MIROC6-AGCM

## GitHub directory structure

### [current_document](./current_document)

Compiled single PDF file "Model Description for MIROC6-AGCM".

### [descript_files](./descript_files)

Markdown files. These are part of Model Description for MIROC6-AGCM.

[Chrome Extension](https://chrome.google.com/webstore/detail/mathjax-3-plugin-for-gith/peoghobgdhejhcmgoppjpjcidngdfkod) enables LaTeX equations previews on Github.

### [for_admin](./for_admin)

Files for the administrators.

### [memo](./memo)

Useful information to edit files.

## Help us with updating [Model Description for MIROC6-AGCM](https://github.com/MIROC-DOC/model_description/blob/master/current_document/agcm.pdf)

- Create your GitHub account and contact MIROC-DOC Admin via e-mail to **miroc.github.info [at] gmail.com**.
- Edit the file on GitHub Blowser(easy way, [procedure](https://github.com/MIROC-DOC/model_description/blob/master/memo/edit_files(ファイル編集方法).md#編集フロー簡易版)) or your local([procedure](https://github.com/MIROC-DOC/model_description/blob/master/memo/edit_files(ファイル編集方法).md#編集フロー詳細版新しくファイルを作る場合複数ファイルを編集する場合など)).

Otherwise, send an e-mail to **miroc.github.info [at] gmail.com**.
If the content of your email is not relevant to the case, we may not respond.

## Contents
1. Introduction 概論
- 1.1 [Characteristics of MIROC6 AGCM](descript_files/summary.md)
- 1.2 [Features and Structure of the Model](descript_files/a-intro.md)
- 1.3 [Basic Settings](descript_files/a.0-setup.md)

2. Dynamics 力学過程
- 2.1  [Basic Equations (基礎方程式)](descript_files/d.1-basic.md)
- 2.2  [Vertical Discretization (鉛直離散化)](descript_files/d.2-vert.md)
- 2.3  [Horizontal Descretization (水平離散化)](descript_files/d.3-hori.md)
- 2.4  [Time Integration　（時間積分）](descript_files/d.4-time.md)
- 2.5  [Tracer Advection Scheme (トレーサー流)](descript_files/d.5-tracer.md)
- 2.6  [Summary of the Dynamical Core (力学過程のまとめ)](descript_files/d.6-summ.md)
- 2.7  [Computational Flow of Dynamical Core](descript_files/d.7-routine.md)

3. Physics 物理過程
- 3.1 [Overview of Physical Parameterizations](descript_files/p-intro.md)
- 3.2 [Cumulus Scheme (積雲対流)](descript_files/p-cum.md)
- 3.3 [Shallow Convection Scheme (浅い対流)](descript_files/p-shallowconv.md)
- 3.4 [Large Scale Condensation (大規模凝結)](descript_files/p-mlsc.md)
- 3.5 [Cloud Microphysics (雲微物理)](descript_files/p-cldphys.md)
- 3.6 [Radiation Scheme (放射)](descript_files/p-rad.md)
- 3.7 [Turbulance Scheme (乱流)](descript_files/p-dif.md)
- 3.8 [Surface Flux Scheme (地表フラックス)](descript_files/p-sfc.md) *陸面(地表)過程については、[ILS-DOC](https://github.com/integrated-land-simulator/model_description)を参照のこと*
- 3.9 [Gravity Waves (重力波)](descript_files/p-grav.md)

4. Miscellaneous その他
- 4.1 [Coupler](descript_files/AO-coupler.md)
- 4.2 [Definition of Land-Sea Distribution](descript_files/Model-Grid.md)

5. [References 引用文献](for_admin/convert/tex/referenc.tex)


# リンク集
-   [Wiki](../../wiki)
    -   [自動変換作業](../../wiki/自動変換作業)
    -   [コンパイルの方法](../../wiki/コンパイルの方法)
    -   [これまでの経緯](../../wiki/これまでの経緯)
    -   [管理者の仕事](../../wiki/管理者の仕事)
