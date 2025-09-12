def generateAndSaveSpeech(inputText, saveFolderPath, fileName, voice="shimmer"):
    """
    Generate speech from text using local TTS and save as MP3.
    Deletes MP3s older than 60 seconds before saving.
    Streams audio directly to disk to prevent memory issues.
    """
    import system.util
    import json
    from java.net import URL
    from java.io import File, FileOutputStream, BufferedOutputStream, OutputStreamWriter, BufferedWriter
    from jarray import zeros

    logger = system.util.getLogger("exchange/iggy/audio/generateAndSaveSpeech")

    try:
        # Ensure file has .mp3 extension
        if not fileName.lower().endswith(".mp3"):
            fileName += ".mp3"

        # Ensure save directory exists
        dir = File(saveFolderPath)
        if not dir.exists():
            dir.mkdirs()
        else:
            # Delete only MP3s older than 60 seconds
            now = system.date.now().getTime()
            cutoff = now - 60000  # 60 seconds in ms
            for f in dir.listFiles():
                if f.isFile() and f.getName().lower().endswith(".mp3"):
                    if f.lastModified() < cutoff:
                        f.delete()

        fullPath = File(saveFolderPath, fileName).getAbsolutePath()
        inputText = exchange.iggy.tts.sanitizeResponse(inputText)

        payload_dict = {
            "model": "tts-1",
            "voice": voice,
            "input": inputText
        }
        payload = json.dumps(payload_dict)

        # Open HTTP connection
        url = URL("http://openedai-speech:8000/v1/audio/speech")
        conn = url.openConnection()
        conn.setDoOutput(True)
        conn.setRequestMethod("POST")
        conn.setRequestProperty("Content-Type", "application/json")
        conn.setRequestProperty("Accept", "audio/mpeg")
        conn.setConnectTimeout(15000)
        conn.setReadTimeout(60000)

        # Send JSON payload
        writer = BufferedWriter(OutputStreamWriter(conn.getOutputStream(), "UTF-8"))
        writer.write(payload)
        writer.flush()
        writer.close()

        # Stream response directly to file
        inputStream = conn.getInputStream()
        bos = BufferedOutputStream(FileOutputStream(fullPath))
        buffer = zeros(8192, 'b')
        while True:
            count = inputStream.read(buffer)
            if count == -1:
                break
            bos.write(buffer, 0, count)

        bos.close()
        inputStream.close()

        return {"success": True, "filePath": fullPath}

    except Exception as e:
        logger.error("TTS streaming error: " + str(e))
        return {"success": False, "error": str(e)}
def sanitizeResponse(text):
    import re
    sanitized_text = text.replace("*", "")
    sanitized_text = re.sub("ICC", "I see sea", sanitized_text, flags=re.IGNORECASE)
    return sanitized_text