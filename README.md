## Implicit Joint Semantic Segmentation of Images and Point Cloud
##### keywords: Deep learning, semantic segmentation, ALS point cloud, aerial imagery
```
Master Thesis in University of Stuttgart,Insititute of Photogrammetry (Ifp), Germany
Author: Fangwen Shu
Betreuer: M.Sc. Dominik Laupheimer
Prüfer: apl. Prof. Dr.-Ing. Norbert Haala

framework: keras 2.0
pre-processing: python3
semantic segmentation: python2

End in 01.04.2018
```

<img src="https://github.com/PeterFWS/masterThesis_BK/blob/master/imgs/pipline.png" width="600">


## Configuration of conda env

./conda_env/py2.yml <br>
./conda_env/py3.yml <br>

```
conda env export > py2.yml <br>
conda env create -f py2.yml
```


## Pre-processing part
```buildoutcfg
main.py
```
pre-processing code for aerial imagery and LiDAR point cloud, including 3D-2D projection, frustum culling, 
Hidden-point-removal (HPR), gird interpolation and operator of Morphology.

```
./utilities.py
```
functions of each of algorithms implemented in pre-processing.

```
./myClasses.py
```
some classes related to frustum culling, traslated from C++ code, detailed explanation in OpenGL.

```
./visualization.py
```
functions used to visualize data. 

```
./statistics.py
```
functions used to calculate statistic information of the data.

```
./Generation_depth_img.py
```
code for generating depth image.

## Deep learning part
./version_playground <br>
Old code backup, including point splatting achieved in C++ if you needed.<br>

./semantic-segmentation <br>
[1] ./semantic-segmentation/Models/: 
1. SegNet (main model used in thesis)
2. U-net (not test)
3. TernausNet (not test)

[2] ./semantic-segmentation/board/: <br>
where you save tensorboard file.

[3] ./semantic-segmentation/data/: <br>
where you save train/validation/test-set and VGG pre-treained weights.

[4] ./semantic-segmentation/weights/: <br>
where you save trained weights.

[5] ./semantic-segmentation/pytorch_code/: <br>
some dirty code of SegNet and pre-processing implemented in pytorch. 

Code:<br>
[1] train.py and prediction.py <br>
train and prediction your data.

[2] LoadBatches.py <br>
loading data with pre-processing such as normalization.

[3] chip.py <br>
cropping images if you need.

[4] evaluation.py <br>
evaluation semantic result in 2D and 3D space.

