# DOG & CAT CLASSIFIER<br>

Dog and cat image classifier using feature extraction techniques and machine learning based classification models.<br><br>

![alt text](project_image.jpg)

## Used feature extractors:

## Extractor 1 :
This method of feature extraction consists of:

1. split the image into NxN sized cells 
2. Assign each neighbouring pixel a value of 0 or 1 depending on the intensity.
3. Using the neighbour values to make a binary number and assigning that colour to the central pixel.
4. Once you have done that with everyone calculate a histogram per cell.

#### Results: 
| Dataset | Accuracy | Run Time |
|--------------|-----------|------------|
| "cat_dog_100" | 95% | 16.30 seconds |
| "cat_dog_500" | 92.5% | 4 minutes 26.28 seconds |


## Extractor 2 :
This feature extraction method involves three steps: 

1. Apply convolution filters to calculate the magnitude and orientation of the gradient.
2. Divide the image into disjoint blocks and create histograms for each block. 
3. Normalise the histograms. 


#### Results: 
| Dataset | Accuracy | Run Time |
|--------------|-----------|------------|
| "cat_dog_100" | 92.5%| 16.46 seconds |
| "cat_dog_500" | 90% | 1 minutes 27.68 seconds |

## Classifier used:

Scikit-learn SVM

https://scikit-learn.org/stable/modules/svm.html


---
## Explanatory videos (In Spanish):

## Video
[![VIDEO](http://img.youtube.com/vi/89BA7UG2XS8/0.jpg)](https://www.youtube.com/watch?v=89BA7UG2XS8 "Video")

## Video Codigo
[![VIDEO](http://img.youtube.com/vi/PlR-ZUXZUCc/0.jpg)](https://www.youtube.com/watch?v=PlR-ZUXZUCc "Video2")


---
Created by Odei H. and Endika A. 2022-2023


