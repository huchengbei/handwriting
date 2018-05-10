from PIL import Image, ImageDraw, ImageFont
import codecs as cs

# margin: the space between cell and the border of picture,
# padding: the space between cell and the word
# font: the font of word
# lines: the words
# redLine: 1 means draw picture with red cell, 0 means without, default is 0
def gen_font_image(margin, padding, font, lines, redLine = 0):
    col = raw = 0
    size = font.size
    width = 0
    for line in lines:
        line = line.strip()
        width = max(width,len(line))
    height = len(lines)
    image = Image.new('RGB', (margin * 2 + (size + padding * 2) * width, margin * 2 + (size + padding * 2) * height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    if redLine == 1 :
        for raw in range(0,height ):
            for col in range(0,width):
                # draw the overbar 
                start = (margin + col * (size + padding * 2), margin + raw * (size + padding * 2))
                end = (margin + col * (size + padding * 2) + (size + padding * 2),margin + raw * (size + padding * 2))
                draw.line([start, end], fill='#ff0000')
                # draw the middle horizontal line
                start = (margin + col * (size + padding * 2), margin + raw * (size + padding * 2) + (size + padding * 2) / 2)
                end = (margin + col * (size + padding * 2) + (size + padding * 2),margin + raw * (size + padding * 2) + (size + padding * 2) / 2)
                draw.line([start, end], fill='#ff0000')
                # draw the left vertical line
                start = (margin + col * (size + padding * 2), margin + raw * (size + padding * 2))
                end = (margin + col * (size + padding * 2),margin + raw * (size + padding * 2) + (size + padding * 2))
                draw.line([start, end], fill='#ff0000')
                # draw the middle vertical line
                start = (margin + col * (size + padding * 2) + (size + padding * 2) / 2, margin + raw * (size + padding * 2))
                end = (margin + col * (size + padding * 2) + (size + padding * 2) / 2, margin + raw * (size + padding * 2) + (size + padding * 2))
                draw.line([start, end], fill='#ff0000')
                # draw the right slash
                start = (margin + col * (size + padding * 2), margin + raw * (size + padding * 2))
                end = (margin + col * (size + padding * 2) + (size + padding * 2), margin + raw * (size + padding * 2) + (size + padding * 2))
                draw.line([start, end], fill='#ff0000')
                # draw the left slash
                start = (margin + col * (size + padding * 2), margin + raw * (size + padding * 2) + (size + padding * 2))
                end = (margin + col * (size + padding * 2) + (size + padding * 2),margin + raw * (size + padding * 2))
                draw.line([start, end], fill='#ff0000')
            # draw the right vertical line
            start = (margin + (col + 1) * (size + padding * 2), margin + raw * (size + padding * 2))
            end = (margin + (col + 1) * (size + padding * 2), margin + raw * (size + padding * 2) + (size + padding * 2))
            draw.line([start, end], fill='#ff0000')
        # draw the bottom horizontal line
        start = (margin + 0 * (size + padding * 2), margin + (raw+1) * (size + padding * 2))
        end = (margin + col * (size + padding * 2) + (size + padding * 2), margin + (raw+1) * (size + padding * 2))
        draw.line([start, end], fill='#ff0000')
    
    # draw the words
    col = raw = 0
    for line in lines:
        line = line.strip()
        for char in line:
            x = margin + col * (size + padding * 2) + padding
            y = margin + raw * (size + padding * 2) + padding
            draw.text((x, y), char, font=font, fill='#000000')
            col = col + 1
        raw = raw + 1
        col = 0
    return image


if __name__ == '__main__':
    size = 96
    font = ImageFont.truetype('田英章钢笔行书简.ttf', size)
    hansfile = cs.open('words.txt', 'r', 'utf-8')
    hans = hansfile.readlines()
    hansfile.close()

    image = gen_font_image(10,6,font,hans,0)
    image.save(str('words'+'.png'))
    image = gen_font_image(10,6,font,hans,1)
    image.save(str('words_with_line'+'.png'))