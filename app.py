from flask import Flask, render_template, url_for, request
from pytube import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/work')
def work():
    return render_template('work.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/pytube', methods=['GET', 'POST'])
def pytube():
    if request.method == 'POST':

        # pytube_url = # get it from web request
        # yt = YouTube(pytube_url)
        # title = yt.title
        # streams = yt.streams.get_by_itag()
        # pytube_music = yt.streams.get_audio_only()
        # pytube_video_hq = yt.streams.get_highest_resolution()
        # pytube_music.download()
        # pytube_video_hq.download()
        return render_template('pytube.html')


    if request.method == 'GET':
        return render_template('pytube.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run()
