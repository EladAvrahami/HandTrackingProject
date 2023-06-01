
<h2>Hand Tracking - basic</h2>

![image](https://github.com/EladAvrahami/HandTrackingProject/assets/86184072/b6d139b9-1f1a-477f-b460-a4f1139a71f4)


quiqe setup python 3.10 and above 
pycharm -> settings->project->interpreter-> install opencv-python & mediapipe packages


<pre style='font-family:Arial, Helvetica, sans-serif'>
#1
Hands include parameters like: the defoult is to be false 
                static_image_mode=False,- if it false somtimes it detect and sometimes it will track depends the confidence level of detection
               max_num_hands=2, -is the max num of hands it can track/detect
               min_detection_confidence=0.5, -to be confident about the obj it should be higher than 50%
               min_tracking_confidence=0.5)  -case lower than 50% it will do the detection again

more about google mediaPipe->  https://developers.google.com/mediapipe/solutions/vision/hand_landmarker
openCV fonts->                 https://www.oreilly.com/library/view/mastering-opencv-4/9781789344912/16b55e96-1027-4765-85d8-ced8fa071473.xhtml



</pre>
