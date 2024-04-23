### Setup
Please go through the following steps to create the correct environment.

Run the following commands to create a Python version = 3.11 environment and activate it:
```bash
conda create -n <env_name> python=3.11 anaconda
conda activate <env_name>
```

Run the following commands to install pytorch and cuda-nvcc:
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
conda install nvidia::cuda-nvcc
```

Run the following commands to install apex:
```bash
git clone https://github.com/NVIDIA/apex.git
cd apex
pip install -v --no-cache-dir .
```

Run the following commands to install the required packages. Notice that you probably need to remove the version control for ray[rllib] and tensorflow in requirements.txt:
```bash
cd trademaster-nyu
pip install -r requirements.txt
```

Run the following commands to install packages other than in requirements.txt:
```bash
pip install opencv-python
pip install ipywidgets
pip install yapf==0.40.1
```

Then your environment is set.

## Auto Hyperparameter finetuning Jupyter Notebook script
On going.

