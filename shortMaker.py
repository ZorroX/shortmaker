from moviepy.video.io.VideoFileClip import VideoFileClip
import os

# Lista de tiempos y títulos en formato ["HH:MM:SS", "titulo"]
clips = [
    ("00:03:13", "Inicio en la música japonesa y el impacto de los medios"),
    ("00:12:03", "Primeros pasos en la música y el impacto de Sakura"),
    ("00:26:06", "Lecciones de la voz y carreras musicales"),
    ("00:38:28", "Concursos y nervios en el mundo del espectáculo"),
    ("00:43:03", "Viaje a Japón, aprendizajes y equipo"),
    ("01:13:22", "Uso de redes sociales y construcción de seguidores"),
    ("01:18:24", "Equilibrio entre aprendizaje y descanso en la carrera artística"),
    ("01:22:25", "Logros e impacto de ser una estudiante internacional en Japón"),
    ("01:23:54", "Participación en doramas y el fandom japonés"),
    ("01:25:36", "El lado oscuro del fandom y experiencias personales"),
]

# Convertir los tiempos a segundos
clips_in_seconds = []
for time, title in clips:
    h, m, s = map(int, time.split(':'))
    total_seconds = h * 3600 + m * 60 + s
    clips_in_seconds.append((total_seconds, title))

# Cargar el video original
input_video_path = 'videos/input/NataliaD.mp4'
output_folder_path = 'videos/output/'

# Verificar si las rutas existen
if not os.path.isfile(input_video_path):
    raise FileNotFoundError(f"El archivo {input_video_path} no se encuentra.")
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

video = VideoFileClip(input_video_path)

# Duración del video corto en segundos
short_duration = 60

# Generar los videos cortos
for start_time, title in clips_in_seconds:
    end_time = start_time + short_duration
    subclip = video.subclip(start_time, end_time)
    output_video_path = f'{output_folder_path}{title}.mp4'
    subclip.write_videofile(output_video_path, codec='libx264')

# Liberar los recursos
video.close()
