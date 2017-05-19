
# Calysto Hy

Calysto Hy is a Hy kernel for Jupyter based on [Metakernel](https://github.com/Calysto/metakernel). [Hy is a language](https://github.com/hylang/hy) that converts Lisp-like syntax to Python semantics. 

This kernel is based on [bollwyvl/hy_kernel/](https://github.com/bollwyvl/hy_kernel/) That kernel treats Hy as a Python preprocessor, and can therefore use the standard IPython tools. Calysto Hy treats Hy as a full language. Because of this, it uses the MetaKernel to gain magics, shell, parallel processing, etc.

## Install

```shell
pip3 install git+https://github.com/Calysto/calysto_hy.git
python3 -m calysto_hy install
```
If installing into the system, you may want to:

```shell
sudo pip3 install git+https://github.com/Calysto/calysto_hy.git
sudo python3 -m calysto_hy install
```

Or into your personal space:

```shell
pip3 install git+https://github.com/Calysto/calysto_hy.git --user
python3 -m calysto_hy install --user
```

Or into a virtualenv, when it was already activate:

```shell
pip3 install git+https://github.com/Calysto/calysto_hy.git
python3 -m calysto_hy install --sys-prefix
```

## Use

```shell
jupyter console --kernel calysto_hy
```

You can use Calysto Hy in Jupyter notebook by selecting the "Calysto Hy" kernel. See example [notebooks](https://github.com/Calysto/calysto_hy/tree/master/notebooks).
