import xml.etree.ElementTree as xml

parse = xml.parse(r"C:\Users\k_sur\PycharmProjects\Api\Ticket")
getroot = parse.getroot()
print("from:" + getroot[0].text)
print("to:" + getroot[1].text)
print("trip type is:" + getroot[2].text)
print("from date:" + getroot[3].text)
print("return date:" + getroot[4].text)
print("return date:" + getroot[5].text)
print("*************Passenger Details*************")
print("passenger name:" + getroot[6][0].text)
print("passenger dob:" + getroot[6][1].text)
print("*************Passenger Address*************")
print("street name:" + getroot[6][2][0].text)
print("city name:" + getroot[6][2][1].text)
print("district name:" + getroot[6][2][2].text)
print("state name:" + getroot[6][2][3].text)
print("country name:" + getroot[6][2][4].text)
print("*************Communication Details*************")
print("phone:" + getroot[6][2][5][0][0].text)
print("land line:" + getroot[6][2][5][0][1].text)
print("personal email:" + getroot[6][2][5][1][0].text)
print("official email:" + getroot[6][2][5][1][1].text)
print("*************Payment Details*************")
print("card name:" + getroot[7][0].text)
print("card holder name:" + getroot[7][1].text)
print("card number:" + getroot[7][2].text)
print("cvv number:" + getroot[7][3].text)
