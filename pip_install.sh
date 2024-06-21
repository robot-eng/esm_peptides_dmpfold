#!/bin/bash

# Function to install a package using pip
install_package() {
  PACKAGE_NAME=$1
  echo "Installing package: $PACKAGE_NAME"
  pip install "$PACKAGE_NAME"

  if [ $? -eq 0 ]; then
    echo "$PACKAGE_NAME installed successfully."
  else
    echo "Failed to install $PACKAGE_NAME."
    exit 1
  fi
}

# Ensure pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found"
    exit 1
fi

# List of packages to install
PACKAGES=(
  "fair-esm"
  "pepdata"
  "torch"
  "torchvision"
  "torchaudio"
  "git+https://github.com/facebookresearch/esm.git"
  "fair-esm[esmfold]"
  "modelcif"
  "biotite"
  "'dllogger@ git+https://github.com/NVIDIA/dllogger.git'"
  "git+https://github.com/aqlaboratory/openfold.git@3bec3e9b2d1e8bdb83887899102eff7d42dc2ba9"
)

# Install each package
for PACKAGE in "${PACKAGES[@]}"; do
  install_package "$PACKAGE"
done

echo "All packages installed successfully."
