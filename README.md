
# Calysto Hy

Calysto Hy is a Hy kernel for Jupyter based on [Metakernel](https://github.com/Calysto/metakernel). [Hy is a language](https://github.com/hylang/hy) that converts Lisp-like syntax to Python semantics. 

This kernel is based on [bollwyvl/hy_kernel/](https://github.com/bollwyvl/hy_kernel/) That kernel treats Hy as a Python preprocessor, and can therefore use the standard IPython tools. Calysto Hy treats Hy as a full language. Because of this, it uses the MetaKernel to gain magics, shell, parallel processing, etc.

## Install

If you want to enjoy full code completion by [kaschalk/jedhy](https://github.com/ekaschalk/jedhy) you have
use bleeding edge and install hy master (> 0.13.1), jedhy and toolz first because jedhy is using new hy syntax.
Otherwise calysto_hy falls back to is normal completion.


```shell
pip3 install git+https://github.com/hylang/hy.git
pip3 install git+https://github.com/ekaschalk/jedhy.git
pip3 install toolz
pip3 install git+https://github.com/Calysto/calysto_hy.git
python3 -m calysto_hy install
```

If installing into the system, you may want to:

```shell
sudo pip3 install git+https://github.com/hylang/hy.git
sudo pip3 install git+https://github.com/ekaschalk/jedhy.git
sudo pip3 install toolz
sudo pip3 install git+https://github.com/Calysto/calysto_hy.git
sudo python3 -m calysto_hy install
```

Or into your personal space:

```shell
pip3 install git+https://github.com/hylang/hy.git --user
pip3 install git+https://github.com/ekaschalk/jedhy.git --user
pip3 install toolz --user
pip3 install git+https://github.com/Calysto/calysto_hy.git --user
python3 -m calysto_hy install --user
```

Or into a virtualenv, when it is already activated:

```shell
pip3 install git+https://github.com/hylang/hy.git
pip3 install git+https://github.com/ekaschalk/jedhy.git
pip3 install toolz
pip3 install git+https://github.com/Calysto/calysto_hy.git
python3 -m calysto_hy install --sys-prefix
```

## Use

```shell
jupyter console --kernel calysto_hy
```

You can use Calysto Hy in Jupyter notebook by selecting the "Calysto Hy" kernel. See example [notebooks](https://github.com/Calysto/calysto_hy/tree/master/notebooks).
