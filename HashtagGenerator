def generate_hashtag(text):
    hashtag_text = '#'
    capitalize = True
        
    for letter in text:
        if len(hashtag_text) > 140:
            hashtag_text = ''
            break
        if letter == ' ':
            capitalize = True
        else:
            if capitalize:
                hashtag_text += letter.upper()
                capitalize = False
            else:
                hashtag_text += letter.lower()
    
    if len(hashtag_text)>1:
        return hashtag_text
    return False
        
