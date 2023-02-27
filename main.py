import webbrowser
from pytube import Playlist , YouTube
from rich.prompt import Prompt 
from rich.console import Console
from rich.traceback import install
import os 
import subprocess
console = Console()
install( show_locals=True)
if not os.path.isdir('/download') : os.mkdir('download')

while True:
    console.print("[green]SAMITHATA MP3 DOWNLOAD KARANNA ONILU")
    video_url = Prompt.ask("[blue]Enter Playlist Link here  ")
    yt = Playlist(video_url)
    try:
        yt.playlist_url
        for video in yt.videos:
                console.print(f'[blue] Video : {video.title}')
        console.print('[yellow] Downloading ...')
        for video in yt.videos:
            console.print(f'[green] Downloading [yellow]{video.title} ...')
            video.streams.get_by_itag(251).download('./download')
            # webbrowser.BackgroundBrowser.open(url=video.streams.get_by_itag(251).url)
            # Download("hello" , video.streams.get_by_itag(251).url)
            # subprocess.run([f'C:\Program Files (x86)\Internet Download Manager\IDMan.exe' , '/n' ,'/d' , video.streams.get_by_itag(251).url])
            console.print('[blue]Downloaded !')
    except KeyError:
        console.print("[red bold]this link dosen't providing any playlist !!!")
        yt = YouTube(video_url)
        choice = Prompt.ask(f'[yellow bold]Do you want to download this single mp3?\nFile Name = [magenta]{yt.title}\n[green]Press Y for download press N for new link adress' , choices=["Y" , "N"] , default="N")
        if choice == 'Y':
            console.print(f'[green] Downloading [yellow]{yt.title} ...')
            yt.streams.get_by_itag(251).download('./download')
            console.print('[blue]Downloaded !')
        else:
            continue
    except KeyboardInterrupt:
        console.print('[orange]Closing ....')
        console.print('[green]bye !')
        break
    except Exception:
        continue
        