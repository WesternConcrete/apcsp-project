alphabet = 'abcdefghijklmnopqrstuvwxyz'
print("Input the encoded message (using the Ceasar Cipher): ")
message = str(input()).lower()
most_common_words =  ['the', 'of', 'give', 'new', 'and', 'a', 'me', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'i', 'at', 'be', 'this', 'have', 'from', 'or', 'one', 'had', 'word', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look', 'two', 'more', 'write', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my', 'than', 'first', 'water', 'been', 'call', 'who', 'oil', 'its', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part', 'again', 'by']
tolerance = 3

def find_conf():
    avg_word_len = 0
    word_count = 0
    confidence = ""
    words_in_message = message.split()
    for word in words_in_message:
        word.strip()
        word_count += 1
        avg_word_len += len(word)
    avg_word_len /= float(word_count)
    if word_count > 3 and avg_word_len >= 3 and avg_word_len < 5:
        confidence = "High"
    elif word_count > 2 and avg_word_len > 2.5:
        confidence = "Medium"
    else:
        confidence = "Low"
    return confidence

def decode(sentence,shift):
    listt = []
    for letter in sentence:
        if alphabet.find(letter) >= 0:
            index = alphabet.find(letter)
            listt.append(alphabet[(index+shift)%26])
        else: 
            listt.append(letter)
    return ''.join(listt)

def matcher():
    for i in range(26):
        message_at_index = decode(message,i)
        list_of_messag = message_at_index.split()
        tab_lom = []
        for each_messag in list_of_messag:
            tab_lom.append(each_messag.strip('.').strip('?').strip('!').strip())
        for tab in tab_lom:
            if len(tab) >= 2:
                for word in most_common_words:
                    if word == tab:
                       return matcher2()
                    else:
                        continue
def matcher2():
    for i in range(26):
        message_at_index = decode(message,i)
        list_of_messag = message_at_index.split()
        tab_lom = []
        for each_messag in list_of_messag:
            tab_lom.append(each_messag.strip('.').strip('?').strip('!').strip())
        tab_lom.sort()
        for tab in tab_lom:
            if len(tab) >= tolerance:
                for word in most_common_words:
                    if word == tab:
                       return message_at_index
                    else:
                        continue


print("\n ---------- \n \nThe decoded message is: ")
if matcher() != None:
    print(matcher())
    print("\nConfidence: " + find_conf())
else:
    tolerance -= 1
    if matcher() != None:
        print(matcher())
        print("\nConfidence: Very Low")
    else:
        print("Unable to be determined")
        
while True:
    pass