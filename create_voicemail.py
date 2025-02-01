from typing import List, Union
from pydub import AudioSegment
from consts import CONSTS
import os.path

class CreateVoicemail:
    
    """
        CreateVoicemail
        
        (Voicemail Greeting Generator)

        Generates automated greetings using a member's phone
        number rather than name.

        Default voice included uses Microsoft's Neural Speech
        API, and Clara's (Canadian English) voice.
            
        Requirements:
            - pydub
    """
    
    def generate_path(num: Union[CONSTS.Numbers, CONSTS.Segments]) -> str:
        """
            Generates safe paths for audio segments.
            
            Parameters:
                num - either a CONSTS.Numbers or CONSTS.Segments value
            
            Returns:
                str - string path
        """
        return os.path.join(CONSTS.Config.BASE_DIR, num)

    def map_num(num: int) -> CONSTS.Numbers:
        """
            Maps integers to corresponding CONSTS.Numbers values.
            
            Parameters: 
                num - int
                
            Returns:
                CONSTS.Numbers - mapped value
        """
        map_dat = {
            0: CONSTS.Numbers.NUM_0, 1: CONSTS.Numbers.NUM_1,
            2: CONSTS.Numbers.NUM_2, 3: CONSTS.Numbers.NUM_3,
            4: CONSTS.Numbers.NUM_4, 5: CONSTS.Numbers.NUM_5, 
            6: CONSTS.Numbers.NUM_6, 7: CONSTS.Numbers.NUM_7,
            8: CONSTS.Numbers.NUM_8, 9: CONSTS.Numbers.NUM_9
        }
        
        if num not in map_dat:
            raise Exception("Invalid integer specified. Valid format: regexp \\d")
        
        return map_dat[num]

    def get_safe_output_path(name: str, path: str) -> str:
        """
            Makes paths safe regardless of OS.
            
            Parameters:
                name - file name
                path - string of path with either fwd/backslashes.
                
            Returns:
                str - string of path with platform-specific path seps. + file name
        """
        safe_path = path.replace("/", os.path.sep).replace("\\", os.path.sep)
        
        if safe_path.endswith(os.path.sep) and len(safe_path) > 1: 
            safe_path = safe_path[:-1]
        
        if not os.path.isdir(safe_path) and not len(safe_path) == 0:
            raise Exception("Output path does not exist.")

        if os.path.isfile(os.path.join(safe_path, name)):
            raise Exception("File already exists.")
        
        return os.path.join(safe_path, name)

    def generate_audio(phone_num: List[List[int]], output_name="output.mp3", output_path="output/") -> None:
        """
            Generates audio based on provided phone number.
            
            Parameters:
                phone_num - Takes in a nested list. Example: [[4, 1, 6], [0, 0, 0], [0, 0, 0, 0]]
        """
        # start off with the base MP3
        final_output = AudioSegment.from_mp3(CreateVoicemail.generate_path(CONSTS.Segments.SEG_START))
        
        for group in phone_num:
            for num in group:
                final_output += AudioSegment.from_mp3(CreateVoicemail.generate_path(CreateVoicemail.map_num(num))) + \
                    CONSTS.Config.DIGITS_VOL_ADJ
            # add delay between groups
            final_output += AudioSegment.silent(duration=300)
        
        final_output += AudioSegment.from_mp3(CreateVoicemail.generate_path(CONSTS.Segments.SEG_END)) + \
            AudioSegment.from_mp3(CreateVoicemail.generate_path(CONSTS.Segments.SEG_BEEP))
        final_output += CONSTS.Config.GLOBAL_VOL_ADJ
        
        # + CONSTS.Config.VOL_ADJ lets you increase/decrease the global vol of the output MP3
        final_output.export(CreateVoicemail.get_safe_output_path(output_name, output_path))