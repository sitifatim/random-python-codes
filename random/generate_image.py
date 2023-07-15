import os 
from bing_image_downloader import downloader

def download_images(query,limit,output_dir):
    downloader.download(query, limit=limit, output_dir=output_dir)

def main():
    query = "sad expression human"
    limit = 20
    output_dir = 'random/dataset'
    #create new dir if it doesnt exist yet
    os.makedirs(output_dir, exist_ok=True)

    #downloa the images
    download_images(query, limit, output_dir)

if __name__ == "__main__":
    main()