import wx
from wx.core import CLEAR
import index1
from dbconn import conn
cursor = conn.cursor()

class login(index1.MyFrame1):
    def __init__ (self,parent):
        index1.MyFrame1.__init__(self,parent)
        self.panelHome = home(parent = self)
        self.panelHome.Hide()

    def Login(self,event):
        Username = self.input_username.GetValue()
        Password = self.input_password.GetValue()
        cursor = conn.cursor()
        sql = "SELECT * FROM customer WHERE username= %s AND password= %s"
        try :
            cursor.execute(sql, (Username, Password))
            results = cursor.fetchall()[0]
            self.panelHome.Show()
            self.panel_login.Hide()
            self.panelHome.profilSaya(results)
        except :
            wx.MessageBox('Silahkan Masukkan Username dan Password dengan Benar')

    def RegisterAwal(self, event):
        self.Regis = regis(parent = self)
        self.Regis.Show()
        self.panel_login.Hide()


class home(index1.panel_home):
    def __init__ (self,parent):
        index1.panel_home.__init__(self,parent)
        self.parent = parent

    def BeliTiket(self,event):
        self.nama = self.input_nama.GetValue()
        self.tanggal_keberangkatan = self.input_tanggal.GetValue()
        self.waktu = self.input_waktu.GetValue()
        self.jumlah_penumpang = self.input_jumlahPenumpang.GetValue()
        harga = int(self.jumlah_penumpang) * 30000
        query = "INSERT INTO data_tiket (nama, tanggal_keberangkatan, waktu, jumlah_penumpang, harga) VALUES ('{}','{}','{}','{}', '{}')".format(
            self.nama,self.tanggal_keberangkatan, self.waktu, self.jumlah_penumpang, harga)
        cursor.execute(query)
        conn.commit()
        self.lihatTiket()
        wx.MessageBox('Terimakasih telah membeli tiket!')
        self.nama = self.input_nama.Clear()
        self.tanggal_keberangkatan = self.input_tanggal.Clear()
        self.waktu = self.input_waktu.Clear()
        self.jumlah_penumpang = self.input_jumlahPenumpang.Clear()

    def lihatTiket(self):
        query = "Select * from data_tiket where nama = '{}'".format(self.nama)
        cursor.execute(query)
        results = cursor.fetchall()[0]
        print(results)
        self.m_textCtrl26.SetValue(str(results[5]))
        self.input_lihatNama.SetValue(str(results[0]))
        self.input_lihatTanggal.SetValue(str(results[1]))
        self.input_lihatWaktu.SetValue(str(results[2]))
        self.input_lihatJumlah.SetValue(str(results[3]))
        self.input_lihatHarga.SetValue(str(results[4]))

    def CariIdBatal(self, event):
        self.idBatal = self.input_idBatal.GetValue()
        query = "Select * from data_tiket where id_tiket = '{}'".format(self.idBatal)
        try :
            cursor.execute(query)
            results = cursor.fetchall()[0]
            print(results)
            self.input_batalId.SetValue(str(results[5]))
            self.input_batalNama.SetValue(str(results[0]))
            self.input_batalTanggal.SetValue(str(results[1]))
            self.input_batalWaktu.SetValue(str(results[2]))
            self.input_batalJumlah.SetValue(str(results[3]))
            self.input_batalHarga.SetValue(str(results[4]))
        except :
            wx.MessageBox("Masukkan ID Tiket dengan Benar")
    
    def Batalkan(self, event):
        self.idBatal = self.input_idBatal.GetValue()
        query = "Delete from data_tiket where id_tiket = '{}'".format(self.idBatal)
        cursor.execute(query)
        conn.commit()
        wx.MessageBox("Berhasil Dihapus")
        self.input_batalId.Clear()
        self.input_batalNama.Clear()
        self.input_batalTanggal.Clear()
        self.input_batalWaktu.Clear()
        self.input_batalJumlah.Clear()
        self.input_batalHarga.Clear()

    def profilSaya(self,data):
        self.input_profilNama.SetValue(str(data[1]))
        self.input_profilKelamin.SetValue(str(data[2]))
        self.input_profilNomor.SetValue(str(data[3]))
        self.input_profilKota.SetValue(str(data[4]))
        self.input_profilEmail.SetValue(str(data[5]))
        self.input_profilUsername.SetValue(str(data[6]))
        self.input_profilPassword.SetValue(str(data[7]))

    def logout(self, event):
        self.parent.panel_login.Show()
        self.Hide()
        self.parent.input_username.Clear()
        self.parent.input_password.Clear()




class regis(index1.panel_regis):
    def __init__ (self,parent):
        index1.panel_regis.__init__(self,parent)
        self.parent = parent

    def Register(self, event):
        nama_lengkap = self.input_namaLengkap.GetValue()
        jenis_kelamin = self.input_kelamin.GetValue()
        nomor_telepon = self.m_textCtrl19.GetValue()
        kota_asal = self.input_kota.GetValue()
        email = self.input_email.GetValue()
        username = self.input_username.GetValue()
        password = self.input_password.GetValue()
        query = "INSERT INTO customer (nama_lengkap, jenis_kelamin, nomor_telepon, kota_asal, email, username, password) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(
            nama_lengkap, jenis_kelamin, nomor_telepon, kota_asal, email, username, password)
        cursor.execute(query)
        conn.commit()
        self.Hide()
        self.parent.panel_login.Show()



if __name__ == "__main__":
    app = wx.App(False)
    frame = login(None)
    frame.Show(True)
    app.MainLoop()
