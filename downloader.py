from yt_dlp import YoutubeDL

def Downloader(video_url, path, mode):

    mp4_opts  = {
        'outtmpl': path + '/%(title)s.%(ext)s',
    }

    mp3_opts = {
        'writethumbnail': True,
        'format': 'bestaudio/best',
        'outtmpl': path + '/%(title)s.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'},
            {'key': 'EmbedThumbnail',},]}

    with YoutubeDL(mp4_opts if mode is "MP4" else mp3_opts) as ydl:
        ydl.download([video_url])
