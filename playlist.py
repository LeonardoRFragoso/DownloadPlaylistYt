from pytube import Playlist

url = "https://www.youtube.com/watch?v=kCMaqla6Grs&list=PLpdAy0tYrnKx9CtTmgSdzHz9YQ-C5ZNI9"

# Cria um objeto Playlist
playlist = Playlist(url)

# Itera sobre os vídeos da playlist e baixa cada um
for video in playlist.videos:
    video_stream = video.streams.get_highest_resolution()
    video_stream.download(output_path=r"C:\Users\leona\OneDrive\Área de Trabalho\testeplaylist")

print("Download concluído.")
