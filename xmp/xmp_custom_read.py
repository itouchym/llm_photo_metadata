import libxmp
from libxmp import XMPFiles, consts

def write_xmp_metadata(image_path, text_content):
    xmpfile = XMPFiles(file_path=image_path, open_forupdate=True)
    xmp = xmpfile.get_xmp()
    if xmp is None:
        xmp = libxmp.XMPMeta()
    custom_ns = "http://app.example.com/image-warehouse/"
    custom_ns_prefix = "image-warehouse"
    libxmp.XMPMeta.register_namespace(custom_ns, custom_ns_prefix)
    xmp.set_property(custom_ns, 'text', text_content)
    if xmpfile.can_put_xmp(xmp):
        xmpfile.put_xmp(xmp)
    xmpfile.close_file()

def read_xmp_metadata(image_path):
    custom_ns = "http://app.example.com/image-warehouse/"
    custom_ns_prefix = "image-warehouse"
    libxmp.XMPMeta.register_namespace(custom_ns, custom_ns_prefix)
    xmpfile = XMPFiles(file_path=image_path)
    xmp = xmpfile.get_xmp()
    if xmp is not None:
        try:
            if xmp.does_property_exist(custom_ns, 'text'):
                text_content = xmp.get_property(custom_ns, 'text')
                print(f"Found text content: {text_content}")
            else:
                print("No text content found in custom namespace")
        except Exception as e:
            print(f"Error reading metadata: {e}")
    else:
        print("No XMP metadata found in file")
    xmpfile.close_file()

image_path = "image.jpg"

# Example usage - write
#text_content = "This is my custom text metadata written to image-warehouse namespace"
#write_xmp_metadata(image_path, text_content)

# Example usage - read
read_xmp_metadata(image_path)

