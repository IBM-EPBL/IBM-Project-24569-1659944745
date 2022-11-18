import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.clogj3sd@tgtulqde00.databases.appdomain.cloud;PORT=32459;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=fsd29379;PWD=SCnrYPTDuCpOSGc0;","","")
print("connection successfully")


sql="""CREATE TABLE login (
    Name varchar(255),
    Email varchar(255),
    Password varchar(255) )"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)

sql="""CREATE TABLE Customerdetails (
    Name varchar(255),
    ShopName varchar(255),
    Location varchar(255),
    MobileNumber varchar(255) )"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)


"""{% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, messages in messages %}
          <div class="alert alert-{{category}}" ></div>{{messages}}</div>
        {% endfor %}
  {% endif %}  
  {% endwith %} """
