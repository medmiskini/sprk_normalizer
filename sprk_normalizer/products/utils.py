import unicodedata

def parse_unicode(text):
    """
    parse Unicode characters.
    """
    if(text):
        # Normalize the text to NFC (Normalization Form Canonical Composition)
        normalized_text = unicodedata.normalize('NFC', text)
        
        # Remove any characters that cannot be encoded in ASCII
        ascii_text = normalized_text.encode('ascii', 'ignore').decode('utf-8')
        
        return ascii_text
    return None