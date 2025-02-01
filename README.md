# python-voicemail-greeting

### Introduction

My current carrier (of the blue/orange bird variety) in Canada does not provide pre-recorded greetings w/o mentioning your name.

I wanted to have a fairly generic one, and couldn't find one online that had the "signature" TTS voice, so I mashed this together using Microsoft Azure's Text-to-Speech (free tier) + NEURAL_CLARA (Canadian English) as the voice. 

Edit: I've added a British voice (NARRATION_SONIA) as well, but it's a tad glitchy (and I haven't had the chance to fix it).

### Transcription(s)

The Canadian voice will read: 

> Your call has been forwarded to an automated voice messaging system. [phone number] is not available. At the tone, please record your message.

  <audio controls><source src="https://c.0z.pm/github/canadian.mp3" type="audio/mpeg"></audio>

The British voice will read: 

> Your call has been forwarded to an automated voice messaging system. [phone number] is not available. At the tone, please record your message. When you have finished recording, you may hang up or press pound for more options.

  <audio controls><source src="https://c.0z.pm/github/british.mp3" type="audio/mpeg"></audio>

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

4. Create `output/` directory (if it doesn't alr. exist):

    ```bash
    mkdir output
    ```

5. Run the script:

    ```bash
    python create_voicemail.py
    ```

    **By default, the generated audio will be saved to `output/output.mp3`.**

**Note:** The script is designed to be called programmatically. `generate_audio()` has an optional `output_path="output/"` parameter, and an optional `output_name="voicemail.mp3"` parameter for this purpose. Feel free to change it to your liking (go ahead and change the audio too, if you'd like!).

### Disclaimer

No warranties are provided while using this software. Feel free to pull, fork, and modify as you see fit. If you find any issues, let me know about them via/ [GitHub Issues](https://github.com/doghouch/python-voicemail-greeting/issues). Alternatively, fork the project, and open a pull request.

### License

This project is licensed under MIT-0. See the LICENSE file for more details.

While licensed under MIT-0, the audio provided may not (though, I've seen a few posts about this, and it seems like no additional licensing exists for generated audio).

See the license file [here](https://github.com/doghouch/python-voicemail-greeting/blob/main/LICENSE).

I appreciate acknowledgements, but <ins>by no means is this required</ins>.

### Credits

I'd like to thank the following projects/repositories:

- [PyDub](https://github.com/jiaaro/pydub)
  - This project would not have been possible (or would've been much more difficult) without the work of James Robert (http://jiaaro.com).
  - PyDub is licensed under the MIT License, so you must include the respective [LICENSE](https://github.com/jiaaro/pydub/blob/master/LICENSE) file if you use/distribute this.

- [GitHub/Gitignore Repo](https://github.com/github/gitignore/tree/main/)
  - Licensed under CC0-1.0.

- [Microsoft TTS](https://azure.microsoft.com/en-ca/services/cognitive-services/text-to-speech/)
  - Unknown license; used to provide sample `assets` (audio) for this project.

