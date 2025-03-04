import os
# TODO: improve this logic later on 
def save_uploaded_file(uploaded_file, upload_dir='uploads'):
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, uploaded_file.filename)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.read())
    return file_path
