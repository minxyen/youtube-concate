import time

from pytube import YouTube

from .step import Step
from .step import StepException



class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print('Downloading Caption for', yt.url)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            try:
                source = YouTube(yt.url)
                # if the video has auto caption: a.en; if the video has manual caption: en; if neither, simply pass
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                print('Attribute Error when downloading for, the video does not have auto caption', yt.url)
                continue

            except KeyError:
                print('Key Error when downloading for', yt.url)
                continue

            # print(en_caption_convert_to_srt)

            # save the caption to a file named {vidoe_id}.txt
            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        end = time.time()
        print('took', end - start, 'secs')

        return data
