class CONSTS:
    
    class Config:
        """
            BASE_DIR
        """
        BASE_DIR = "assets"
        GLOBAL_VOL_ADJ = -10 # global MP3 volume offset
        DIGITS_VOL_ADJ = -3 # TTS digits volume offset    
    
    class Numbers:
        """
            TTS NUMBERS
        """
        NUM_0 = "0.mp3"
        NUM_1 = "1.mp3"
        NUM_2 = "2.mp3"
        NUM_3 = "3.mp3"
        NUM_4 = "4.mp3"
        NUM_5 = "5.mp3"
        NUM_6 = "6.mp3"
        NUM_7 = "7.mp3"
        NUM_8 = "8.mp3"
        NUM_9 = "9.mp3"
    
    class Segments:
        """
            START/END SEGMENTS OF VOICEMAIL
        """
        SEG_START = "call_forwarded.mp3"
        SEG_END = "please_record.mp3"
        SEG_BEEP = "beep.mp3"