
import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
import time

destino = "pasta_destino"
opcao_download = ['Vídeo', 'Áudio']


st.title("Baixar Vídeo / Áudio do YouTube")
st.divider()

link_video = st.text_input("Informe o link do vídeo ")
st.divider()

left, middle, right = st.columns(3)

if left.button("DownLoad Vídeo", use_container_width=True):
     st.write('Baixando Vídeo...')
     
     yt = YouTube(link_video)
     ys = yt.streams.get_highest_resolution()
     ys.download(output_path=destino)    
     
     with st.spinner("Wait for it...", show_time=True):
          time.sleep(5)

          
     st.write('Vídeo baixado com sucesso...')
    
if middle.button("DownLoad Áudio", use_container_width=True):
    st.write('Baixando Áudio...')
    
    yt = YouTube(link_video)
    arquivo = yt.title + '.mp3'

    ys = yt.streams.get_audio_only()
    ys.download(output_path=destino, filename=arquivo)
    
    with st.spinner("Wait for it...", show_time=True):
          time.sleep(5)
