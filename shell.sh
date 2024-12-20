#!/bin/bash

# Environment name
ENV_NAME="featuregenie"

# Python version for the environment
PYTHON_VERSION="3.9"

# Packages to install (optional)
PACKAGES=("numpy" "pandas" "matplotlib" "seaborn" "scikit-learn")

# Function to display error messages and exit
function error_exit {
    echo "Error: $1"
    exit 1
}

# Check if Conda is installed
if ! command -v conda &> /dev/null; then
    error_exit "Conda is not installed. Please install Conda first."
fi

# Check if the environment already exists
if conda info --envs | grep -w "$ENV_NAME" &> /dev/null; then
    echo "Environment '$ENV_NAME' already exists. Use 'conda activate $ENV_NAME' to activate it."
    exit 0
fi

# Create the environment
echo "Creating Conda environment '$ENV_NAME' with Python $PYTHON_VERSION..."
if ! conda create -q -y -n "$ENV_NAME" python="$PYTHON_VERSION"; then
    error_exit "Failed to create the Conda environment."
fi

# Activate the environment
echo "Activating the environment '$ENV_NAME'..."
source "$(conda info --base)/etc/profile.d/conda.sh"
if ! conda activate "$ENV_NAME"; then
    error_exit "Failed to activate the Conda environment."
fi

# Install additional packages
if [ ${#PACKAGES[@]} -gt 0 ]; then
    echo "Installing packages: ${PACKAGES[*]}..."
    if ! conda install --yes "${PACKAGES[@]}"; then
        error_exit "Failed to install additional packages."
    fi
fi

echo "Conda environment '$ENV_NAME' created and activated successfully!"
echo "Use 'conda activate $ENV_NAME' to activate it in the future."
