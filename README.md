# ESM
## Ref: https://github.com/facebookresearch/esm
## The python instructions on the computer/notebook should be as follows:
```cmd
$pip install virtualenv
$python -m venv venv 
$venv\Scripts\activate
```
## Type error 
```
/usr/local/lib/python3.10/dist-packages/deepspeed/runtime/utils.py and /usr/local/lib/python3.10/dist-packages/deepspeed/runtime/zero/stage_1_and_2.py 
ModuleNotFoundError: No module named 'torch._six'
```
## modify
```
from torch._six import inf  
```
to
```
from torch import inf
```
