from PIL import Image
from xmp import XMPMeta
from xmp.namespaces import register_namespace

# Register a custom namespace for your plaintext data (optional but good practice)
namespace_uri = "http://yourdomain.com/plaintext/"  # Replace with your own URI
namespace_prefix = "plaintext"
register_namespace(namespace_uri, namespace_prefix)

image_path = "image.jpg" # /Users/steve/Desktop/image.jpg
plaintext_data = "This is a very long string of plaintext data..." * 1000  # Simulate 100KB

try:
    img = Image.open(image_path)
    xmp_data = XMPMeta()

    # Store the plaintext data in a custom XMP property within your namespace
    xmp_data.set_property(namespace_uri, "largeTextData", plaintext_data)

    # Embed the XMP data into the image
    img.save(image_path, xmp=xmp_data)  # PIL >= 9.2 supports xmp in save

    print(f"Plaintext data successfully written to XMP metadata in {image_path}")

except Exception as e:
    print(f"Error writing XMP metadata: {e}")