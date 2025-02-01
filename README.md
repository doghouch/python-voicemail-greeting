# python-voicemail-greeting

### Introduction

My current carrier (of the blue/orange bird variety) in Canada does not provide pre-recorded greetings w/o mentioning your name.

I wanted to have a fairly generic one, and couldn't find one online that had the "signature" TTS voice, so I mashed this together using Microsoft Azure's Text-to-Speech (free tier) + NEURAL_CLARA (Canadian English) as the voice.

### Usage

There might be a web interface for this *eventually*, but for now, you can run the script locally (which is fairly simple).

1. Clone the repo:

    ```bash
    git clone https://github.com/doghouch/python-voicemail-greeting.git
    ```

2. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

3. Change `example.py` to match your phone number:

    ```python
                                      vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    CreateVoicemail.generate_audio([[4, 1, 6], [0, 0, 0], [0, 0, 0, 0]])
    ```

4. Run the script:

    ```bash
    python create_voicemail.py
    ```

    **By default, the generated audio will be saved to `output/output.mp3`.**

**Note:** The script is designed to be called programmatically. `generate_audio()` has an optional `output_path="output/"` parameter, and an optional `output_name="voicemail.mp3"` parameter for this purpose. Feel free to change it to your liking (go ahead and change the audio too, if you'd like!).

### Disclaimer

No warranties are provided while using this software. Feel free to pull, fork, and modify as you see fit. If you find any issues, let me know about them via/ "Issues."

### License

This project is licensed under MIT-0. See the LICENSE file for more details.

While licensed under MIT-0, the audio provided may not (though, I've seen a few posts about this, and it seems like no additional licensing exists for generated audio).

See the license file [here](?tab=MIT-0-1-ov-file).

I do appreciate acknowledgements, but <ins>by no means is it required</ins>.

### Credits

I'd like to thank the following projects/repositories:

- [PyDub](https://github.com/jiaaro/pydub)
  - This project would not have been possible (or would've been much more difficult) without the work of James Robert (http://jiaaro.com).
  - PyDub is licensed under the MIT License, so you must include the respective [LICENSE](https://github.com/jiaaro/pydub/blob/master/LICENSE) file if you use/distribute this.

- [GitHub/Gitignore Repo](https://github.com/github/gitignore/tree/main/)
  - Licensed under CC0-1.0.

- [Microsoft TTS](https://azure.microsoft.com/en-ca/services/cognitive-services/text-to-speech/)
  - Unknown license; used to provide sample `assets` (audio) for this project.

