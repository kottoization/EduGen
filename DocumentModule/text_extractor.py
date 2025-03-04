import os
import fitz  # PyMuPDF
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.docx import partition_docx
from unstructured.partition.pptx import partition_pptx
from unstructured.partition.image import partition_image
from unstructured.partition.text import partition_text

def extract_text_and_images(file_path):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

#TODO: add more methods or delete unnecessary logic
    if file_extension == '.pdf':
        return extract_from_pdf(file_path)
    elif file_extension == '.docx':
        return extract_with_unstructured(file_path, partition_docx)
    elif file_extension == '.pptx':
        return extract_with_unstructured(file_path, partition_pptx)
    elif file_extension in ['.jpg', '.jpeg', '.png']:
        return extract_with_unstructured(file_path, partition_image)
    elif file_extension == '.txt':
        return extract_with_unstructured(file_path, partition_text)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

def extract_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    images = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page{page_num + 1}_img{img_index + 1}.{image_ext}"
            images.append((image_filename, image_bytes))

    return text, images

def extract_with_unstructured(file_path, partition_function):
    try:
        elements = partition_function(filename=file_path)
        text = "\n".join([str(el) for el in elements])
        images = []  # 'unstructured' may not handle image extraction
        return text, images
    except Exception as e:
        print(f"[Error] An error occurred while extracting {file_path} using {partition_function.__name__}: {str(e)}")
        return None, None
