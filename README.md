# annotation-reader-and-viz
# NYU CUSP Road Traffic Monitoring Video Annotation
Sponsors: Bea Steers, Magdalena Fuentes

Team members: Qianyi Eve Shi, Yao Hou

This is an annotation dataset for road traffic monitoring. The dataset is currently used in the NYU CUSP capstone project **Modality-agnostic road traffic monitoring**. The original data is collected from the Bosch Group and part of TAU Urban Audio-Visual Scenes 2021, Development dataset. For pravicy, all personal information in the videos are all mosaic processed. 

The data authorized by the Bosch Group is only for research purpose. The videos have a relatively clear and higher view of the objects.

The TAU Urban Audio-Visual Scenes 2021 dataset contains 10-seconds video segments of major cities in Europe (Barcelona, Helsinki, Lisbon, London, Lyon, Milan, Paris, Prague, Stockholm, Vienna). Acoustic scenes include pedestrian streets, public squares, bridges, fast lanes, crossings, urban parks and so on.    
Audio | Video | Duration 
----- | ----- | --------
48kHz  | 30fps | Each clip is 10 sec
24 bits | 1280*720 | Total 34hs 
stereo| | Relevant 4hs
Zoom P8+binaural |GoPro Hero 5|   

For more information about TAU Urban Audio-Visual Scenes 2021, Development dataset, please visit: https://zenodo.org/record/4477542#.YLeK3JNKjMI

The group mixed the two original dataset together and the material is totally 1.2 hour long. The following plot shows the percentage of the components.   
![image missing](../main/img_folder/dataset_pie.png)

# Basic Analysis   
**Annotation Difficulty**  
The group has considered mixing different difficulty level data together in the dataset. We use the number of annotated objects to distinguish the annotation difficulty.   
Annotation Difficulty | Number of Annotated Objects   
--------------------- | ---------------------------
Easy | < 4  
Medium | >=4 && <10   
Hard | >=10   

The following pie plot and bar plot illustrate the difficulty composition of dataset. The Easy clips ranks the first, Medium is the second, and Hard is the last.      

![image missing](../main/img_folder/level_pie.png) ![image missing](../main/img_folder/level_bar.png)  

**Labels**    
Label is the standard of image classification. The more detailed the classification, the higher the accuracy of the model. The group labelled the object into 5 categories: bicycle, bus, car, truck, motorbike. The plots show their proportion. Cars are the most common objects in the annotation. The rest labels occupy a little in this annotation dataset.

![image missing](../main/img_folder/label_pie.png) ![image missing](../main/img_folder/label_bar.png)  

**Illumination Condition**       
The illumination condition affects the result of image segmentation and might reduce the recognition rate. To generalize the model, the dataset has mixed day and night conditions. The easy level occurs the most and the hard level is the least occured in the day annotations, the medium level occurs the most and the easy level is the least in the night annotations.    

![image missing](../main/img_folder/daynight_pie.png) ![image missing](../main/img_folder/daynight_bar.png)  

**Weather**     
Different weather conditions have effect on the annotation. The group noticed 2 special weather conditions: snow, rain. The weather condition in the dataset is also shown below. About 10 percent of data is under special weather. The rainy days are all easy-level but snowy days cover all difficulty levels. 

![image missing](../main/img_folder/weather_pie.png) ![image missing](../main/img_folder/weather_bar.png) 
