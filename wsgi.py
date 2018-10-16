from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    kid = raw_input('KID : ')
	db = raw_input('Rekening Pengirim : ')
	cr = raw_input('Rekening Penerima : ')
	amount = raw_input('Jumlah : ')

	url1 = 'http://baronang.com/test/test1.php'
	data = {'kid': kid, 'db': db, 'cr': cr, 'amount': amount}
	res = requests.get(url1, params=data, stream=True)

	data = json.loads(res.text)
	db_name = data['db_name']
	db_bal = float(data['db_bal'])
	cr_name = data['cr_name']
	cr_bal = float(data['cr_bal'])
	amt = float(amount)

	print 'Nama Pengirim : ', db_name[0]
	print 'Saldo : Rp. ', '{0:,.2f}'.format(db_bal)
	print 'Nama Penerima : ', cr_name[0]
	print 'Saldo : Rp. ', '{0:,.2f}'.format(cr_bal)
	print 'Jumlah Transfer : Rp. ', '{0:,.2f}'.format(amt)

if __name__ == "__main__":
    application.run()
