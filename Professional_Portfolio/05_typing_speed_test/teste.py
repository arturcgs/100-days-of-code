
def break_line_text(text):
    words = text.split()
    chars = 0
    text_with_line_breaks = ""

    for word in words:
        chars += len(word)
        if chars > 30:
            text_with_line_breaks += "\n"
            chars = 0

        text_with_line_breaks += word
        text_with_line_breaks += " "

    return text_with_line_breaks

blop = "In a bustling city, diverse lives intertwine. Dreams take flight, and challenges emerge. Through connections and resilience, each person navigates a unique journey, adding their chapter to the vibrant urban tapestry."

a = break_line_text(blop)

print(a)