import re

def sentiment_analyzer(text):
    # Read the sentiment dictionary from a file
    sentiment_dict = {}
    with open(r"C:\Users\inesz\OneDrive\Desktop\memoire\home\arabic_sentiment_dict.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()   # Remove spaces at the beginning or at the end of the line
            
            if not line:
                continue
                
            # Split the line into word and score using comma as separator
            parts = line.split(",")
            if len(parts) != 2:
                # Skip lines that do not contain two values separated by a comma
                continue
            
            # Convert the score to an integer and add the word and score to the dictionary
            word = parts[1]
            score = int(parts[0])
            sentiment_dict[word] = score
            
    # Define a list of words whose subsequent words should be negated if they appear
    negate_words = ['لا', 'لم', 'ما', 'إن', 'ليس', 'غير', 'لات', 'لما', 'لن', 'ليست' , 'مش' , 'ليست', 'ماهوش' ,
                    'مهوش' , 'ماهيش' , 'مهيش' , 'ماشي', 'ما', 'مانيش', 'ماناش', 'ماهمش']
    
    # Split the text into words
    words = re.findall(r'\S+', text)
    
    # Initialize the sentiment score
    sentiment_score = 0
    negate = False  # Flag to indicate if the subsequent word should be negated
    
    # Loop through the words
    for word in words:
        # Check if the word should be negated
        if word in negate_words:
            negate = True
            continue
        
        # Get the score for the word
        score = sentiment_dict.get(word, 0)
        
        # Negate the score if the previous word was a negate word
        if negate:
            score *= -1
            negate = False
        
        # Add the score to the sentiment score
        sentiment_score += score
    
    # Return the sentiment score
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'




