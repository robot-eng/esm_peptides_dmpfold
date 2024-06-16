pip install fair-esm  # latest release, OR:
pip install torch torchvision torchaudio
pip install git+https://github.com/facebookresearch/esm.git  # bleeding edge, current repo main branch
#-----------------------#
pip install "fair-esm[esmfold]" 
pip modelcif biotite
# OpenFold and its remaining dependency
pip install 'dllogger @ git+https://github.com/NVIDIA/dllogger.git'
pip install -q git+https://github.com/aqlaboratory/openfold.git@3bec3e9b2d1e8bdb83887899102eff7d42dc2ba9