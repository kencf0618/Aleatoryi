import wave
import pyaudio
import random
import os

def play_random_segments(wav_file):
    try:
        # Open the WAV file
        with wave.open(wav_file, 'rb') as wf:
            # Get audio parameters
            sample_width = wf.getsampwidth()
            frame_rate = wf.getframerate()
            num_channels = wf.getnchannels()
            total_frames = wf.getnframes()
            
            # Calculate segment length in frames (1.5 seconds)
            segment_frames = int(frame_rate * 1.5)
            
            # Verify file is long enough
            if total_frames < segment_frames:
                print(f"Error: File is too short ({total_frames/frame_rate:.2f}s). Need at least 1.5s of audio.")
                return
            
            # Initialize PyAudio
            p = pyaudio.PyAudio()
            stream = p.open(
                format=p.get_format_from_width(sample_width),
                channels=num_channels,
                rate=frame_rate,
                output=True
            )
            
            try:
                print("Playing random segments... Press Ctrl+C to stop.")
                while True:
                    # Calculate random start frame
                    max_start = total_frames - segment_frames
                    start_frame = random.randint(0, max_start)
                    
                    # Read audio segment
                    wf.setpos(start_frame)
                    audio_data = wf.readframes(segment_frames)
                    
                    # Play segment
                    stream.write(audio_data)
                    
            except KeyboardInterrupt:
                print("\nPlayback stopped")
            finally:
                # Cleanup
                stream.stop_stream()
                stream.close()
                p.terminate()
    except wave.Error:
        print("Error: Not a valid WAV file or unsupported WAV format.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def get_wav_path():
    while True:
        file_path = input("Please enter the path to a WAV file: ").strip()
        
        if not file_path:
            print("No file path entered. Please try again.")
            continue
            
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        return file_path

if __name__ == "__main__":
    print("WAV File Random Segment Player")
    print("-------------------------------")
    
    wav_file = get_wav_path()
    play_random_segments(wav_file)
