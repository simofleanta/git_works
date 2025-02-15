from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = """
I am sachsen from my grandparents' side, they were deported to Russia 40 years ago. 
I am grateful that I am today able to take further the legacy of sachsens and be proud of my very origins. 
I am not sachsen but I prefer living my life next to my German friends because they always do great things and they celebrate a lot. 
My mom is German and my dad is Hungarian. They lived in Nurnberg but later in life moved to Romania and I was eventually born here and led my childhood in this very village. 
I am grateful that not far from my village I got to a German school and grew my social life and further career near where I studied. 
Living in a German community yet in Romania is simply exciting.
"""

# Generate the word cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',  # You can change the colormap to customize colors
    max_words=100,  # Limit the number of words displayed
    stopwords=set(["I", "am", "my", "they", "is", "and", "to", "in", "a"])  # Add common words to be excluded
).generate(text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Sample Text')
plt.show()

