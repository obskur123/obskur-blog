import base64
from django import template

register = template.Library()

@register.filter(name='binary_to_image')
def encode_binary_data_to_image(binary):
    encoded_bytes = base64.b64encode(binary)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string