import colorgram

# extracting colors
colors = colorgram.extract('hirst_painting.jpg', 34)

# creating colors_list
colors_list = []
for color in colors:
    if color.proportion < 0.5:  # don't get white
        colors_list.append(tuple(color.rgb))

# removing manually curated bad colors
bad_colors = [(247, 241, 244), (240, 246, 241), (236, 238, 244)]

colors_list = [color for color in colors_list if color not in bad_colors]
