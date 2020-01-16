# A Pytorch Implementation of Tacotron: End-to-end Text-to-speech Deep-Learning Model
Implement google's [Tacotron](https://arxiv.org/abs/1703.10135) TTS system with pytorch. 
![tacotron](asset/arch_fig.jpg)

## Updates
Fork from TTao 


## Requirements
See `used_packages.txt`.


## Usage

* Data  
Download [BZNSYP 標貝dataset](https://www.data-baker.com/open_source.html), which is a Mandarin opensource uni-female-speaker dataset containing 10000 sentences

* Preprocessing
```bash
# Prepare metadata.csv which matches format for this project. It will create `bzn_meta.csv` 
$ python data/prepare_for_bzn.py --data-dir <WHERE_YOU_PATH_TO_DATASET> \
                                 --output-dir bzn_tmp 
                                 
# Generate a directory 'bzn_training/' containing extracted features'
$ python data/preprocess.py --output-dir bzn_training \ 
                            --data-dir <WHERE_YOU_PUT_YOUR_DATASET> \
                            --old-meta bzn_tmp/bzn_meta.csv \
                            --config config/config.yaml
```

* Split dataset
```bash
# Generate 'meta_train.txt' and 'meta_test.txt' in 'bzn_training/'
$ python data/train_test_split.py --meta-all bzn_training/all_bzn_meta.txt \ 
                                  --ratio-test 0.05
```

* Train
```bash
# Start training
$ python main.py --config config/config.yaml \
                 --checkpoint-dir <WHERE_TO_PUT_YOUR_CHECKPOINTS> 

# Continue training
$ python main.py --config config/config.yaml \
                 --checkpoint-dir <WHERE_TO_PUT_YOUR_CHECKPOINTS> \
                 --checkpoint-path <LAST_CHECKPOINT_PATH>
```

* Examine the training process
```bash
# Scalars : loss curve 
# Audio   : validation wavs
# Images  : validation spectrograms & attentions
$ tensorboard --logdir log
```

* Inference
```bash
# Generate synthesized speech 
$ python generate_speech.py --text "For example, Taiwan is a great place." \
                            --output <DESIRED_OUTPUT_PATH> \ 
                            --checkpoint-path <CHECKPOINT_PATH> \
                            --config config/config.yaml
```


## Samples
All the samples can be found [here](https://github.com/ttaoREtw/Tacotron-pytorch/tree/master/samples). These samples are generated after 102k updates.


## Checkpoint
The pretrained model can be downloaded in this [link](https://drive.google.com/file/d/1q8xLo9zyyclIDgYk3V2mczofnQwqT6pk/view?usp=sharing).


## Alignment
The proper alignment shows after **10k** steps of updating.


## Differences from the original Tacotron
1. Gradient clipping
2. Noam style learning rate decay (The mechanism that [Attention is all you need](https://arxiv.org/abs/1706.03762) applies.)

## Acknowlegements
This work is based on r9y9's [implementation](https://github.com/r9y9/tacotron_pytorch) of Tacotron.

## Refenrence
* Tacotron: Towards End-to-End Speech Synthesis [[link](https://arxiv.org/abs/1703.10135)]

