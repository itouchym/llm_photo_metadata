from exif import Image
import json

def write_large_text(image_path, text_data):
    try:
        # Read the image
        with open(image_path, 'rb') as img_file:
            img = Image(img_file)
        
        # Convert text to JSON string (helps with encoding)
        img.user_comment = json.dumps(text_data)
        
        # Write back to file
        with open(image_path, 'wb') as updated_file:
            updated_file.write(img.get_file())
            
        print("Text data written successfully")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def read_large_text(image_path):
    try:
        # Read the image
        with open(image_path, 'rb') as img_file:
            img = Image(img_file)
        
        if hasattr(img, 'user_comment'):
            # Parse JSON string back to text
            return json.loads(img.user_comment)
        return None
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    image_path = "/Users/steve/Desktop/image.jpg"

    # Example large text data
    large_text = "Your large text content here..." * 1000

    # Write the data
    write_large_text(image_path, large_text)

    # Read back the data
    retrieved_text = read_large_text(image_path)
    if retrieved_text:
        print(f"Retrieved text length: {len(retrieved_text)}")
        print("First 100 characters:", retrieved_text[:100])
    else:
        print("No text retrieved")