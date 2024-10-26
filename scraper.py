import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser   # To open the link in the browser

st.set_page_config(
      page_title = 'Image Search',
      page_icon='📷',
      layout='wide',
)

st.markdown("<h1 style='text-align: center'>Image Search</h1>", unsafe_allow_html=True)

with st.form(key='Search'):
      keyword=st.text_input('Enter your keyword')
      search = st.form_submit_button('Search')
placeholder = st.empty()      # placeholder helps to display different images in the same row
if keyword:
      with st.spinner('Searching for images...'):
            try:
                  page=requests.get(f'https://unsplash.com/s/photos/{keyword}')
                  soup = BeautifulSoup(page.content, 'lxml')
                  rows = soup.find_all('div', class_='bugb2')
                  col1, col2 = placeholder.columns(2)
                  for index,row in enumerate(rows):
                        figures = row.find_all('figure')
                        for i in range(2):
                              img = figures[i].find('img', class_='I7OuT DVW3V L1BOa')
                              list=img['srcset'].split('?')
                              anchor = figures[i].find('a', class_='zNNw1')
                              print(anchor['href'])
                              if i==0:
                                    with col1:
                                          st.image(list[0])
                                          btn=st.button('Download', key=str(index)+str(i))  # Unique key built
                                          if btn:
                                                webbrowser.open_new_tab('https://unsplash.com'+anchor['href'])
                              else:
                                    with col2:
                                          st.image(list[0])
                                          btn = st.button('Download', key=str(index)+str(i))
                                          if btn:
                                                webbrowser.open_new_tab('https://unsplash.com'+anchor['href'])
            except requests.exceptions.RequestException as e:
                  st.error(f"Error: {e}")
                  
