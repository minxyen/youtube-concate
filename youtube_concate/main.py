from youtube_concate.pipeline.steps.preflight import Preflight
from youtube_concate.pipeline.steps.get_video_list import GetVideoList
from youtube_concate.pipeline.steps.download_captions import DownloadCaptions
from youtube_concate.pipeline.steps.read_caption import ReadCaption
from youtube_concate.pipeline.steps.postflight import Postflight
from youtube_concate.pipeline.steps.step import StepException
from youtube_concate.pipeline.pipeline import Pipeline
from youtube_concate.utils import Utils



# CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
CHANNEL_ID = 'UC1W9I8YtbX4Smf6RCAfMH1Q'  # for test


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        ReadCaption(),
        Postflight(),
        ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
