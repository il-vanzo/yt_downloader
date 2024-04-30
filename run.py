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
            suffix = "_video"
        elif choice == 'a':
            stream = yt.streams.get_audio_only()
            suffix = "_audio"
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue

        # Asegurarse de que la carpeta 'downloads' exista
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        # Formar el nombre del archivo, agregando un sufijo para diferenciar el tipo
        extension = stream.mime_type.split('/')[-1]  # extraer la extensión basada en el tipo MIME
        file_name = f"{stream.title}{suffix}.{extension}"  # asegurar que el punto esté antes de la extensión

        # Reemplazar caracteres no permitidos en nombres de archivo
        file_name = "".join([c for c in file_name if c.isalpha() or c.isdigit() or c in [' ', '.', '_', '-']]).rstrip()

        # Descargar el stream seleccionado
        stream.download(output_path='downloads', filename=file_name)

        print(f"\nDescarga completada: {file_name}")

        respuesta = input("¿Quieres descargar otro video? (s/n): ")
        if respuesta.lower() != 's':
            break

if __name__ == "__main__":
    download_video()

