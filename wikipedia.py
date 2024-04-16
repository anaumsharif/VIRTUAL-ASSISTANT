import wikipedia

while True:
        input = raw_input("Q: ")
        wikipedia.set_lang("es")
        print wikipedia.summary(input, sentences=2)
        
        
# import wikipedia

# while True:
#         input = raw_input("Q: ")
#         print wikipedia.summary(input)