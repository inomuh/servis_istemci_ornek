#!/usr/bin/env python
# coding=utf-8

import rospy
from std_srvs.srv import *


class IstemciOrnek(object):
    def __init__(self):
        self.ana_fonksiyon()

    def ana_fonksiyon(self):
        # Servise gönderilecek isteği tutan değişken
        gonderilecek_istek = True

        # İstemci fonksiyonunu çağırarak servise gönderilmek istenen istek gönderilir.
        # servisten_gelen_yanit değerine Serviste yapılan işlem sonucu yanıt değeri dönmektedir.
        servisten_gelen_yanit = self.bilgi_servisi_ornek_istemcisi_fonksiyonu(gonderilecek_istek)
        print("Servisten Gelen Yanit")
        print("\nYanit 1 = " + str(servisten_gelen_yanit.success))
        print("\nYanit 2 = " + str(servisten_gelen_yanit.message) + "\n\n")

    def bilgi_servisi_ornek_istemcisi_fonksiyonu(self, istek):
        rospy.wait_for_service('bilgi_servisi_ornek')
        try:
            # bilgi_servisi_ornek servisi ile bağlantıyı sağlamaktadır.
            bilgi_servisi_ornek = rospy.ServiceProxy('bilgi_servisi_ornek', SetBool)
            # Servise isteği parametre olarak yollar ve servisin cevabı yanit olarak gelmektedir.
            yanit = bilgi_servisi_ornek.call(SetBoolRequest(istek))

            return yanit

        except rospy.ServiceException, e:
            print "Service call failed: %s" % e

if __name__ == '__main__':
    try:
        rospy.init_node('istemci_ornek_dugumu', anonymous=True)

        # IstemciOrnek() sınıfını çağırmaktadır.
        dugum = IstemciOrnek()

    except rospy.ROSInterruptException:
        pass
