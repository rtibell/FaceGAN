#!/bin/sh
FILE='epoch*.jpg'

if [ -e /home/rasse/Projects/GAN-face/newFacesC/epoch*.jpg ]
then
    echo "file excists"
    SH=`cd /home/rasse/Projects/GAN-face/newFacesC && ls -1 epoch*.jpg` 
    curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"New file $SH excists!\"}" https://hooks.slack.com/services/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
else
    echo "no file"
fi
