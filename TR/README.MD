GNU/Linux sistemlerin yönetiminde bildirim almak elbette önemli. E-posta ile bildirim göndermek ise en çok kullanılan yöntemlerden. Konsoldan `mail` komutu ile e-posta göndermede sorun yaşıyor iseniz; güvenli, kolay ve stabil bir yöntem olarak aşağıdaki script'i kullanabilirsiniz. ***SMTP client*** ile ***kullanıcı adı*** ve ***şifre*** kullanılarak e-posta gönderimi  yapıldığından, e-postanızın sağlıklı şekilde yerine ulaştığından emin olabilirsiniz. 

## Kurulum (Debian)
 1. Ben Yandex sunucularını kullandığımdan, önce bir Yandex hesabınızın olması gerekiyor. *(Bu hesap bilgileri, script'in şu değişkenlerinde kullanılacak: ***gonderen, user, password***)*
 
 3. Daha sonra `heirloom-mailx` paketini kuruyoruz. 
	 ```
	 apt-get install heirloom-mailx
	 ```

## Python Script

Aşağıdaki kodları `send-mail.py` dosyasına kayıt edelim.
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *** README ***
# Önce aşağıdaki kurulum yapılır.
# apt-get install heirloom-mailx

import os

# ********** TANIMLAR **********
mesaj = "Buraya mesaj yazılacak..."
gonderen = "kullanıcı@yandex.com (Gönderen Adı)"
konu = "Buraya konu yazılacak..."
smtpserver = "smtp.yandex.com:587"
user = "kullanıcı@yandex.com"
password = "KULLANICININ_ŞİFRESİ"
kime = "user@example.com"
# ******** TANIMLAR SON ********

os.system('echo "%s" | heirloom-mailx -v -r "%s" -s "%s" -S smtp="%s" -S smtp-use-starttls -S smtp-auth=login -S smtp-auth-user="%s" -S smtp-auth-password="%s" -S ssl-verify=ignore %s' % (mesaj, gonderen, konu, smtpserver, user, password, kime))

exit ()
```

... ve çalıştırıp e-postayı gönderiyoruz...
```
$ python3 send-mail.py 
```
