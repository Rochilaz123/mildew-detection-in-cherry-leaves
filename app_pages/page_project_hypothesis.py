import streamlit as st
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import random
import itertools

def page_project_hypothesis_body():
    st.write("---")
    st.write("## Project Hypothesis and Validation")
    st.write("---")

    st.warning(
        f"* We suspect that leaves infected with powdery mildew have clear signs, "
        f"predominantly white patches on the surface, that can differentiate them " 
        f"from healthy leaves.\n\n"
    )

    st.success(
        f"* Average Image shows that the surface of the average healthy leaf is clear, "
        f"whilst the surface of the average infected leaf has white marks.\n\n"
        f"* The Variability Image reveals white lines accross the centre of the average "
        f"infected leaf, whilst the centre of the average healthy leaf is clear."        
    )

    version = 'v1'
    avg_infected = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
    avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

    st.image(avg_infected, caption='Infected Leaf - Average and Variability')
    st.image(avg_uninfected, caption='Healthy Leaf - Average and Variability')

    st.success(
        f"* An Image Montage shows that typically an infected leaf has white patches "
        f"on the surface. \n"
        )

    my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
    labels = os.listdir(my_data_dir+ '/validation')
    image_montage(dir_path= my_data_dir + '/validation',
                  label_to_display='healthy',
                  nrows=2, ncols=3, figsize=(10,8))

    my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
    labels = os.listdir(my_data_dir+ '/validation')
    image_montage(dir_path= my_data_dir + '/validation',
                  label_to_display='powdery_mildew',
                  nrows=2, ncols=3, figsize=(10,8))


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    img_idx = random.sample(images_list, nrows * ncols)


    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)
    # plt.show()
