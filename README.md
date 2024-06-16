# ESM
## Ref: https://github.com/facebookresearch/esm
![image](https://github.com/robot-eng/esm/assets/79349006/2e7104c3-e586-433f-ba6b-fc08e3e27ff8)
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
