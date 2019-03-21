#!/bin/sh
HOST='www15.space2u.com'
USER='d35632-ml'
PASSWD='K0ll1Face'
FILE='epoch*.jpg'
FTPLOG='ftp-trans.log'


for FILE in `cd /home/rasse/Projects/GAN-face/newFacesC && ls -1 epoch*.jpg`
do

ftp -dpnv $HOST>$FTPLOG <<END_SCRIPT
quote USER $USER
quote PASS $PASSWD
binary
lcd /home/rasse/Projects/GAN-face/newFacesC
put $FILE
quit
END_SCRIPT

    mv /home/rasse/Projects/GAN-face/newFacesC/$FILE /home/rasse/Projects/GAN-face/newFacesCMoved/$FILE
done
