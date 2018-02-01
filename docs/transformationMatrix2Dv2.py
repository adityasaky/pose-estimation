
# coding: utf-8

# In[1]:


import numpy as np
import math


# In[2]:


def transformImage2DVector(input2D, scaleFactor, translation2D, rotationFactor, debug=False) :
    txnMatrix = np.zeros([3,3])
    if (debug) :
        print(txnMatrix)
        print(input2D)
    # Vectorized version
    translationMatrix2D = np.identity(3)
    translationMatrix2D[0, 2] = translation2D[0]
    translationMatrix2D[1, 2] = translation2D[1]
    if (debug) :
        print("Translation : ", translationMatrix2D)
    txnMatrix = translationMatrix2D
    
    # Apply the translation
    output2D = np.dot(translationMatrix2D, input2D)
    if (debug) :
        print("TXN matrix after translation : ", txnMatrix)
        print("Output after translation : ", output2D)

    if (scaleFactor > 1) :
        # Apply scaling
        scalingMatrix2D = np.identity(3)
        scalingMatrix2D[0, 0] = scaleFactor
        scalingMatrix2D[1, 1] = scaleFactor
        if (debug) :
            print("Scaling matrix : ", scalingMatrix2D)
        output2D = np.dot(scalingMatrix2D, output2D)
        if (debug) :
            print("Output after scaling : ", output2D)
        txnMatrix = np.dot(scalingMatrix2D, txnMatrix,)
        if (debug) :
            print("TXN matrix after scaling : ", txnMatrix)
        
     
    if (rotationFactor > 0) :
        # Apply rotation
        rotationMatrix2D = np.identity(3)
        rotationMatrix2D[0, 0] = math.cos(rotationFactor)
        rotationMatrix2D[0, 1] = -math.sin(rotationFactor)
        rotationMatrix2D[1, 0] = math.sin(rotationFactor)
        rotationMatrix2D[1, 1] = math.cos(rotationFactor)
        if (debug) :
            print("Rotation matrix : ", rotationMatrix2D)
        output2D = np.dot(rotationMatrix2D, output2D)
        if (debug) :
            print("Output after rotation : ", output2D)
        txnMatrix = np.dot(rotationMatrix2D, txnMatrix)
        if (debug) :
            print("TXN matrix after rotation : ", txnMatrix)
        
    return output2D, txnMatrix


# In[3]:


def testTransformImage2D() :
    input2D = np.array([[1.0, 2.3, 1.0], [1.5, 4.5, 1.0]])
    input2D = input2D.T
    
    translation2D = np.array([1, 1.5])
    #print(translation2D)
    
    scaleFactor = 1.5
    
    rotationFactor = math.pi / 4
    
    output2D, txnMatrix = transformImage2DVector(input2D, scaleFactor, translation2D, rotationFactor)
    print("Txn : ", txnMatrix)
    outputVerify = np.dot(txnMatrix, input2D)
    
    print(output2D)
    print(outputVerify)


# In[4]:


testTransformImage2D()


# In[5]:


# x is the input array 'n' x values representing 'n' points in the image
# 'y' is the input array 'n' y values of the same image points
# tx is the translation uniformly to beapplied along x to all points in image
# ty is the translation uniformly to be applied along y to all points in image
# scale factor to be applied to both x and y (rigid body scaling)
# rotate is the angle in radians to be applied to the image
def transformImage2D(x, y, tx, ty, scale, rotate) :
    if (len(x) != len(y)) :
        print("Lengths of x and y dont match")
        return None
    onesArray = np.ones(len(x))
    xyMatrix = np.vstack((x, y))
    inputTxnMatrix = np.vstack((xyMatrix, onesArray))
    #print(inputTxnMatrix)
    
    txnVector = np.array([tx, ty, 1])
    #print(txnVector)
    
    output2D, txnMatrix = transformImage2DVector(inputTxnMatrix, scale, txnVector, rotate)
    
    return output2D[0], output2D[1], txnMatrix


# In[6]:


x, y, txnMatrix = transformImage2D(np.array([1.0, 1.5]), np.array([2.3, 4.5]), 1.0, 1.5, 1.5, math.pi/4)
print(x)
print(y)
print(txnMatrix)
