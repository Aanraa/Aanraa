#from gpiozero import led
from vosk import Model, KaldiRecognizer, SetLogLevel # Vosk 
import sys # CLI-аас arg татахад зориулагдсан
import os # os үйл ажиллагаа
import wave # wav ugugdluudiig udirdahad zoriulagdsan
import pyaudio # Audio orolt garalttai ajilladag san
import webrtcvad #

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels=1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()
vad = webrtcvad.Vad(3)
sample_rate = 16000
frame_duration = 10

frame = b'\x00\x00' * int(sample_rate * frame_duration / 1000)


SetLogLevel(0) # debug level 0 for output on terminal

#led = LED(17)
kherem = "хэрэм";
print("хэрэм байна")

#Modeliinho zamiig zaaj ogoh heregtei ba 
if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

# Audiogoo wav esehiig shalgaj baina
#wf = wave.open(sys.argv[1], "rb")
#if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
rec = KaldiRecognizer(model, 16000)
rec.SetWords(True)

while True:
    data = stream.read(4096, exception_on_overflow = False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
                if  rec.Result() == "гэрэл ас":
                    print("Pi: " + "аслаа" )
                    #led.on();

                elif rec.Result() == "гэрэл унтар":
                    print("Pi: " + "унтарлаа" )
                    #led.off();