import xml.etree.ElementTree as xml

parse = xml.parse(r"C:\Users\k_sur\PycharmProjects\Api\Tickets")
getroot = parse.getroot()
for x in getroot.findall('pnr'):
    from_text = x.find('from').text
    to_text = x.find('to').text
    print("From:" + from_text + "   " + "To:" + to_text)
    trip_type = x.find('tripType').text
    print("Triptype:" + trip_type)
    from_date = x.find('fromDate').text
    return_date = x.find('returnDate').text
    print("From Date:" + from_date + "   " + "Return Date:" + return_date)
    flight_no = x.find('flightNo').text
    print("Flight Number:" + flight_no)
    passenger_details = x.find('passengerDetails')
    name = passenger_details.find('name').text
    dob = passenger_details.find('dob').text
    print("Name:" + name)
    print("Date Of Birth:" + dob)
    address = passenger_details.find('address')
    street_name = address.find('streetName').text
    city_name = address.find('cityName').text
    district_name = address.find('districtName').text
    state_name = address.find('stateName').text
    country_name = address.find('Country').text
    print(
        "Residential Address:" + street_name + "," + city_name + "," + district_name + "," + state_name + "," + country_name)
    communication_details = address.find('communicationDetails')
    phone = communication_details.find('phone')
    mobile_no = phone.find('mobileNo').text
    landline_no = phone.find('landlineNo').text
    print("Mobile Number:" + mobile_no + "," + "Landline Number:" + landline_no)
    email = communication_details.find('email')
    personal_email = email.find('personal').text
    official_email = email.find('official').text
    print("Personal Email:" + personal_email + "," + "Official Email:" + official_email)
    payment_details = x.find('paymentDetails')
    card_name = payment_details.find('cardName').text
    card_holder_name = payment_details.find('cardHolderName').text
    card_no = payment_details.find('cardNo').text
    cvv_no = payment_details.find('cvvNo').text
    print(
        "Card Name:" + card_name + "\n" + "Card Holder Name:" + card_holder_name + "\n" + "Card Number" + card_no + "\n" + "CVV Number:" + cvv_no)
    print("------------------------------------------------------------------------------------")
