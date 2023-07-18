# from django.shortcuts import render
# from gtts import gTTS
# import os
# import pygame

# def index(request):
#     all_person = {
#         "3": {
#             "Parent_name": "น้องโทนี่",
#             "children_name": "สตาร์ค"
#         }
#     }
    
#     # สร้างฟังก์ชันสำหรับเล่นเสียง
#     def speak(text):
#         language = 'th'
        
#         # สร้างอ็อบเจกต์ gTTS
#         tts = gTTS(text, lang=language)
        
#         # บันทึกไฟล์เสียงเป็นชื่อ temp.mp3
#         audio_file = 'temp.mp3'
#         tts.save(audio_file)
        
#         # เล่นไฟล์เสียง
#         pygame.mixer.init()
#         pygame.mixer.music.load(audio_file)
#         pygame.mixer.music.play()
        
#         # รอให้เสียงเล่นจบ
#         while pygame.mixer.music.get_busy():
#             continue
        
#         # ลบไฟล์เสียงหลังจากใช้งานเสร็จสิ้น
#         os.remove(audio_file)
    
#     # เรียกใช้งานฟังก์ชันเล่นเสียง
#     speak(f'ผญ{all_person["3"]["Parent_name"]} มาส่งคุณ{all_person["3"]["children_name"]} ไปแล้ว')
    
#     context = {
#         'all_person': all_person
#     }
#     return render(request, 'index.html', context)
