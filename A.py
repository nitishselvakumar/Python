import xml.etree.ElementTree as xml

booking = xml.Element('booking')
from_text = xml.SubElement(booking, 'from')
from_text.text = 'Mumbai'
to = xml.SubElement(booking, 'to')
to.text = 'Chennai'
triptype = xml.SubElement(booking, 'tripType')
triptype.text = 'round-trip'
fromdate = xml.SubElement(booking, 'fromDate')
fromdate.text = '10-06-2020'
returndate = xml.SubElement(booking, 'returnDate')
returndate.text = '12-06-2020'
flightno = xml.SubElement(booking, 'flightNo')
flightno.text = 'AA5623'
passenger_details = xml.SubElement(booking, 'passengerDetails')
name = xml.SubElement(passenger_details, 'name')
name.text = 'Nitish'
dob = xml.SubElement(passenger_details, 'dob')
dob.text = '01-11-1996'
address = xml.SubElement(passenger_details, 'address')
street_name = xml.SubElement(address, 'streetName')
street_name.text = '200 Feet radial road'
city_name = xml.SubElement(address, 'cityName')
city_name.text = 'pallikaranai'
district_name = xml.SubElement(address, 'districtName')
district_name.text = 'chennai'
state_name = xml.SubElement(address, 'stateName')
state_name.text = 'Tamil Nadu'
Country = xml.SubElement(address, 'Country')
Country.text = 'India'
communication_details = xml.SubElement(address, 'communicationDetails')
phone = xml.SubElement(communication_details, 'phone')
mobile_no = xml.SubElement(phone, 'mobileNo')
mobile_no.text = '8056592150'
landline_no = xml.SubElement(phone, 'landlineNo')
landline_no.text = '04321-234267'
email = xml.SubElement(communication_details, 'email')
personal = xml.SubElement(email, 'personal')
personal.text = 'nitish@gmail.com'
official = xml.SubElement(email, 'official')
official.text = 'nitishgreens@gmail.com'
payment_details = xml.SubElement(booking, 'paymentDetails')
card_name = xml.SubElement(payment_details, 'cardName')
card_name.text = 'VISA'
card_holder_name = xml.SubElement(payment_details, 'cardHolderName')
card_holder_name.text = 'NITISH S'
card_no = xml.SubElement(payment_details, 'cardNo')
card_no.text = '1234567890123456'
cvv_no = xml.SubElement(payment_details, 'cvvNo')
cvv_no.text = '563'
booking = xml.tostring(booking)
file = open("booking.xml", "wb")
file.write(booking)
print("done......")
