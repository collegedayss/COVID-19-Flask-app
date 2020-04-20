# COVID-19-Flask-app
This app utilizes a deep convolutional neural network to detect COVID-19. The model was pretrained from chest radiography images that are open source and available to the general public, and was built by the [COVID-Net Open Source Initiative](https://github.com/lindawangg/COVID-Net). 

## Getting Started with COVID-19 model
- Download all the files from the [COVIDNet-CXR-Large](https://drive.google.com/drive/folders/1eNidqMyz3isLjGYN1evzQu--A-JVkzbk) pretrained model.
- You may end up with multiple zipped folders after downloading evertything.
- Unizip the folders and delete the original zipfiles.
- Make sure to move the files into the models folder.
- Your models folder should look like this:
```
      ├── models
      │   └── COVIDNet-CXR-Large
      │       ├── checkpoint
      │       ├── model-8485.data-00000-of-00001
      │       ├── model-8485.index
      │       ├── model.meta
      │       └── savedModel
      │           ├── saved_model.pb
      │           └── variables
      │               ├── variables.data-00000-of-00001
      │               └── variables.index
```
