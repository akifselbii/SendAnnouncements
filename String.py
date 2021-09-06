#Mehmet Akif Selbi

wrongEntry = "Hatalı Girdi"
Error = "hata"

#Main
helpCommand = "          komutlar    ---> Komut Penceresini Açar"
_helpCommand ="komutlar"
interfaceCommand = "          arayuz      ---> Arayüzü Açar"
_interfaceCommand = "arayuz"
mailCommand = "          mail        ---> Komut Penceresinde mail işlemleri için"
_mailCommand = "mail"
announcementsCommand = "          duyuru      ---> Duyuruları listeler"
_announcementsCommand = "duyuru"
createAnnouncement = "          olustur     ---> Duyuru oluşturup göndermek için"
_createAnnouncement = "olustur"
startCommand = "          baslat      ---> Programı Başlatır (Atılmış mail bir daha atılmaz)"
_startCommand = "baslat"
deleteStartCommand = "          silbaslat   ---> Programı Başlatır (Atılmış mail bir daha atılabilir)"
_deleteStartCommand = "silbaslat"
exitCommand = "          kapat       ---> Program sonlanır"
_exitCommand = "kapat"

inpt = ">>>"
registeredMail = "Kayıtlı Kişinin Maili >>"
numberOfMail = "Aynı anda kaç mail atılacağını giriniz >>"

subject = "Konu :"
body = "Yazı : "
sendClass = "Atılacak sınıf :"

zero = "     0-Tümüne"
facultyList = ['Mühendislik Fakültesi','Biga İktisadi ve İdari Bilimler Fakültesi','Biga Uygulamalı Bilimler Fakültesi',
               'Çanakkale Uygulamalı Bilimler Fakültesi','Deniz Bilimleri ve Teknolojisi Fakültesi',
               'Diş Hekimliği Fakültesi.','Eğitim Fakültesi.','Fen Edebiyat Fakültesi','Güzel Sanatlar Fakültesi',
               'İlahiyat Fakültesi','İletişim Fakültesi','Mimarlık ve Tasarım Fakültesi',
               'Sağlık Bilimleri Fakültesi','Siyasal Bilgiler Fakültesi',
               'Spor Bilimleri Fakültesi.','Turizm Fakültesi.','Tıp Fakültesi.','Ziraat Fakültesi']

departmentList = [['Bilgisayar Mühendisliği','Biyomühendislik','Çevre Mühendisliği','Elektronik Mühendisliği','Endüstri Mühendisliği',
                   'Harita Mühendisliği','Gıda Mühendisliği ','İnşaat Mühendisliği','Jeofizik Mühendisliği','Jeoloji Mühendisliği',
                   'Kimya Mühendisliği','Maden Mühendisliği','Malzeme Bilimi ve Mühendisliği'],
                  ['Uluslararası İlişkiler','Maliye','Kamu Yönetimi','İşletme','İktisat','Ekonometri','Çalışma Ekonomisi ve Endüstri İlişkileri'],
                  ['Uluslararası Ticaret ve Lojistik Bölümü','Finans ve Bankacılık Bölümü'],
                  ['Gıda Teknolojisi ','Balıkçılık Teknolojisi','Sağlık Yönetimi','Enerji Yönetimi ','Sosyal Hizmet',
                   'Müzecilik ve Kültürel Miras Yönetimi','Moda Tasarımı'],
                  ['Su Ürünleri Mühendisliği','Temel Bilimler','Yetiştiricilik','Avlama ve İşleme Teknolojisi','Deniz Teknoloji Mühendisliği',
                   'Gemi İnşaatı ve Gemi Makineleri Mühendisliği Bölümü','Deniz Ulaştırma İşletme Mühendisliği'],
                  ['Diş Hekimliği.'],['Eğitim.'],
                  ['Arkeoloji','Batı Dilleri ve Edebiyatları','Biyoloji','Coğrafya ','Doğu Dilleri ve Edebiyatları',
                   'Felsefe','Fizik','İstatistik','Kimya','Matematik','Moleküler Biyoloji ve Genetik','Psikoloji',
                   'Sanat Tarihi','Sosyoloji','Tarih','Türk Dili ve Edebiyatı','Uzay Bilimleri ve Teknolojileri '],
                  ['Geleneksel Türk Sanatları Bölümü','Grafik Tasarım Bölümü','Resim Bölümü','Seramik ve Cam Bölümü','Tekstil ve Moda Tasarımı',
                   'Tiyatro Bölümü'],
                  ['Temel İslam Bilimleri','Felsefe ve Din Bilimleri','İslam Tarihi ve Sanatları'],
                  ['Radyo-Televizyon ve Sinema ','Gazetecilik','Görsel İletişim Tasarımı','Halkla İlişkiler ve Reklamcılık','Yeni Medya','İletişim Bilimleri'],
                  ['Endüstri Ürünleri Tasarımı','İç Mimarlık','Mimarlık','Peyzaj Mimarlığı ','Şehir ve Bölge Planlama'],
                  ['Hemşirelik','Ebelik','Acil Yardım ve Afet Yönetimi'],
                  ['Siyaset Bilimi ve Kamu Yönetimi Bölümü','İktisat Bölümü','İşletme','Uluslararası İlişkiler Bölümü'],
                  ['Spor Bilimleri.'],['Turizm.'],['Tıp.'],
                  ['Bahçe Bitkileri','Bitki Koruma','Tarım Ekonomisi','Tarım Makinalari ve Teknolojileri Mühendisliği',
                   'Tarımsal Biyoteknoloji ','Tarımsal Yapılar ve Sulama','Tarla Bitkileri','Toprak Bilimi ve Bitki Besleme','Zootekni']]

