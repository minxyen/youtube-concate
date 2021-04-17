
from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):

        for url in data:
            source = YouTube(url)
            try:
                # if the video has auto caption: a.en
                # if the video has manual caption: en
                # if neither, simply pass
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                continue
            print(en_caption_convert_to_srt)

            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_path(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
