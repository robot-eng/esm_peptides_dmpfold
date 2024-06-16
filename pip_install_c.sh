#!/bin/bash

# Install packages using pip
pip install fair-esm
pip install torch torchvision torchaudio
pip install git+https://github.com/facebookresearch/esm.git
pip install "fair-esm[esmfold]"
pip install modelcif
pip install biotite
pip install dllogger @ git+https://github.com/NVIDIA/dllogger.git
pip install -q git+https://github.com/aqlaboratory/openfold.git@3bec3e9b2d1e8bdb83887899102eff7d42dc2ba9
