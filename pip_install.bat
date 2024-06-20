@echo off
:: Ensure pip is installed
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip is not installed. Please install pip before running this script.
    exit /b 1
)

:: List of packages to install
set PACKAGES=fair-esm torch torchvision torchaudio git+https://github.com/facebookresearch/esm.git "fair-esm[esmfold]" modelcif biotite dllogger@ git+https://github.com/NVIDIA/dllogger.git git+https://github.com/aqlaboratory/openfold.git@3bec3e9b2d1e8bdb83887899102eff7d42dc2ba9 pepdata

:: Install each package
for %%P in (%PACKAGES%) do (
    echo Installing package: %%P
    python -m pip install %%P
    if %errorlevel% neq 0 (
        echo Failed to install %%P
        exit /b 1
    )
)

echo All packages installed successfully.




