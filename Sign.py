from database import connection
import hashlib


c = connection.cursor()

def SignUp (st) :
    st.sidebar.subheader(" Create A New Account ")
    new_user = st.sidebar.text_input('Username')
    ID = st.sidebar.number_input(label = "Enter Student ID",step = 1, value = 0)
    new_passwd = st.sidebar.text_input('Password',type = 'password')
    if st.sidebar.button('SignUp'):

        query = "SELECT COUNT(*) FROM Users WHERE ID =%s "
        c.execute(query,(ID,))
        result = c.fetchall()
        count=result[0][0]
        if count == 0:

            query = 'INSERT INTO Users(user_name ,ID, passwd) VALUES (%s, %s, %s)'
            c.execute(query,(new_user,ID,make_hashes(new_passwd)))
            connection.commit()
            st.success("You have successfully created an account.")
            st.info("Go to the SignIn Menu to login")
        
        else :
           return st.error("This ID is already used !")
        

        # encrypt or hash the passwd to make it more secure
        # + store the hashed/encrypted password to the database not the plaintext password

def make_hashes(new_passwd):
    return hashlib.sha256(str.encode(new_passwd)).hexdigest()


def check_hashes(passwd,hashed_pswd):
	if make_hashes(passwd) == hashed_pswd:
		return hashed_pswd
	return False

def login_user(st,username,password,ID):
    query = 'SELECT COUNT(*) FROM users WHERE user_name = %s AND passwd = %s AND ID = %s '
    c.execute(query,(username,password,ID))
    result = c.fetchall()
    count=result[0][0]
    if count == 0:
        return False
    else:
        return True
