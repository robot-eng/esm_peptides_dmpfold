# ESM / Peptides
### Ref: [facebookresearch:esm](https://github.com/facebookresearch/esm), [openvax:pepdata](https://github.com/openvax/pepdata), [THGLab:int2cart](https://github.com/THGLab/int2cart)

<p align="center">
    <img src="https://th.bing.com/th/id/R.492d8ce81dda15d5bd1b9543e14d7576?rik=%2bBTSDBOdKUyOOg&riu=http%3a%2f%2ffiles.abovetopsecret.com%2ffiles%2fimg%2fte566e15d5.gif&ehk=YkaOSAsr%2bjwlj7F3n96fIIpZOsMPPnSW1nz%2fvC3wn7M%3d&risl=&pid=ImgRaw&r=0">
</p>

## Pip install LiBRARY
>🧾 **Note** : Main LiBRARY 1.esm 2.pepdata 3.SidechainNet 4.pdbtools [5.pyrosetta](https://rosettacommons.github.io/PyRosetta.notebooks/)
### windows
```
.\pip_install.bat
```
> :warning: **Warning** : Windows should use wsl and install cuda and cudnn.

### ubuntu / Linux
```
chmod +x pip_install.sh

./pip_install.sh
```
### Colab and ubuntu / Linux
```colab
# Install dos2unix tool
!apt-get install dos2unix

# Convert file format
!dos2unix pip_install_c.sh

# Make the script executable
!chmod +x pip_install_c.sh

# Run the script
!./pip_install_c.sh

```
## Convert colab to pdf
```
!apt-get install texlive texlive-xetex texlive-latex-extra pandoc
!pip install pypandoc
# and
!jupyter nbconvert --to pdf --output name.pdf /location_file/file.ipynb
```
## Set up openfold for Create environment

<p>In this guide, we will OpenFold and its dependencies.</p>

### Pre-requisites

<p>This package is currently supported for CUDA 11 and Pytorch 1.12. All dependencies are listed in the <code>environment.yml</code></p>

<p>At this time, only Linux systems are supported.</p>

## Instructions Installation:

Clone the repository, e.g. `git clone https://github.com/aqlaboratory/openfold.git`

### From the openfold repo:

Create a Mamba environment, e.g. `mamba env create -n openfold_env -f environment.yml` Mamba is recommended as the dependencies required by OpenFold are quite large and mamba can speed up the process.

Activate the environment, e.g `conda activate openfold_env`

### Run the setup script to configure kernels and folding resources.

`scripts/install_third_party_dependencies.sh`

Prepend the conda environment to the `$LD_LIBRARY_PATH`., e.g. `export $LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH`. You may optionally set this as a conda environment variable according to the conda docs to activate each time the environment is used.

Download parameters. We recommend using a destination as openfold/resources as our unittests will look for the weights there.

### For AlphaFold2 weights, use

`./scripts/download_alphafold_params.sh`

### For OpenFold weights, use :

`./scripts/download_openfold_params.sh`

### For OpenFold SoloSeq weights, use:

`./scripts/download_openfold_soloseq_params.sh`

### Checking your build with unit tests:
To test your installation, you can run OpenFold unit tests. Make sure that the OpenFold and AlphaFold parameters have been downloaded, and that they are located (or symlinked) in the directory openfold/resources

### Run with the following script:

`scripts/run_unit_tests.sh`

The script is a thin wrapper around Python’s unittest suite, and recognizes unittest arguments. E.g., to run a specific test verbosely:

`scripts/run_unit_tests.sh -v tests.test_model`

Alphafold Comparison tests: Certain tests perform equivalence comparisons with the AlphaFold implementation. Instructions to run this level of tests requires an environment with both AlphaFold 2.0.1 and OpenFold installed, and is not covered in this guide. These tests are skipped by default if no installation of AlphaFold is found.

### Environment specific modifications
**CUDA 12**
To use OpenFold on CUDA 12 environment rather than a CUDA 11 environment. In step 1, use the branch pl_upgrades rather than the main branch, i.e. replace the URL in step 1 with `https://github.com/aqlaboratory/openfold/tree/pl_upgrades` Follow the rest of the steps of Installation Guide

### MPI
To use OpenFold with MPI support, you will need to add the package mpi4py. This can be done with pip in your OpenFold environment, e.g. `$ pip install mpi4py`.

### Install OpenFold parameters without aws
If you don’t have access to aws on your system, you can use a different download source:

**HuggingFace (requires git-lts):** `scripts/download_openfold_params_huggingface.sh`

**Google Drive:** `scripts/download_openfold_params_gdrive.sh`

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
