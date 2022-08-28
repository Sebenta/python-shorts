from os.path import join, dirname
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image


def main():

    path = dirname(__file__)

    fonte = join(path, "FontSytle", "NotoSerif-Regular.ttf")

    with open(join(path, "TextFiles", "Computer_Programming_Words.txt"), encoding="utf-8") as f:
        txt = f.read().split()

    words = ''
    for i in np.random.randint(0, len(txt), 10000):
        words += txt[i] + ' '

    mask = np.array(Image.open(join(path, "Imagens", "Cartoon_cloud_c2.png")))

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    word_cloud = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA", font_path=fonte,
                           mask=mask, width=1920, height=1080, max_words=1000,
                           stopwords=stopwords, random_state=42)

    word_cloud.generate(words)
    image_colors = ImageColorGenerator(mask)
    word_cloud.recolor(color_func=image_colors)

    word_cloud.to_file('Imagens/test.png')


if __name__ == "__main__":
    main()
