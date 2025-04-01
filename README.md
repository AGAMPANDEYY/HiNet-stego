
# HiNet-stego

HiNet-stego leverages the HiNet framework for steganography to train models on an ImageNet-based dataset. The project automates the setup process by cloning the original [HiNet repository](https://github.com/TomTomTommi/HiNet), installing dependencies, and integrating the Kaggle ImageNet steganography dataset.

## Features

- **Automated Setup:** Clones and configures the HiNet framework.
- **Kaggle Integration:** Downloads and unpacks the steganography ImageNet dataset.
- **Training Pipeline:** Initiates training using the HiNet model.

## Requirements

- Python 3.6+
- [Kaggle API](https://github.com/Kaggle/kaggle-api)
- [TensorboardX](https://github.com/lanpa/tensorboardX)
- Additional dependencies listed in `requirements.txt`

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AGAMPANDEYY/HiNet-stego.git
   cd HiNet-stego
   ```

2. **Install Dependencies**

   Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   pip install -q tensorboardX kaggle
   ```

3. **Configure Kaggle API**

   Upload your `kaggle.json` file (using Colab or your local setup):

   ```python
   from google.colab import files
   files.upload()  # Upload kaggle.json
   ```

   Then configure Kaggle credentials:

   ```bash
   mkdir -p ~/.kaggle
   cp kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

4. **Dataset Setup**

   Create a directory for the dataset and download it:

   ```bash
   mkdir -p /content/imagenet/
   curl -L -o /content/imagenet/dataset.zip \
     https://www.kaggle.com/api/v1/datasets/download/abhinav1609/steganography-imagenet
   unzip -q /content/imagenet/dataset.zip -d /content/imagenet
   ```

5. **Run Training**

   The training process is triggered by the script in `hinet.py`. Run it in a Jupyter Notebook or Colab environment:

   ```bash
   python train.py
   ```

## Usage

- **Training:** Executes a steganography training pipeline using the HiNet framework.
- **Customization:** Modify the configuration or scripts as needed to suit your specific dataset or training parameters.

> **Note:** The `main.py` file currently contains a placeholder script. The core functionality is handled via `hinet.py`.

## Acknowledgements

- Original HiNet repository by [TomTomTommi](https://github.com/TomTomTommi/HiNet).
