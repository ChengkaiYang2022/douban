from wordcloud import WordCloud, ImageColorGenerator
import jieba
from scipy.misc import imread
import matplotlib.pyplot as plt
wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=back_coloring,
               max_font_size=100, random_state=42, width=1000, height=860, margin=2,)
