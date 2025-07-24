import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader, PdfWriter

# Load environment variables from .env.local
load_dotenv('.env.local')

input_folder = os.getenv('INPUT_FOLDER')
output_folder = os.getenv('OUTPUT_FOLDER')
pdf_password = os.getenv('PDF_PASSWORD')

def unlock_pdf_batch(input_folder, output_folder, password):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with open(input_path, 'rb') as file:
                    reader = PdfReader(file)
                    
                    if reader.is_encrypted:
                        if reader.decrypt(password) == 0:
                            print(f"❌ Incorrect password for: {filename}")
                            continue
                    
                    writer = PdfWriter()
                    for page in reader.pages:
                        writer.add_page(page)

                    with open(output_path, 'wb') as output_file:
                        writer.write(output_file)

                    print(f"✅ Unlocked: {filename}")

            except Exception as e:
                print(f"⚠️ Error with file {filename}: {e}")

# Run the batch unlocker
unlock_pdf_batch(input_folder, output_folder, pdf_password)
