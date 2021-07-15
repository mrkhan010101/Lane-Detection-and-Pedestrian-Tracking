import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import hog
def get_hog_features(img, orient, pix_per_cell, cell_per_block, 
                        vis=False, feature_vec=True):
    # Call with two outputs if vis==True
    if vis == True:
        features, hog_image = hog(img, orientations=orient, 
                                  pixels_per_cell=(pix_per_cell, pix_per_cell),
                                  cells_per_block=(cell_per_block, cell_per_block), 
                                  transform_sqrt=True, 
                                  visualise=vis, feature_vector=feature_vec)
        return features, hog_image
    # Otherwise call with one output
    else:      
        features = hog(img, orientations=orient, 
                       pixels_per_cell=(pix_per_cell, pix_per_cell),
                       cells_per_block=(cell_per_block, cell_per_block), 
                       transform_sqrt=True, 
                       visualise=vis, feature_vector=feature_vec)
        return features

# Define a function to compute binned color features  
def bin_spatial(img, size=(32, 32)):
    # Use cv2.resize().ravel() to create the feature vector
    features = cv2.resize(img, size).ravel() 
    # Return the feature vector
    return features

# Define a function to compute color histogram features 
# NEED TO CHANGE bins_range if reading .png files with mpimg!
def color_hist(img, nbins=32, bins_range=(0, 256)):
    # Compute the histogram of the color channels separately
    channel1_hist = np.histogram(img[:,:,0], bins=nbins, range=bins_range)
    channel2_hist = np.histogram(img[:,:,1], bins=nbins, range=bins_range)
    channel3_hist = np.histogram(img[:,:,2], bins=nbins, range=bins_range)
    # Concatenate the histograms into a single feature vector
    hist_features = np.concatenate((channel1_hist[0], channel2_hist[0], channel3_hist[0]))
    # Return the individual histograms, bin_centers and feature vector
    return hist_features



# # Parameter tunning
# color_space = ‘YCrCb’ # Can be RGB, HSV, LUV, HLS, YUV, YCrCb
# orient = 9 # HOG orientations
# pix_per_cell = (8,8) # HOG pixels per cell
# cell_per_block = (2,2) # HOG cells per block
# hog_channel = 0 # Can be 0, 1, 2, or “ALL”
# spatial_size = (32, 32) # Spatial binning dimensions
# hist_bins = 32 # Number of histogram bins
# spatial_feat = True # Spatial features on or off
# hist_feat = True # Histogram features on or off
# hog_feat = True # HOG features on or off
# y_start_stop = [None, None] # Min and max in y to search in slide_window()

# Split up data into randomized training and test sets
# rand_state = np.random.randint(0, 100)
# X_train, X_test, y_train, y_test = train_test_split(
#  scaled_X, y, test_size=0.2, random_state=rand_state)
# # Use a linear SVC 
# svc = LinearSVC()
# # Train
# svc.fit(X_train, y_train)
# # Accuracy
# svc.score(X_test, y_test)

# Window 1
# window = (320,240)
# cells_per_step = (2,2)
# pix_per_cell=(40,30)
# ystart = 400
# ystop = 700
# Window 2
# window = (240,160)
# cells_per_step = (2,2)
# pix_per_cell=(30,20)
# ystart = 380
# ystop = 620
# Window 3
# window = (160,104)
# cells_per_step = (2,2)
# pix_per_cell=(20,13)
# ystart = 380
# ystop = 536
# Window 4
# window = (80,72)
# cells_per_step = (2,2)
# pix_per_cell=(10,9)
# ystart = 400
# ystop = 490

# heatmap = np.zeros_like(image[:,:,0])
# Add += 1 for all pixels inside each bbox
# Assuming each “box” takes the form ((x1, y1), (x2, y2))
# heatmap[box[0][1]:box[1][1], box[0][0]:box[1][0]] +=plt.imshow(cap)
                

# Zero out pixels below the threshold
# heatmap[heatmap <= threshold] = 0