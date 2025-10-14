#import brain atlas (using nilearns atlas)
import nilearn

#importing libraries (collecting 3 packages - nilearn, matplotlib,numpy)
from nilearn import plotting, datasets # draw brain images, sample brain/atlas
import matplotlib.pyplot as plt #show and save plots
import numpy as np #for manipulating numeric data (activity values for later)




#[
#load a brain TEMPLATE from nilearn
anat = datasets.load_mni152_template() #loads MRI template (MNI152) - blank template
print(type(anat)) #shows its a 3D NumPy
print(anat.shape) #prints(197, 233, 189) - each number represents 3D tissue intesity

#plot brain TEMPLATE
display = plotting.plot_anat(anat, title = 'Brain Visualization 1') #plot_anat draws the 3D brain into a 2D brain, title lables figure
#shows outline template of brain (no color)
#]



#[
#load brain atlas - Schaefer atlas (most recent 2018) 
atlas = datasets.fetch_atlas_schaefer_2018(n_rois=700, resolution_mm=1) #atlas contains brain regions
template = datasets.load_mni152_template() #template gives backround to plot image

#plot atlas (Overlay onto TEMPLATE)
display=plotting.plot_roi(atlas.maps, bg_img=template, title='Schaefer Brain Atlas', cmap = 'spring')#ROI is region of intrest. focuses computation/data on specific part. spring is color of map!
plt.show()#shows image in a new window (brain plot) in diff colors (choropleth)

print(nilearn.datasets.MNI152_FILE_PATH)

#]

