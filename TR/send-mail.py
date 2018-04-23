#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *** README ***
# Önce aşağıdaki kurulum yapılır.
# apt-get install heirloom-mailx

import os

# ********** TANIMLAR **********
mesaj = "Buraya mesaj yazılacak..."
gonderen = "zadh.bildirim@yandex.com (Yazıcılar Merkez Bildirim)"
baslik = "[Yazicilar Merkez] IP Değişti"
smtpserver = "smtp.yandex.com.tr:587"
user = "zadh.bildirim@yandex.com"
password = "2858Bim2859"
kime = "aytekinaygun@gmail.com"
# ******** TANIMLAR SON ********

os.system('echo "%s" | heirloom-mailx -v -r "%s" -s "%s" -S smtp="%s" -S smtp-use-starttls -S smtp-auth=login -S smtp-auth-user="%s" -S smtp-auth-password="%s" -S ssl-verify=ignore %s' % (mesaj, gonderen, baslik, smtpserver, user, password, kime))

exit ()
