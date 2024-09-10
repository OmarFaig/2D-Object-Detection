import os
#import torchvision.transforms as transforms
#from PIL import Image

def save_images(dataset, split_name,output_dir,preprocess=None):
    split_dir = os.path.join(output_dir, split_name)
    os.makedirs(split_dir, exist_ok=True)
    
    for idx, sample in enumerate(dataset):
        image=sample["image"]
        if preprocess is not None:
            image = preprocess(image)
        # Convert back to PIL image for saving
           # image = transforms.ToPILImage()(image)
        image_path = os.path.join(split_dir, f'image_{idx}.png')
        image.save(image_path,"jpeg")