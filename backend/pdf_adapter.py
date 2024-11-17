import fitz

def pdf_reader(path_to_pdf):
    reader = fitz.open(path_to_pdf)
    text = ""
    for page in reader:
        text += page.get_text() 
    return text


def extract_first_image_from_pdf(pdf_path, output_image_path):
   doc = fitz.open(pdf_path)
   for page in doc:
      images = page.get_images(full=True)
      if images:
         xref = images[0][0]
         base_image = doc.extract_image(xref)
         image_bytes = base_image["image"]
         image_ext = 'png'

         with open(f"{output_image_path}.{image_ext}", "wb") as img_file:
            img_file.write(image_bytes)
         return f"{output_image_path}.{image_ext}"
   return ''