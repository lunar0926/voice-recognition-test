import speech_recognition as sr 
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
print(r.recognize_google(audio,language='ko-KR'))
answer = r.recognize_google(audio,language='ko-KR')
if (answer == '안녕하세요'):
    print('반갑습니다.')
else: 
    print('무슨 말인지 이해하지 못했어요.')