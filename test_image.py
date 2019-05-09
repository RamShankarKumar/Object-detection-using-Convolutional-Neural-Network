# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:24:24 2019

@author: Ram Shankar Kumar
"""
def main():
        # -*- coding: utf-8 -*-
    """
    Created on Sun May  5 13:52:15 2019
    
    @author: Ram Shankar Kumar
    """
    
    import darkflow
    from darkflow.net.build import TFNet
    import cv2
    import numpy as np
    
    options = {"model": "E:\\project\\minor project 2\\darkflow-master\\cfg\\tiny-yolo-voc-30c.cfg","labels": "E:\\project\\minor project 2\\darkflow-master\\labels.txt", "load": 66750 , "threshold": 0.01,"gpu": 1.0}
    
    tfnet = TFNet(options)
    
    original_img = cv2.imread("E:\\project\\minor project 2\\darkflow-master\\sample_img\\test.jpg")
    original_img = cv2.cvtColor(original_img,cv2.COLOR_BGR2RGB)
    results = tfnet.return_predict(original_img)
    print(results)
    np.savetxt("result of prediction",results,fmt='%s')
    
    Confidence1 = results[0]
    confid = Confidence1['confidence']
    #print(confid)
    
    for result in results:
        Confidence2 = result['confidence']
        if Confidence2 > confid:
            confid = Confidence2
            
    for result in results:                    #this loop is just for knowing the label of the highest confidence tuple
            top_x = result['topleft']['x']
            top_y = result['topleft']['y']
            btm_x = result['bottomright']['x']
            btm_y = result['bottomright']['y']
            confidence = result['confidence']
            label = result['label']
            if confidence == confid:
                label2 = label
     
    #print(label2)
    #print(type(label2))
    f= open("E:\\project\\minor project 2\\darkflow-master\\sample_img\\breedname.txt","w+")
    f.write(label2)
    f.close()
    
    def boxing(original_img, results):
        newImage = np.copy(original_img)
        for result in results:
            top_x = result['topleft']['x']
            top_y = result['topleft']['y']
            btm_x = result['bottomright']['x']
            btm_y = result['bottomright']['y']
            confidence = result['confidence']
            label = result['label'] + " " + str(round(confidence, 3))
            #print(result['label'])
            #if confidence > 0.3:
            if confidence == confid:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (0,0,255),2)
                #newImage = cv2.putText(newImage, label, (top_x-5, top_y+80), cv2.FONT_HERSHEY_COMPLEX_SMALL , 1.0, (255,255, 255), 2, cv2.LINE_AA)
                cv2.imwrite('E:\\project\\minor project 2\\darkflow-master\\sample_img\\result.jpg',newImage)
        return newImage
    
    
    import matplotlib.pyplot as plt
    _, ax = plt.subplots(figsize=(20, 10))
    ax.imshow(boxing(original_img, results))
    
    fimg = cv2.imread("E:\\project\\minor project 2\\darkflow-master\\sample_img\\result.jpg")
    fimg1 = cv2.cvtColor(fimg,cv2.COLOR_BGR2RGB)
    cv2.imwrite('E:\\project\\minor project 2\\darkflow-master\\sample_img\\result.jpg',fimg1)

if __name__ == "__main__":
    main()