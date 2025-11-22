import shutil
import os
import kagglehub

# Clear the cache directory
cache_path = r"C:\Users\guyil\.cache\kagglehub\datasets\olistbr\brazilian-ecommerce"
if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
    print("Cache cleared!")

# Download fresh copy
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print("Path to dataset files:", path)

# List downloaded filesa
files = os.listdir(path)
print(f"Downloaded {len(files)} files: {files}")

# Destination path
destination_path = r"C:\Users\guyil\Desktop\data_analysis\data_csv"

# Create destination directory if it doesn't exist
os.makedirs(destination_path, exist_ok=True)

# Move all files (cut and paste)
for file in os.listdir(path):
    source_file = os.path.join(path, file)
    destination_file = os.path.join(destination_path, file)

    if os.path.isfile(source_file):
        shutil.move(source_file, destination_file)
        print(f"Moved: {file}")

print("All files moved successfully!")
