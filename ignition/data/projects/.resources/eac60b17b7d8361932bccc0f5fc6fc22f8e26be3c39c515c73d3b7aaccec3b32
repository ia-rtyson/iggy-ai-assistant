# Project Script: tts
# Final version: Uses Java for file deletion for maximum compatibility.

def generateAndSaveSpeech(inputText, saveFolderPath, fileName, voice="shimmer"):
    """
    Deletes all files in a folder, then generates speech and saves it as an MP3 file.
    Uses core Java methods for networking and file handling to ensure compatibility.

    Args:
        inputText (str): The text to convert to speech.
        saveFolderPath (str): The absolute path to the folder on the GATEWAY.
        fileName (str): The desired name for the output file.
        voice (str): The voice to use. Defaults to "alloy".

    Returns:
        dict: A dictionary indicating success or failure.
    """
    import system.file
    import system.util
    from java.net import URL, HttpURLConnection
    from java.io import File, DataOutputStream
    from org.apache.commons.io import IOUtils

    conn = None
    try:
        # --- CORRECTED SECTION: Delete existing files using Java's File object ---
        dir_to_clear = File(saveFolderPath)
        if dir_to_clear.exists() and dir_to_clear.isDirectory():
            # Loop through the array of File objects and delete each one
            for f in dir_to_clear.listFiles():
                if f.isFile(): # Make sure we only delete files, not subdirectories
                    f.delete()
        # --- END CORRECTED SECTION ---

        # The URL for the speech service
        url = URL("http://openedai-speech:8000/v1/audio/speech")

        # Construct the JSON payload
        payload = {
            "model": "tts-1",
            "voice": voice,
            "input": inputText
        }
        jsonPayloadBytes = system.util.jsonEncode(payload).encode('utf-8')

        # Open and configure the Java HTTP connection
        conn = url.openConnection()
        #... (The rest of the script is unchanged) ...
        conn.setDoOutput(True)
        conn.setRequestMethod("POST")
        conn.setRequestProperty("Content-Type", "application/json")
        conn.setRequestProperty("Content-Length", str(len(jsonPayloadBytes)))

        # Send the POST data
        wr = DataOutputStream(conn.getOutputStream())
        wr.write(jsonPayloadBytes)
        wr.flush()
        wr.close()

        # Check the response
        responseCode = conn.getResponseCode()

        if responseCode == HttpURLConnection.HTTP_OK: # Status 200
            inputStream = conn.getInputStream()
            audioBytes = IOUtils.toByteArray(inputStream)
            inputStream.close()

            # Create directory and save the file
            dir = File(saveFolderPath)
            if not dir.exists():
                dir.mkdirs()

            if not fileName.lower().endswith('.mp3'):
                fileName += ".mp3"

            fullPath = File(saveFolderPath, fileName).getAbsolutePath()
            system.file.writeFile(fullPath, audioBytes)

            return {'success': True, 'filePath': fullPath}
        else:
            errorStream = conn.getErrorStream()
            errorMessage = IOUtils.toString(errorStream)
            errorStream.close()
            return {'success': False, 'error': "HTTP Error %d: %s" % (responseCode, errorMessage)}

    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        if conn is not None:
            conn.disconnect()