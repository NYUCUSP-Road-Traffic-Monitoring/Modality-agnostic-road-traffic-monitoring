# NYU CUSP Road Traffic Monitoring

**[Report]()**

**[Website]()**

**Team members**: Eve Shi, Yao Hou 

**Directors**: Bea Steers, Magdalena Fuentes

Support by: NYU Center for Urban Science and Progress, NYU Music and Audio Research Laboratory

Sponsors: Bosch

This project provides a multi-modality machine learning framework for traffic monitoring, which fits either audio or video-images traffic data. Our framework eliminates the limitations of poor visibility or noisy environments that have a huge impact on single-modality methods and shows a comparable performance (76% accuracy).

## Dataset

We present a labelled traffic video dataset with 421 2-fps 10-second video clips, which contains different illumination and weather situations, to fill the gap of labeled dataset now in the field of traffic monitoring. To test our framework, you can download our dataset from [here](https://drive.google.com/drive/folders/1Ho6l0lmUZZKbzQdzj1Ly-LEUrOXNfeTT?usp=sharing). The instructions for using the dataset is in the root folder, you can also find it at [this link](https://drive.google.com/file/d/1i2br-krYcBnghRblgjJFkUhVGNvAiJDu/view?usp=sharing).

## Codes

### Embeddings

1. Untranslated embeddings: you can use codes from any current embedding methods. In this project, we use [yamnet](https://github.com/tensorflow/models/tree/master/research/audioset/yamnet) and resnet(https://github.com/pytorch/vision/blob/6db1569c89094cf23f3bc41f79275c45e9fcb3f3/torchvision/models/resnet.py#L124).
2. Translated embeddings. You can use codes from [here](https://github.com/hohsiangwu/crossmodal).

### Analysis

#### Installation

```sh
# Install Python libraries using conda
conda env create -f environment.yml
conda activate modality_agnostic
python -m ipykernel install --user --name modality_agnostic --display-name "modality_agnostic"

# Run the notebook
jupyter notebook
```

### Read Annotations

If you use our example dataset, you can download annotations from [here](https://drive.google.com/file/d/19oscKAd2WnwM6mheuv3tbkMQC3vQ7sUb/view?usp=sharing). Otherwise, you can use `utils/annotation_reader.py` as an example to read your own annotations.

### Models and Analysis

Run annotations and embeddings with `*.ipynb`.
