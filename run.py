from pytube import YouTube
import sys
import os

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    sys.stdout.write(f"\rDescargando... {percentage_of_completion:.2f}% completado")
    sys.stdout.flush()

def download_video():
    while True:
        url = input("\nIngresa la URL del video de YouTube: ")
        yt = YouTube(url, on_progress_callback=on_progress)
        choice = input("¿Quieres descargar video o audio? (v/a): ").lower()

        if choice == 'v':
            stream = yt.streams.get_highest_resolution()
            file_type = 'video'
        elif choice == 'a':
            stream = yt.streams.get_audio_only()
            file_type = 'audio'
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue

        # Definir ruta de descarga dentro de la carpeta 'downloads'
        download_path = os.path.join('downloads', f"{stream.title}.{file_type}")

        # Descargar el stream seleccionado
        stream.download(output_path='downloads', filename=download_path)

        print(f"\nDescarga completada: {download_path}")

        respuesta = input("¿Quieres descargar otro video? (s/n): ")
        if respuesta.lower() != 's':
            break

if __name__ == "__main__":
    download_video()

