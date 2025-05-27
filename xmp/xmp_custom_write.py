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

image_path = "image.jpg"

# Example usage - write
text_content = "This is my custom text metadata written to image-warehouse namespace ..." * 1000
write_xmp_metadata(image_path, text_content)
