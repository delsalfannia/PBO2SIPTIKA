# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.panel_login = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_login.SetBackgroundColour( wx.Colour( 198, 132, 219 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( self.panel_login, wx.ID_ANY, u"SIPTIKA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Cocogoose Pro" ) )
		self.m_staticText17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer2.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.label_username = wx.StaticText( self.panel_login, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_username.Wrap( -1 )

		self.label_username.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		fgSizer1.Add( self.label_username, 0, wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self.panel_login, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.input_username.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer1.Add( self.input_username, 0, wx.ALL, 5 )

		self.label_password = wx.StaticText( self.panel_login, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_password.Wrap( -1 )

		self.label_password.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		fgSizer1.Add( self.label_password, 0, wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self.panel_login, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.input_password.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer1.Add( self.input_password, 0, wx.ALL, 5 )

		self.btn_login = wx.Button( self.panel_login, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_login.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "COCOGOOSE" ) )

		fgSizer1.Add( self.btn_login, 0, wx.ALL, 5 )

		self.btn_register = wx.Button( self.panel_login, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_register.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )
		self.btn_register.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.btn_register.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer1.Add( self.btn_register, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_login.SetSizer( bSizer2 )
		self.panel_login.Layout()
		bSizer2.Fit( self.panel_login )
		bSizer1.Add( self.panel_login, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_login.Bind( wx.EVT_BUTTON, self.Login )
		self.btn_register.Bind( wx.EVT_BUTTON, self.RegisterAwal )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Login( self, event ):
		event.Skip()

	def RegisterAwal( self, event ):
		event.Skip()


###########################################################################
## Class panel_home
###########################################################################

class panel_home ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 213, 163, 228 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		bSizer3.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_logout = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_logout.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )
		self.btn_logout.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.btn_logout.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer3.Add( self.btn_logout, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.panel_home1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel_home1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "COCOGOOSE" ) )
		self.panel_home1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		self.panel_beli = wx.Panel( self.panel_home1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_beli.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.panel_beli.SetMaxSize( wx.Size( -1,5 ) )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.text_nama = wx.StaticText( self.panel_beli, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_nama.Wrap( -1 )

		self.text_nama.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer1.Add( self.text_nama, 0, wx.ALL, 5 )

		self.input_nama = wx.TextCtrl( self.panel_beli, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_nama.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer1.Add( self.input_nama, 0, wx.ALL, 5 )

		self.text_tanggal = wx.StaticText( self.panel_beli, wx.ID_ANY, u"Tanggal Keberangkatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_tanggal.Wrap( -1 )

		self.text_tanggal.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer1.Add( self.text_tanggal, 0, wx.ALL, 5 )

		self.input_tanggal = wx.TextCtrl( self.panel_beli, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_tanggal.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer1.Add( self.input_tanggal, 0, wx.ALL, 5 )

		self.text_waktu = wx.StaticText( self.panel_beli, wx.ID_ANY, u"Waktu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_waktu.Wrap( -1 )

		self.text_waktu.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer1.Add( self.text_waktu, 0, wx.ALL, 5 )

		input_waktuChoices = [ u"07.00", u"12.00", u"17.00", u"20.00", u"24.00" ]
		self.input_waktu = wx.ComboBox( self.panel_beli, wx.ID_ANY, u"Waktu", wx.DefaultPosition, wx.Size( 350,-1 ), input_waktuChoices, 0 )
		self.input_waktu.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer1.Add( self.input_waktu, 0, wx.ALL, 5 )

		self.text_jumlahPenumpang = wx.StaticText( self.panel_beli, wx.ID_ANY, u"Jumlah Penumpang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_jumlahPenumpang.Wrap( -1 )

		self.text_jumlahPenumpang.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer1.Add( self.text_jumlahPenumpang, 0, wx.ALL, 5 )

		self.input_jumlahPenumpang = wx.TextCtrl( self.panel_beli, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_jumlahPenumpang.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer1.Add( self.input_jumlahPenumpang, 0, wx.ALL, 5 )

		self.text_harga = wx.StaticText( self.panel_beli, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_harga.Wrap( -1 )

		self.text_harga.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer1.Add( self.text_harga, 0, wx.ALL, 5 )

		self.input_harga = wx.TextCtrl( self.panel_beli, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_harga.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )
		self.input_harga.SetBackgroundColour( wx.Colour( 147, 155, 253 ) )

		gSizer1.Add( self.input_harga, 0, wx.ALL, 5 )

		self.btn_beli = wx.Button( self.panel_beli, wx.ID_ANY, u"Beli", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_beli.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer1.Add( self.btn_beli, 0, wx.ALL, 5 )


		self.panel_beli.SetSizer( gSizer1 )
		self.panel_beli.Layout()
		gSizer1.Fit( self.panel_beli )
		self.panel_home1.AddPage( self.panel_beli, u"Beli Tiket", True )
		self.panel_lihatTiket = wx.Panel( self.panel_home1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.text_lihatId = wx.StaticText( self.panel_lihatTiket, wx.ID_ANY, u"ID Tiket", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_lihatId.Wrap( -1 )

		self.text_lihatId.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		bSizer6.Add( self.text_lihatId, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self.panel_lihatTiket, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.m_textCtrl26.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		bSizer6.Add( self.m_textCtrl26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_lihatNama = wx.StaticText( self.panel_lihatTiket, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_lihatNama.Wrap( -1 )

		self.text_lihatNama.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		bSizer6.Add( self.text_lihatNama, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_lihatNama = wx.TextCtrl( self.panel_lihatTiket, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_lihatNama.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		bSizer6.Add( self.input_lihatNama, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_lihatTanggal = wx.StaticText( self.panel_lihatTiket, wx.ID_ANY, u"Tanggal Keberangkatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_lihatTanggal.Wrap( -1 )

		self.text_lihatTanggal.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		bSizer6.Add( self.text_lihatTanggal, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_lihatTanggal = wx.TextCtrl( self.panel_lihatTiket, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_lihatTanggal.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		bSizer6.Add( self.input_lihatTanggal, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_lihatWaktu = wx.StaticText( self.panel_lihatTiket, wx.ID_ANY, u"Waktu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_lihatWaktu.Wrap( -1 )

		self.text_lihatWaktu.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		bSizer6.Add( self.text_lihatWaktu, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_lihatWaktu = wx.TextCtrl( self.panel_lihatTiket, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_lihatWaktu.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		bSizer6.Add( self.input_lihatWaktu, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_jumlahPenumpang = wx.StaticText( self.panel_lihatTiket, wx.ID_ANY, u"Jumlah Penumpang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_jumlahPenumpang.Wrap( -1 )

		self.text_jumlahPenumpang.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		bSizer6.Add( self.text_jumlahPenumpang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_lihatJumlah = wx.TextCtrl( self.panel_lihatTiket, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_lihatJumlah.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		bSizer6.Add( self.input_lihatJumlah, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_lihatHarga = wx.StaticText( self.panel_lihatTiket, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_lihatHarga.Wrap( -1 )

		self.text_lihatHarga.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		bSizer6.Add( self.text_lihatHarga, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_lihatHarga = wx.TextCtrl( self.panel_lihatTiket, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_lihatHarga.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		bSizer6.Add( self.input_lihatHarga, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.panel_lihatTiket.SetSizer( bSizer6 )
		self.panel_lihatTiket.Layout()
		bSizer6.Fit( self.panel_lihatTiket )
		self.panel_home1.AddPage( self.panel_lihatTiket, u"Lihat Tiket", False )
		self.panel_batal = wx.Panel( self.panel_home1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer41 = wx.GridSizer( 0, 2, 0, 0 )

		self.text_batalId = wx.StaticText( self.panel_batal, wx.ID_ANY, u"Masukkan ID Tiket yang dibatalkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_batalId.Wrap( -1 )

		self.text_batalId.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.text_batalId, 0, wx.ALL, 5 )

		self.input_idBatal = wx.TextCtrl( self.panel_batal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_idBatal.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer41.Add( self.input_idBatal, 0, wx.ALL, 5 )

		self.btn_cariBatal = wx.Button( self.panel_batal, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_cariBatal.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.btn_cariBatal, 0, wx.ALL, 5 )


		gSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.text_batalID = wx.StaticText( self.panel_batal, wx.ID_ANY, u"ID Tiket", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_batalID.Wrap( -1 )

		self.text_batalID.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.text_batalID, 0, wx.ALL, 5 )

		self.input_batalId = wx.TextCtrl( self.panel_batal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_batalId.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer41.Add( self.input_batalId, 0, wx.ALL, 5 )

		self.text_batalNama = wx.StaticText( self.panel_batal, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_batalNama.Wrap( -1 )

		self.text_batalNama.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.text_batalNama, 0, wx.ALL, 5 )

		self.input_batalNama = wx.TextCtrl( self.panel_batal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_batalNama.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer41.Add( self.input_batalNama, 0, wx.ALL, 5 )

		self.text_batalTanggal = wx.StaticText( self.panel_batal, wx.ID_ANY, u"Tanggal Keberangkatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_batalTanggal.Wrap( -1 )

		self.text_batalTanggal.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.text_batalTanggal, 0, wx.ALL, 5 )

		self.input_batalTanggal = wx.TextCtrl( self.panel_batal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_batalTanggal.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer41.Add( self.input_batalTanggal, 0, wx.ALL, 5 )

		self.text_batalWaktu = wx.StaticText( self.panel_batal, wx.ID_ANY, u"Waktu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_batalWaktu.Wrap( -1 )

		self.text_batalWaktu.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.text_batalWaktu, 0, wx.ALL, 5 )

		self.input_batalWaktu = wx.TextCtrl( self.panel_batal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_batalWaktu.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer41.Add( self.input_batalWaktu, 0, wx.ALL, 5 )

		self.text_batalJumlah = wx.StaticText( self.panel_batal, wx.ID_ANY, u"Jumlah Penumpang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_batalJumlah.Wrap( -1 )

		self.text_batalJumlah.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.text_batalJumlah, 0, wx.ALL, 5 )

		self.input_batalJumlah = wx.TextCtrl( self.panel_batal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_batalJumlah.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer41.Add( self.input_batalJumlah, 0, wx.ALL, 5 )

		self.text_batalHarga = wx.StaticText( self.panel_batal, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_batalHarga.Wrap( -1 )

		self.text_batalHarga.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.text_batalHarga, 0, wx.ALL, 5 )

		self.input_batalHarga = wx.TextCtrl( self.panel_batal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_batalHarga.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer41.Add( self.input_batalHarga, 0, wx.ALL, 5 )

		self.btn_batalkan = wx.Button( self.panel_batal, wx.ID_ANY, u"Batalkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_batalkan.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer41.Add( self.btn_batalkan, 0, wx.ALL, 5 )


		self.panel_batal.SetSizer( gSizer41 )
		self.panel_batal.Layout()
		gSizer41.Fit( self.panel_batal )
		self.panel_home1.AddPage( self.panel_batal, u"Batal Tiket", False )
		self.panel_profil = wx.Panel( self.panel_home1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.text_profilNama = wx.StaticText( self.panel_profil, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_profilNama.Wrap( -1 )

		self.text_profilNama.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer4.Add( self.text_profilNama, 0, wx.ALL, 5 )

		self.input_profilNama = wx.TextCtrl( self.panel_profil, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 350,-1 ), 0 )
		self.input_profilNama.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer4.Add( self.input_profilNama, 0, wx.ALL, 5 )

		self.text_profilKelamin = wx.StaticText( self.panel_profil, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_profilKelamin.Wrap( -1 )

		self.text_profilKelamin.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer4.Add( self.text_profilKelamin, 0, wx.ALL, 5 )

		self.text_profilEmail = wx.StaticText( self.panel_profil, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_profilEmail.Wrap( -1 )

		self.text_profilEmail.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer4.Add( self.text_profilEmail, 0, wx.ALL, 5 )

		self.input_profilKelamin = wx.TextCtrl( self.panel_profil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.input_profilKelamin.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer4.Add( self.input_profilKelamin, 0, wx.ALL, 5 )

		self.input_profilEmail = wx.TextCtrl( self.panel_profil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.input_profilEmail.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer4.Add( self.input_profilEmail, 0, wx.ALL, 5 )

		self.text_profilNomor = wx.StaticText( self.panel_profil, wx.ID_ANY, u"Nomor Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_profilNomor.Wrap( -1 )

		self.text_profilNomor.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer4.Add( self.text_profilNomor, 0, wx.ALL, 5 )

		self.text_profilUsername = wx.StaticText( self.panel_profil, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_profilUsername.Wrap( -1 )

		self.text_profilUsername.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer4.Add( self.text_profilUsername, 0, wx.ALL, 5 )

		self.input_profilNomor = wx.TextCtrl( self.panel_profil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.input_profilNomor.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer4.Add( self.input_profilNomor, 0, wx.ALL, 5 )

		self.input_profilUsername = wx.TextCtrl( self.panel_profil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.input_profilUsername.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer4.Add( self.input_profilUsername, 0, wx.ALL, 5 )

		self.text_profilKota = wx.StaticText( self.panel_profil, wx.ID_ANY, u"Kota Asal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_profilKota.Wrap( -1 )

		self.text_profilKota.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer4.Add( self.text_profilKota, 0, wx.ALL, 5 )

		self.text_profilPassword = wx.StaticText( self.panel_profil, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_profilPassword.Wrap( -1 )

		self.text_profilPassword.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer4.Add( self.text_profilPassword, 0, wx.ALL, 5 )

		self.input_profilKota = wx.TextCtrl( self.panel_profil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.input_profilKota.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer4.Add( self.input_profilKota, 0, wx.ALL, 5 )

		self.input_profilPassword = wx.TextCtrl( self.panel_profil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.input_profilPassword.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer4.Add( self.input_profilPassword, 0, wx.ALL, 5 )


		self.panel_profil.SetSizer( gSizer4 )
		self.panel_profil.Layout()
		gSizer4.Fit( self.panel_profil )
		self.panel_home1.AddPage( self.panel_profil, u"Profil Saya", False )

		bSizer3.Add( self.panel_home1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout )
		self.btn_beli.Bind( wx.EVT_BUTTON, self.BeliTiket )
		self.btn_cariBatal.Bind( wx.EVT_BUTTON, self.CariIdBatal )
		self.btn_batalkan.Bind( wx.EVT_BUTTON, self.Batalkan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout( self, event ):
		event.Skip()

	def BeliTiket( self, event ):
		event.Skip()

	def CariIdBatal( self, event ):
		event.Skip()

	def Batalkan( self, event ):
		event.Skip()


###########################################################################
## Class panel_regis
###########################################################################

class panel_regis ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 248, 146, 230 ) )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.textRegister = wx.StaticText( self, wx.ID_ANY, u"REGISTER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textRegister.Wrap( -1 )

		self.textRegister.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.textRegister, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.text_namaLengkap = wx.StaticText( self, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_namaLengkap.Wrap( -1 )

		self.text_namaLengkap.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.text_namaLengkap, 0, wx.ALL, 5 )

		self.input_namaLengkap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_namaLengkap.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.input_namaLengkap, 0, wx.ALL, 5 )

		self.text_jenisKelamin = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_jenisKelamin.Wrap( -1 )

		self.text_jenisKelamin.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.text_jenisKelamin, 0, wx.ALL, 5 )

		input_kelaminChoices = [ u"Pria", u"Wanita" ]
		self.input_kelamin = wx.ComboBox( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.Size( 350,-1 ), input_kelaminChoices, 0 )
		self.input_kelamin.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.input_kelamin, 0, wx.ALL, 5 )

		self.text_nomortelepon = wx.StaticText( self, wx.ID_ANY, u"Nomor Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_nomortelepon.Wrap( -1 )

		self.text_nomortelepon.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.text_nomortelepon, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.m_textCtrl19.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer2.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.text_kota = wx.StaticText( self, wx.ID_ANY, u"Kota Asal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_kota.Wrap( -1 )

		self.text_kota.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.text_kota, 0, wx.ALL, 5 )

		self.input_kota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_kota.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer2.Add( self.input_kota, 0, wx.ALL, 5 )

		self.text_email = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_email.Wrap( -1 )

		self.text_email.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.text_email, 0, wx.ALL, 5 )

		self.input_email = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_email.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer2.Add( self.input_email, 0, wx.ALL, 5 )

		self.text_username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_username.Wrap( -1 )

		self.text_username.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.text_username, 0, wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_username.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer2.Add( self.input_username, 0, wx.ALL, 5 )

		self.text_password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_password.Wrap( -1 )

		self.text_password.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.text_password, 0, wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.input_password.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		gSizer2.Add( self.input_password, 0, wx.ALL, 5 )

		self.btn_register = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_register.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "COCOGOOSE" ) )

		gSizer2.Add( self.btn_register, 0, wx.ALL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		# Connect Events
		self.btn_register.Bind( wx.EVT_BUTTON, self.Register )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Register( self, event ):
		event.Skip()


