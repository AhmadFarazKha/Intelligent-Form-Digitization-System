
import cv2
import numpy as np
from google.colab import files
import pytesseract

# Install necessary libraries (if not already installed)
!apt-get install tesseract-ocr
!pip install pytesseract

# Function to perform OCR on the image and extract digits
def extract_digits_from_image(image_path):
    try:
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Ensure correct color format for pytesseract
        text = pytesseract.image_to_string(img, config='--psm 6')  # Use page segmentation mode 6 for single-line text
        digits = ''.join(filter(str.isdigit, text))  # Extract only digits from the text
        return digits
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

# Main function
def main():
    uploaded = files.upload()

    for fn in uploaded.keys():
        image_path = fn  # Get the image file path from the uploaded file
        extracted_digits = extract_digits_from_image(image_path)

        if extracted_digits:
            print("Extracted digits from the image:", extracted_digits)

            user_input = input("Enter the digits you want to check: ")

            if user_input in extracted_digits:
                print("The input digits are present in the image.")
            else:
                print("The input digits are not present in the image.")
        else:
            print("Failed to extract digits from the image.")

if __name__ == "__main__":
    main()
