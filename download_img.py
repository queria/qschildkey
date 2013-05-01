#!/usr/bin/python

from __future__ import print_function

import os
import sys
import json
import urllib2
import wand.image


def mprint(text):
    print(text, end='... ')
    sys.stdout.flush()


if __name__ == '__main__':
    with open('./img/source.json', 'r') as src:
        urls = json.load(src)
    max_size = 1000.0
    for name in urls:
        mprint(name)
        tmp_path = './img/tmp_{0}'.format(name)
        tgt_path = './img/{0}.png'.format(name)
        forced = '--force' in sys.argv

        try:
            if not forced and os.path.exists(tgt_path):
                print('already done')
                continue
            if not os.path.exists(tmp_path):
                conn = urllib2.urlopen(urls[name])
                with open(tmp_path, 'w') as tmp:
                    mprint('downloading')
                    tmp.write(conn.read())

            with wand.image.Image(filename=tmp_path) as tmp_img:
                mprint('processing')
                mprint(tmp_img.size)
                mprint(tmp_img.width)
                mprint(tmp_img.height)
                big_side = max(tmp_img.width, tmp_img.height)
                mprint(big_side)
                scale = min(1, max_size / big_side)
                mprint(scale)
                with tmp_img.clone() as img:
                    img.resize(
                        int(tmp_img.width * scale),
                        int(tmp_img.height * scale))
                    img.save(filename=tgt_path)

            os.unlink(tmp_path)
            print('')
        except IOError as e:
            print("Unable to process file {0}:\n  {1}".format(
                name, str(e)))

        #print('[[ -f "./img/tmp_{0}" ]] '
        #      '|| curl -o "./img/tmp_{0}" "{1}"'.format(
        #          img, urls[img]))
        #print('convert "./img/tmp_{0}" {1} "./img/{0}.png" '
        #      '|| echo "{0} FAILED" '.format(
        #          img, copts))
