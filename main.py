import os

import aubio
import cv2
import numpy as np

if __name__ == '__main__':
    video_filename = 'your file.mp4'
    s = aubio.source(video_filename)
    print(s.samplerate, s.hop_size)

    out_fvec = aubio.fvec(2)

    o = aubio.tempo(hop_size=s.hop_size, samplerate=s.samplerate)

    delay = 4. * s.hop_size

    # list of beats, in samples
    beats = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            this_beat = int(total_frames - delay + is_beat[0] * s.hop_size)
            # print("%f" % (this_beat / float(s.samplerate)))
            beats.append(this_beat * 1000 / float(s.samplerate))
        total_frames += read
        if read < s.hop_size: break
    # print(len(beats))
    # https://stackoverflow.com/questions/42934617/how-to-find-the-tempo-of-a-wav-with-aubio

    os.makedirs('res', exist_ok=True)
    cap = cv2.VideoCapture(video_filename)
    for idx, moment in enumerate(beats):
        cap.set(cv2.CAP_PROP_POS_MSEC, moment)
        success, image = cap.read()

        if success:
            cv2.imwrite(f"res/%0{len(str(len(beats)))}d.png" % idx, image)