#Database
registeredUser = "Kayıtlı Kullanıcı"
noMail = "Böyle bir mail yok"

#SendMail
baseMail = ""#mail
password = ""#mailPassword
comuAnnouncement = "COMU Duyuru"
successfulSending = "Mail Gönderildi %s:"

#Announcements
annoouncementLink = "\nDuyuru Linki : "

facultyTagList = ['muhendislik','biibf','bigaubf','cubf','denbiltek','dishekimligi',
             'egitim','fef','gsf','ilahiyat','iletisim','mtf','saglikbf','sbf','sporbf','turizm','tip','ziraat']

departmentTagList = [['ce','biyo','cevre','?','?',
                   'harita','gida','insaat','jeofizik','jeoloji','chemeng','maden','?'],
                  ['uluslararasiiliskiler','maliye','kamu','isletme','iktisat','ekonometri','!'],
                  ['!','!'],
                  ['gida','balikcilik','saglik','enerji','!','muzecilik','!'],
                  ['!','!','!','!','!','!','!'],
                  ['!'],
                  ['!'],
                  ['arkeoloji','ide','biyoloji','cografya','?','felsefe','physics',
                   'istatistik','kimya','math','molbio','?','sanattarihi','sosyoloji','tarih','turkdiliveedebiyati','ubt'],
                   ['?','?','resim','?','?','?'],
                   ['!','!','!'],
                   ['!','!','!','!','!','!'],
                   ['!','!','mimarlik','peyzaj','sbp'],
                   ['hem','ebelik','ayay'],
                   ['sbky','iktisat','isletme','ir'],
                   ['!'],
                   ['!'],
                   ['!'],
                   ['bahce','bitkikoruma','?','tarmak','tbt','tys','tarla','toprak','zootekni']]

#TerminalManager
saveCommand = "          kaydet   ---> Terminalden mail ve kişi kaydetmek için"
_saveCommand = "kaydet"
deleteCommand = "          sil      ---> Kayitli kişileri silmek için"
_deleteCommand = "sil"
listCommand = "          listele  ---> Kayıtlı kişileri listelemek için"
_listCommand = "listele"
backCommand = "          geri     ---> Komut Penceresine dönmek için"
_backCommand = "geri"

inptMail = "m>>"

enterMinutes = "Dakika Giriniz >>"
noNewAnnouncements = " Yeni Duyuru Yok"

name = "İsim :"
mail = "Mail :"
faculty = "FakulteNo :"
department = "BölümNo :"

#GUInterface
mailListI = "Mail Listesi"
saveMailI = "Mail Kaydet"
announcementsI = "Duyurular"
nameI = "İsim"
mailI = "Mail"
addI = "Ekle"
deleteI = "Sil"
refreshI = "Yenile"
findI = "Bul"
startI = "Başlat"
deleteStartI = "Sil Başlat"
mailSaveBox = "Mail     İsim     Fakülte     Bölüm"
timeI = "Kaç Dakikada Bir Kontrol Edilecek"
numI = "Aynı Anda Gönderilecek Mail Sayısı"
facultyName = "Fakülteler"
departmentName = "Bölümler"
createAnnouncementI = "Duyuru Oluştur"
subjectI = "Konu"
bodyI = "Yazı"
sendI = "Gönder"
saveI = "Kaydet"
warningI = "Lütfen Tüm Alanları Doldurunuz"
allFacultySendI = "Tüm Fakültelere Gönder"
allDepartmentSendI = "Tüm Bölümlerine Gönder"
width = 800
height = 600
