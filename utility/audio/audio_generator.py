import edge_tts

async def generate_audio(text,outputFilename):
    # communicate = edge_tts.Communicate(text,"en-AU-WilliamNeural")
    communicate = edge_tts.Communicate(text,"hi-IN-SwaraNeural")
    await communicate.save(outputFilename)





