
from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/lipsync", methods=["POST"])
def lipsync():
    video = request.files.get("video")
    audio = request.files.get("audio")

    if not video or not audio:
        return jsonify({"error": "Envie os arquivos de vídeo e áudio."}), 400

    video_path = "input.mp4"
    audio_path = "input.wav"

    video.save(video_path)
    audio.save(audio_path)

    command = f"python3 inference.py --checkpoint_path Wav2Lip.pth --face {video_path} --audio {audio_path}"
    subprocess.run(command, shell=True)

    return jsonify({
        "result": "Vídeo gerado com sucesso",
        "output": "/static/result_voice.mp4"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
