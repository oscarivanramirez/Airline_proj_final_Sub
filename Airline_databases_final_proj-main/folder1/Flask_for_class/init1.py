#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
from random import randint

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
					   port=8889,
                       user='root',
                       password='root',
                       db='travel',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
	return render_template('index.html')

#Define route for login
@app.route('/login')
def login():
	return render_template('login.html')

#Define route for register
@app.route('/register')
def register():
	return render_template('register.html')

#BEG OF CUSTOMERS

@app.route('/defaultFlightsCus',methods=['GET','POST'])
def defaultFlightsCus():
    cursor=conn.cursor()
    email=session['email']
	#'SELECT * FROM Booking_Agent, Purchase_by_BA WHERE BA_email=email and email=%s'
    query='SELECT * FROM Ticket NATURAL JOIN Purchase_by_Customer WHERE customer_email=%s and depart_date>CURDATE() and depart_time>CURTIME()'
    cursor.execute(query, (email))
    data2 = cursor.fetchall()
    cursor.close()
    return render_template('customerUse.html',purchasedCus=data2)

@app.route('/searchingFlightsCus', methods=['GET', 'POST'])
def searchingFlightsCus():
    #This is for status
    '''Search for future flights based on source city/airport name, destination city/airport name,
departure date for one way (departure and return dates for round trip).'''
    soci_airpoN=request.form['soci_airpoN']
    desci_airpoN=request.form['desci_airpoN']
    depart_date=request.form['depart_date']
    return_date=request.form['return_date']
    print(soci_airpoN,'soci_airpoN') 
    first=False
    two=False
    third=False
    four=False
    data2=None
    data3=None
    data4=None
    data5=None
    data6=None
    data7=None
    #check if it has return date
    if(return_date==''):
        print('im in')
        frist=True
        two=True
    else:
        third=True
        four=True
	
    #checks if it is airport or city
    



	#4 different kinds of queries 

	#query to return results for one way between cities
    
    cursor = conn.cursor()
    if(first):
        #SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city='Shanghai' and Aport_arr.city='NYC' and Aport_dep.airport_name=airport_name_depart and
		#Aport_arr.airport_name=airport_name_arrival and depart_date='2021-03-31'
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data2 = cursor.fetchall()
    print(data2,'firstttttt')
    cursor.close()

	#query to return resutls for one way between airports
    cursor = conn.cursor()
    if(two):
    	#WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s
		#soci_airpoN,desci_airpoN,depart_date
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data3 = cursor.fetchall()
        print(data3,'twoooooo')
    cursor.close()

	#query to return results for two way between cities
    cursor = conn.cursor()
    if(third):
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data4 = cursor.fetchall()
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date))
	    #stores the results in a variable
        data5 = cursor.fetchall()
    print(data4)
    print(data5)
    cursor.close()

	#query to return results for two way between airports
    cursor = conn.cursor()
    if(four):
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data6 = cursor.fetchall()
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date))
	    #stores the results in a variable
        data7 = cursor.fetchall()
    print(data6)
    print(data7)
    cursor.close()
    if(data2):
        return render_template('customerUse.html',data2=data2,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data3):
        return render_template('customerUse.html',data3=data3,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data4 and data5):
        return render_template('customerUse.html',data4=data4,data5=data5,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    elif(data6 and data7):
        return render_template('customerUse.html',data6=data6,data7=data7,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    else:
        return render_template('customerUse.html',report='NO FLIGHTS')


@app.route('/purchaseAvailability', methods=['GET', 'POST'])
def purchaseAvailability():
    airport_name_depart = request.form['airport_name_depart']
    #airport_name_arrival = request.form['airport_name_arrival']
    depart_date = request.form['depart_date']
    airplaneID = request.form['airplaneID']
    flight_number = request.form['flight_number']
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT * FROM Flight WHERE airplane_ID=%s and airport_name_depart = %s and depart_date=%s and flight_number=%s'
    cursor.execute(query,(airplaneID, airport_name_depart, depart_date,flight_number))
    flightA = cursor.fetchone()
    #print(airplaneID,'yoooooooooo44444')
    #ticket_ID = request.form['ticket_ID']
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT seats FROM Airplane WHERE airplane_ID=%s'
    cursor.execute(query,(airplaneID))
    data2 = cursor.fetchone()
	#tickets
    query = 'SELECT count(flight_number) as num_tick FROM Ticket WHERE flight_number=%s GROUP by flight_number'
    cursor.execute(query,(flight_number))
    data3 = cursor.fetchone()
    query = 'SELECT base_price FROM Flight WHERE flight_number=%s'
    cursor.execute(query,(flight_number))
    data4 = cursor.fetchone()
    cursor.close()
    print(data2['seats'],'seatsssssssss')
    print(data3,'tickeettststst')
    if(data3==None):
        num_tickets=0
    else:
        num_tickets=data3['num_tick']
    seats=data2['seats']
    print(num_tickets,'tickeettststst')
    base_price=data4['base_price']
    msg1='SOLD OUT'
    if(num_tickets==seats):
        return render_template('customerUse.html',msg=msg1)
    elif(num_tickets/seats>.7):
        price1=.2*base_price
        return render_template('customerUse.html',msg='Price has gone up due to high demand',price=price1,flightA=flightA,dummy='secure')
    else:
        return render_template('customerUse.html',msg='Price is the base price',price=base_price,flightA=flightA,dummy='secure')
	#if(not enough seats) return sold out
	#ask to fill out credit card info
	#else make ticket <- have a function

@app.route('/purchaseTicket', methods=['GET', 'POST'])
def purchaseTicket():
	#ticket_id 
	#ticket attributes
	#airline_name,airplane_ID,flight_number,depart_time,depart_date,ticket_ID,sold_price,airport_name_arrival, airport_name_depart
	#purchase_date,purchase_time,card_type,card_name,card_expiration,card_num
    ticketList=[]
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT ticket_ID FROM ticket'
    cursor.execute(query,())
    data2 = cursor.fetchall()
    cursor.close()
    for i in range(len(data2)):
        ticketList.append(list(data2[i].values())[0])
    print(ticketList,'tickettetLISTTTT')
	#first ticket_id 
    rangeStart = 10**(6-1)
    rangeEnd = (10**6)-1
    num = randint(rangeStart, rangeEnd)
    while num in ticketList:
        num = randint(rangeStart, rangeEnd)
    ticket_ID=num
	# then make ticket
    customer_email = session['email']
    airline_name=request.form['airline_name']
    airplane_ID=request.form['airplaneID']
    flight_number=request.form['flight_number']
    depart_time=request.form['depart_time']
    print(depart_time,'departttt timeee')
    depart_date=request.form['depart_date']
    sold_price=request.form['sold_price']
    airport_name_arrival=request.form['airport_name_arrival']
    airport_name_depart=request.form['airport_name_depart']
    card_type=request.form['card_type']
    card_name=request.form['card_name']
    card_expiration=request.form['card_expiration']
    card_num=request.form['card_num']
    cursor=conn.cursor()
    query = 'INSERT into Ticket(airline_name, airplane_ID,flight_number,depart_time,depart_date,ticket_ID,sold_price,airport_name_arrival,airport_name_depart,\
    purchase_date,purchase_time,card_type,card_name,card_expiration,card_num) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,CURDATE(),CURTIME(),%s,%s,%s,%s)'
    cursor.execute(query,(airline_name,airplane_ID,flight_number,depart_time,depart_date,ticket_ID,sold_price,airport_name_arrival,airport_name_depart,card_type,card_name,card_expiration,card_num))
    conn.commit()  
    cursor.close()
	#then add to purchase_by customer
	#then add to feedback

    cursor=conn.cursor()
    query = 'INSERT into Purchase_by_Customer (customer_email, ticket_ID)values (%s,%s)'
    cursor.execute(query,(customer_email,ticket_ID))
    conn.commit()  
    cursor.close()
    cursor=conn.cursor()
    query = 'INSERT into Feedback (airline_name, airplane_ID, flight_number, depart_time, depart_date, email, airport_name_arrival, airport_name_depart)values (%s, %s, %s, %s, %s, %s, %s,%s)'
    cursor.execute(query, (airline_name, airplane_ID, flight_number, depart_time, depart_date, customer_email, airport_name_arrival, airport_name_depart))
    conn.commit()
    cursor.close()
    return render_template('customerUse.html',ticket_ID=ticket_ID, success='success')


@app.route('/trackSpendingDefault_Cus', methods=['GET', 'POST'])
def trackSpendingDefault_Cus():
    customer_email = session['email']
    cursor = conn.cursor()
	#and purchase_date BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE()
	#SELECT sum(sold_price) FROM Ticket NATURAL JOIN Purchase_by_Customer WHERE customer_email='oir209@nyu.edu' GROUP by customer_email
	#SELECT sum(sold_price) as total_spent,customer_email FROM Purchase_by_Customer NATURAL JOIN Ticket WHERE customer_email='oir209@nyu.edu' AND purchase_date > CURDATE()- INTERVAL 1 YEAR AND purchase_date < CURDATE() GROUP by customer_email
    query = 'SELECT sum(sold_price) as total_spent FROM Purchase_by_Customer NATURAL JOIN Ticket WHERE customer_email=%s AND purchase_date > CURDATE()- INTERVAL 1 YEAR AND purchase_date < CURDATE() GROUP by customer_email'
    cursor.execute(query, (customer_email))
    trackSpendDef = cursor.fetchone() 
    print(trackSpendDef['total_spent'])
    total_spent=trackSpendDef['total_spent']
    cursor.close()
    '''
    cursor = conn.cursor()
    query = 'SELECT sum(sold_price) as total_spent, month(purchase_date) FROM Purchase_by_Customer NATURAL JOIN Ticket WHERE customer_email=%s AND purchase_date > CURDATE()- INTERVAL 6 Month AND purchase_date < CURDATE() GROUP by customer_email,month(purchase_date)'
    cursor.execute(query, (customer_email))
    barChartD = cursor.fetchone() 
    print(trackSpendDef['total_spent'])
    total_spent=trackSpendDef['total_spent']
    cursor.close()
    '''
    return render_template('customerUse.html',total_spent=total_spent)

@app.route('/trackSpending_Cus', methods=['GET', 'POST'])
def trackSpending_Cus():
    customer_email = session['email']
    fromDate=request.form['fromDate']
    toDate=request.form['toDate']
    cursor = conn.cursor()
    query = 'SELECT sum(sold_price) as total_spent FROM Purchase_by_Customer NATURAL JOIN Ticket WHERE customer_email=%s AND purchase_date > DATE(%s) AND purchase_date < DATE(%s) GROUP by customer_email'
    cursor.execute(query, (customer_email,fromDate,toDate))
    trackSpend = cursor.fetchone() 
    print(trackSpend)
    cursor.close()
    '''
    cursor = conn.cursor()
    query = 'SELECT sum(sold_price) as total_spent, month(purchase_date) FROM Purchase_by_Customer NATURAL JOIN Ticket WHERE customer_email=%s AND purchase_date > DATE(%s) AND purchase_date < DATE(%s) GROUP by customer_email,month(purchase_date)'
    cursor.execute(query, (customer_email,fromDate,toDate))
    barChart = cursor.fetchall() 
    print(trackSpendDef['total_spent'])
    total_spent=trackSpendDef['total_spent']
    cursor.close()
    '''
    return render_template('customerUse.html',trackSpend=trackSpend['total_spent'],fromDate=fromDate,toDate=toDate)
    
@app.route('/displayLeft_to_Rate',methods=['GET','POST'])
def displayLeft_to_Rate():
    customer_email = session['email']
    cursor=conn.cursor()
    query = 'SELECT * FROM Feedback NATURAL JOIN Flight WHERE comments is NULL and CURDATE()>arrival_date and CURTIME()>arrival_time and email=%s'
    cursor.execute(query, (customer_email))
    flight_no_rate = cursor.fetchall()
    cursor.close()
    return render_template('customerUse.html',flight_no_rate=flight_no_rate)
@app.route('/rateComment', methods=['GET', 'POST'])
def rateComment():
    rating=request.form['rating']
    comment=request.form['comment']
    customer_email = session['email']
    airport_name_depart=request.form['airport_name_depart']
    airport_name_arrival=request.form['airport_name_arrival']
    depart_date=request.form['depart_date']
    flight_number=request.form['flight_number']
    cursor=conn.cursor()
    query = 'UPDATE Feedback SET comments = %s,ratings = %s WHERE flight_number = %s and email=%s and depart_date=%s'
    cursor.execute(query, (flight_number,customer_email,depart_date))
    conn.commit()
    cursor.close()
    return render_template('customerUse.html',postedCom='Success')


# END OF CUSTOMERS


#------------------------------------------------------------------------------------------------------------------------



# BEG INDEX HTML

@app.route('/searchingFlightStatus',methods=['GET','POST'])
def searchingFlightStatus():
	airlineName = request.form['airline_name']
	departDate = request.form['depart_date']
	flightNum = request.form['flight_number']
	cursor = conn.cursor()
	#make a query
	#SELECT * FROM Flight WHERE airlineName = %s and flightNum = %i and departDate = %d 
	query = 'SELECT * FROM Flight WHERE airline_name = %s and flight_number = %s and depart_date = %s'
	cursor.execute(query, (airlineName,flightNum,departDate))
	#stores the results in a variable
	data = cursor.fetchall()
	print(data)
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	return render_template('index.html',dat=data[0]['status_F'],airline_n=airlineName,departD=departDate,flightN=flightNum)


@app.route('/searchingFlights', methods=['GET', 'POST'])
def searchingFlightss():
    #This is for status
    '''Search for future flights based on source city/airport name, destination city/airport name,
departure date for one way (departure and return dates for round trip).'''
    soci_airpoN=request.form['soci_airpoN']
    desci_airpoN=request.form['desci_airpoN']
    depart_date=request.form['depart_date']
    return_date=request.form['return_date']
    print(soci_airpoN,'soci_airpoN') 
    first=False
    two=False
    third=False
    four=False
    data2=None
    data3=None
    data4=None
    data5=None
    data6=None
    data7=None
    #check if it has return date
    if(return_date==''):
        print('im in')
        frist=True
        two=True
    else:
        third=True
        four=True
	
    #checks if it is airport or city
    



	#4 different kinds of queries 

	#query to return results for one way between cities
    
    cursor = conn.cursor()
    if(first):
        #SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city='Shanghai' and Aport_arr.city='NYC' and Aport_dep.airport_name=airport_name_depart and
		#Aport_arr.airport_name=airport_name_arrival and depart_date='2021-03-31'
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data2 = cursor.fetchall()
    print(data2,'firstttttt')
    cursor.close()

	#query to return resutls for one way between airports
    cursor = conn.cursor()
    if(two):
    	#WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s
		#soci_airpoN,desci_airpoN,depart_date
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data3 = cursor.fetchall()
        print(data3,'twoooooo')
    cursor.close()

	#query to return results for two way between cities
    cursor = conn.cursor()
    if(third):
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data4 = cursor.fetchall()
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date))
	    #stores the results in a variable
        data5 = cursor.fetchall()
    print(data4)
    print(data5)
    cursor.close()

	#query to return results for two way between airports
    cursor = conn.cursor()
    if(four):
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data6 = cursor.fetchall()
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date))
	    #stores the results in a variable
        data7 = cursor.fetchall()
    print(data6)
    print(data7)
    cursor.close()
    if(data2):
        return render_template('index.html',data2=data2,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data3):
        return render_template('index.html',data3=data3,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data4 and data5):
        return render_template('index.html',data4=data4,data5=data5,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    elif(data6 and data7):
        return render_template('index.html',data6=data6,data7=data7,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    else:
        return render_template('index.html',report='NO FLIGHTS')
# END INDEX HTML


#------------------------------------------------------------------------------------------------------------------------

#BEG OF BOOKING AGENT

#
@app.route('/defaultFlightsBA',methods=['GET','POST'])
def defaultFlightsBA():
    cursor=conn.cursor()
    BA_email=session['email']
	#'SELECT * FROM Booking_Agent, Purchase_by_BA WHERE BA_email=email and email=%s'
    query='SELECT * FROM (Ticket NATURAL JOIN Purchase_by_BA) ,Booking_Agent WHERE Ticket.booking_agent_ID = Booking_Agent.ID and Purchase_by_BA.BA_email=%s and depart_date>CURDATE() and depart_time>CURTIME()'
    cursor.execute(query, (BA_email))
    data2 = cursor.fetchall()
    cursor.close()
    return render_template('bookingAgentUse.html',purchasedBA=data2)

@app.route('/searchingFlightsBA', methods=['GET', 'POST'])
def searchingFlightsBA():
    #This is for status
    '''Search for future flights based on source city/airport name, destination city/airport name,
departure date for one way (departure and return dates for round trip).'''
    soci_airpoN=request.form['soci_airpoN']
    desci_airpoN=request.form['desci_airpoN']
    depart_date=request.form['depart_date']
    return_date=request.form['return_date']
    print(soci_airpoN,'soci_airpoN') 
    first=False
    two=False
    third=False
    four=False
    data2=None
    data3=None
    data4=None
    data5=None
    data6=None
    data7=None
    #check if it has return date
    if(return_date==''):
        print('im in')
        frist=True
        two=True
    else:
        third=True
        four=True
	
    #checks if it is airport or city
    



	#4 different kinds of queries 

	#query to return results for one way between cities
    
    cursor = conn.cursor()
    if(first):
        #SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city='Shanghai' and Aport_arr.city='NYC' and Aport_dep.airport_name=airport_name_depart and
		#Aport_arr.airport_name=airport_name_arrival and depart_date='2021-03-31'
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=DATE(%s)'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data2 = cursor.fetchall()
        print(data2,'firstttttt')
    cursor.close()

	#query to return resutls for one way between airports
    cursor = conn.cursor()
    if(two):
    	#WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s
		#soci_airpoN,desci_airpoN,depart_date
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=DATE(%s)'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data3 = cursor.fetchall()
        print(data3,'twoooooo')
    cursor.close()

	#query to return results for two way between cities
    cursor = conn.cursor()
    if(third):
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data4 = cursor.fetchall()
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date))
	    #stores the results in a variable
        data5 = cursor.fetchall()
    print(data4)
    print(data5)
    cursor.close()

	#query to return results for two way between airports
    cursor = conn.cursor()
    if(four):
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date))
	    #stores the results in a variable
        data6 = cursor.fetchall()
        query = 'SELECT * FROM Flight WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date))
	    #stores the results in a variable
        data7 = cursor.fetchall()
    print(data6)
    print(data7)
    cursor.close()
    if(data2):
        return render_template('bookingAgentUse.html',data2=data2,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data3):
        return render_template('bookingAgentUse.html',data3=data3,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data4 and data5):
        return render_template('bookingAgentUse.html',data4=data4,data5=data5,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    elif(data6 and data7):
        return render_template('bookingAgentUse.html',data6=data6,data7=data7,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    else:
        return render_template('bookingAgentUse.html',report='NO FLIGHTS')


@app.route('/purchaseAvailability_BA', methods=['GET', 'POST'])
def purchaseAvailability_BA():
    airport_name_depart = request.form['airport_name_depart']
    #airport_name_arrival = request.form['airport_name_arrival']
    depart_date = request.form['depart_date']
    airplaneID = request.form['airplaneID']
    flight_number = request.form['flight_number']
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT * FROM Flight WHERE airplane_ID=%s and airport_name_depart = %s and depart_date=%s and flight_number=%s'
    cursor.execute(query,(airplaneID, airport_name_depart, depart_date,flight_number))
    flightA = cursor.fetchone()
    #print(airplaneID,'yoooooooooo44444')
    #ticket_ID = request.form['ticket_ID']
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT seats FROM Airplane WHERE airplane_ID=%s'
    cursor.execute(query,(airplaneID))
    data2 = cursor.fetchone()
	#tickets
    query = 'SELECT count(flight_number) as num_tick FROM Ticket WHERE flight_number=%s GROUP by flight_number'
    cursor.execute(query,(flight_number))
    data3 = cursor.fetchone()
    query = 'SELECT base_price FROM Flight WHERE flight_number=%s'
    cursor.execute(query,(flight_number))
    data4 = cursor.fetchone()
    cursor.close()
    print(data2['seats'],'seatsssssssss')
    print(data3,'tickeettststst')
    if(data3==None):
        num_tickets=0
    else:
        num_tickets=data3['num_tick']
    seats=data2['seats']
    print(num_tickets,'tickeettststst')
    base_price=data4['base_price']
    msg1='SOLD OUT'
    if(num_tickets==seats):
        return render_template('bookingAgentUse.html',msg=msg1)
    elif(num_tickets/seats>.7):
        price1=.2*base_price
        return render_template('bookingAgentUse.html',msg='Price has gone up due to high demand',price=price1,flightA=flightA,dummy='secure')
    else:
        return render_template('bookingAgentUse.html',msg='Price is the base price',price=base_price,flightA=flightA,dummy='secure')
	#if(not enough seats) return sold out
	#ask to fill out credit card info
	#else make ticket <- have a function

@app.route('/purchaseTicket_BA',methods=['GET','POST'])
def purchaseTicket_BA():
	#ticket_id 
	#ticket attributes
	#airline_name,airplane_ID,flight_number,depart_time,depart_date,ticket_ID,sold_price,airport_name_arrival, airport_name_depart
	#purchase_date,purchase_time,card_type,card_name,card_expiration,card_num
    ticketList=[]
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT ticket_ID FROM ticket'
    cursor.execute(query,())
    data2 = cursor.fetchall()
    cursor.close()
    for i in range(len(data2)):
        ticketList.append(list(data2[i].values())[0])
    print(ticketList,'tickettetLISTTTT')
	#first ticket_id 
    rangeStart = 10**(6-1)
    rangeEnd = (10**6)-1
    num = randint(rangeStart, rangeEnd)
    while num in ticketList:
        num = randint(rangeStart, rangeEnd)
    ticket_ID=num
	# then make ticket
	#NEED TO FIND BOOKING AGENT ID
    BA_email = session['email']
    cursor=conn.cursor()
    query = 'SELECT ID as booking_agent_ID FROM Booking_Agent where email=%s'
    cursor.execute(query,(BA_email))
    data2 = cursor.fetchone()
    print(data2['booking_agent_ID'],'booking agent')
    booking_agent_ID=data2['booking_agent_ID']
    cursor.close()
    customer_email=request.form['customer_email']
    airline_name=request.form['airline_name']
    airplane_ID=request.form['airplaneID']
    flight_number=request.form['flight_number']
    depart_time=request.form['depart_time']
    print(depart_time,'departttt timeee')
    depart_date=request.form['depart_date']
    sold_price=request.form['sold_price']
    airport_name_arrival=request.form['airport_name_arrival']
    airport_name_depart=request.form['airport_name_depart']
    card_type=request.form['card_type']
    card_name=request.form['card_name']
    card_expiration=request.form['card_expiration']
    card_num=request.form['card_num']
    cursor=conn.cursor()
    query = 'INSERT into Ticket(airline_name, airplane_ID,flight_number,depart_time,depart_date,ticket_ID,sold_price,airport_name_arrival,airport_name_depart,\
    purchase_date,purchase_time,card_type,card_name,card_expiration,card_num,booking_agent_ID) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,CURDATE(),CURTIME(),%s,%s,%s,%s,%s)'
    cursor.execute(query,(airline_name,airplane_ID,flight_number,depart_time,depart_date,ticket_ID,sold_price,airport_name_arrival,airport_name_depart,card_type,card_name,card_expiration,card_num,booking_agent_ID))
    conn.commit()  
    cursor.close()
	#then add to purchase_by booking agent
	#then add to feedback

    cursor=conn.cursor()
    query = 'INSERT into Purchase_by_BA (customer_email, BA_email ,ticket_ID)values (%s,%s,%s)'
    cursor.execute(query,(customer_email,BA_email,ticket_ID))
    conn.commit()  
    cursor.close()
    cursor=conn.cursor()
    query = 'INSERT into Feedback (airline_name, airplane_ID, flight_number, depart_time, depart_date, email, airport_name_arrival, airport_name_depart)values (%s, %s, %s, %s, %s, %s, %s,%s)'
    cursor.execute(query, (airline_name, airplane_ID, flight_number, depart_time, depart_date, customer_email, airport_name_arrival, airport_name_depart))
    conn.commit()
    cursor.close()
    return render_template('bookingAgentUse.html',ticket_ID=ticket_ID,success='success')



@app.route('/defaultCommissionT',methods=['GET','POST'])
def defaultCommissionT():
    '''
	Default view will be total amount of commission received in the past 30 days
			and the average commission he/she received per ticket booked in the past 30 days and total
			number of tickets sold by him in the past 30 day'''
    total_Comm=0
    avg_Comm=0
    email=session['email']
    cursor=conn.cursor()
	#SELECT sum(sold_price) FROM (Ticket NATURAL JOIN Purchase_by_BA), Booking_Agent WHERE email=BA_email
    query='SELECT sum(sold_price) FROM (Ticket NATURAL JOIN Purchase_by_BA), Booking_Agent WHERE email=BA_email and email=%s'
    cursor.execute(query, (email))
    data2 = cursor.fetchall()
    cursor.close()
    cursor=conn.cursor()
	#SELECT sum(sold_price) FROM (Ticket NATURAL JOIN Purchase_by_BA), Booking_Agent WHERE email=BA_email
    query='SELECT commission FROM Booking_Agent WHERE email=%s'
    cursor.execute(query, (email))
    data3 = cursor.fetchall()
    cursor.close()
    total_Comm=data2['sum(sold_price)']*data3['commission']
    #the average commission he/she received per ticket booked in the past 30 days
    cursor=conn.cursor()
    query='SELECT count(ticket_ID) FROM (Ticket NATURAL JOIN Purchase_by_BA), Booking_Agent WHERE email=BA_email and email=%s'
    cursor.execute(query, (email))
    data4 = cursor.fetchall()
    cursor.close()
    avg_Comm=total_Comm/data4['count(ticket_ID)']
	#and total number of tickets sold by him in the past 30 day
    cursor=conn.cursor()
    query='SELECT sum(ticket_ID) FROM (Ticket NATURAL JOIN Purchase_by_BA), Booking_Agent WHERE email=BA_email and email=%s'
    cursor.execute(query, ())
    data5 = cursor.fetchall()
    cursor.close()
    return render_template('bookingAgentUse.html',totalComm=total_Comm,avgCom=avg_Comm,totalTick=data5['sum(ticket_ID)'])

@app.route('/SearchingCommission',methods=['GET','POST'])
def SearchingCommission():
    fromDate=request.form['fromDate']
    toDate=request.form['toDate']
    email=session['email']
    cursor=conn.cursor()
	#sum of sold prices
    query='SELECT sum(sold_price) FROM (Ticket NATURAL JOIN Purchase_by_BA), Booking_Agent WHERE email=BA_email and email=%s and purchase_date<DATE(%s) and purchase_date>DATE(%s)'
    cursor.execute(query, (email,toDate,fromDate))
    data2 = cursor.fetchall()
    cursor.close()
    cursor=conn.cursor()
	#finding commissions
    query='SELECT commission FROM Booking_Agent WHERE email=%s'
    cursor.execute(query, (email))
    data3 = cursor.fetchall()
    cursor.close()
	#finding total # of tickets sold
    cursor=conn.cursor()
    query='SELECT sum(ticket_ID) FROM (Ticket NATURAL JOIN Purchase_by_BA), Booking_Agent WHERE email=BA_email and email=%s and purchase_date<DATE(%s) and purchase_date>DATE(%s)'
    cursor.execute(query, (email,toDate,fromDate))
    data5 = cursor.fetchall()
    cursor.close()    
    total_Comm=data2['sum(sold_price)']*data3['commission']
    return render_template('bookingAgentUse.html',totalComm=total_Comm,totalTick=data5['sum(ticket_ID)']) 


#View top customers

@app.route('/topCustomers',methods=['GET','POST'])
def topCustomers():
    ''': Top 5 customers based on number of tickets bought from the booking agent in
	the past 6 months and top 5 customers based on amount of commission received in the last year'''
    email=session['email']
    cursor=conn.cursor()
	#sum of sold prices
	#last 6 months
    query='SELECT customer_email,count(customer_email) as count_cust_email FROM Ticket NATURAL JOIN Purchase_by_BA WHERE email=%s GROUP BY customer_email ORDER BY count(customer_email) DESC LIMIT 5'
    cursor.execute(query, (email))
    top5tick = cursor.fetchall()
    cursor.close()
    cursor=conn.cursor()
	#sum of sold prices
	#last 6 months
	#commission
	#SELECT dept_name,sum(salary)as s FROM instructor GROUP BY dept_name ORDER BY s DESC LIMIT 5
    query='SELECT customer_email,sum(sold_price) as count_cust_email FROM Ticket NATURAL JOIN Purchase_by_BA WHERE email=%s GROUP BY customer_email ORDER BY count(customer_email) DESC LIMIT 5'
    cursor.execute(query, (email))
    top5Com = cursor.fetchall()
    cursor.close()
    return render_template('bookingAgentUse.html',top5Com=top5Com,top5tick=top5tick)



#END OF BOOKING AGENT 


#------------------------------------------------------------------------------------------------------------------------

#BEG OF STAFF 

@app.route('/defaultFlights_Staff',methods=['GET','POST'])
def defaultFlights_Staff():
    username=session['email']
    cursor=conn.cursor()
	#'SELECT * FROM Booking_Agent, Purchase_by_BA WHERE BA_email=email and email=%s'
    query='SELECT * FROM Staff NATURAL JOIN Flights Where username=%s and depart_date>CURDATE()'
    cursor.execute(query, (username))
    data2 = cursor.fetchall()
    cursor.close()
    return render_template('airline_staff.html',airline_Flights=data2)

@app.route('/searchingFlights_Staff', methods=['GET', 'POST'])
def searchingFlights_Staff():
    username=session['email']
    soci_airpoN=request.form['soci_airpoN']
    desci_airpoN=request.form['desci_airpoN']
    depart_date=request.form['depart_date']
    return_date=request.form['return_date']
    print(soci_airpoN,'soci_airpoN') 
    first=False
    two=False
    third=False
    four=False
    data2=None
    data3=None
    data4=None
    data5=None
    data6=None
    data7=None
    #check if it has return date
    if(return_date==''):
        print('im in')
        frist=True
        two=True
    else:
        third=True
        four=True
	
    #checks if it is airport or city
	#4 different kinds of queries 

	#query to return results for one way between cities
    
    cursor = conn.cursor()
    if(first):
        #SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight WHERE Aport_dep.city='Shanghai' and Aport_arr.city='NYC' and Aport_dep.airport_name=airport_name_depart and
		#Aport_arr.airport_name=airport_name_arrival and depart_date='2021-03-31'
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight,Staff WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s and Staff.airline_name=Flight.airline_name and Staff.username=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date,username))
	    #stores the results in a variable
        data2 = cursor.fetchall()
    print(data2,'firstttttt')
    cursor.close()

	#query to return resutls for one way between airports
    cursor = conn.cursor()
    if(two):
    	#WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s
		#soci_airpoN,desci_airpoN,depart_date
        query = 'SELECT * FROM Flight NATURAL JOIN Staff WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s and username=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date,username))
	    #stores the results in a variable
        data3 = cursor.fetchall()
        print(data3,'twoooooo')
    cursor.close()

	#query to return results for two way between cities
    cursor = conn.cursor()
    if(third):
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight,Staff WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s and Staff.airline_name=Flight.airline_name and Staff.username=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date,username))
	    #stores the results in a variable
        data4 = cursor.fetchall()
        query = 'SELECT * FROM Airport as Aport_dep, Airport as Aport_arr, Flight,Staff WHERE Aport_dep.city=%s and Aport_arr.city=%s \
	    and Aport_dep.airport_name=airport_name_depart and Aport_arr.airport_name=airport_name_arrival and depart_date=%s and Staff.airline_name=Flight.airline_name and Staff.username=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date,username))
	    #stores the results in a variable
        data5 = cursor.fetchall()
    print(data4)
    print(data5)
    cursor.close()

	#query to return results for two way between airports
    cursor = conn.cursor()
    if(four):
        query = 'SELECT * FROM Flight NATURAL JOIN Staff WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s and username=%s'
        cursor.execute(query, (soci_airpoN,desci_airpoN,depart_date,username))
	    #stores the results in a variable
        data6 = cursor.fetchall()
        query = 'SELECT * FROM Flight NATURAL JOIN Staff WHERE airport_name_depart=%s and airport_name_arrival=%s and depart_date=%s and username=%s'
        cursor.execute(query, (desci_airpoN,soci_airpoN,return_date,username))
	    #stores the results in a variable
        data7 = cursor.fetchall()
    print(data6)
    print(data7)
    cursor.close()
    if(data2):
        return render_template('airline_staff.html',data2=data2,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data3):
        return render_template('airline_staff.html',data3=data3,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date)
    elif(data4 and data5):
        return render_template('airline_staff.html',data4=data4,data5=data5,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    elif(data6 and data7):
        return render_template('airline_staff.html',data6=data6,data7=data7,soci_airpoN=soci_airpoN,desci_airpoN=desci_airpoN,depart_date=depart_date,return_date=return_date)
    else:
        return render_template('airline_staff.html',report='NO FLIGHTS')
'''

@app.route('/purchaseAvailability_BA', methods=['GET', 'POST'])
def purchaseAvailability_BA():
    airport_name_depart = request.form['airport_name_depart']
    #airport_name_arrival = request.form['airport_name_arrival']
    depart_date = request.form['depart_date']
    airplaneID = request.form['airplaneID']
    flight_number = request.form['flight_number']
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT * FROM Flight WHERE airplane_ID=%s and airport_name_depart = %s and depart_date=%s and flight_number=%s'
    cursor.execute(query,(airplaneID, airport_name_depart, depart_date,flight_number))
    flightA = cursor.fetchone()
    #print(airplaneID,'yoooooooooo44444')
    #ticket_ID = request.form['ticket_ID']
    cursor=conn.cursor()
	#first check how many seats
	#seats
    query = 'SELECT seats FROM Airplane WHERE airplane_ID=%s'
    cursor.execute(query,(airplaneID))
    data2 = cursor.fetchone()
	#tickets
    query = 'SELECT count(flight_number) as num_tick FROM Ticket WHERE flight_number=%s GROUP by flight_number'
    cursor.execute(query,(flight_number))
    data3 = cursor.fetchone()
    query = 'SELECT base_price FROM Flight WHERE flight_number=%s'
    cursor.execute(query,(flight_number))
    data4 = cursor.fetchone()
    cursor.close()
    print(data2['seats'],'seatsssssssss')
    print(data3['num_tick'],'tickeettststst')
    seats=data2['seats']
    num_tickets=data3['num_tick']
    base_price=data4['base_price']
    msg1='SOLD OUT'
    if(num_tickets==seats):
        return render_template('bookingAgentUse.html',msg=msg1)
    elif(num_tickets/seats>.7):
        price1=.2*base_price
        return render_template('bookingAgentUse.html',msg='Price has gone up due to high demand',price=price1,flightA=flightA)
    else:
        return render_template('bookingAgentUse.html',msg='Price is the base price',price=base_price,flightA=flightA)
	#if(not enough seats) return sold out
	#ask to fill out credit card info
	#else make ticket <- have a function

'''
#flightRatings
@app.route('/flightRatings_staff', methods=['GET', 'POST'])
def flightRatings_staff():
    email=session['email']
    '''
    cursor = conn.cursor()
    query = 'SELECT * FROM Feedback NATURAL JOIN Staff WHERE username=%s'
    cursor.execute(query, (email))
	#stores the results in a variable
    data2 = cursor.fetchall()
    print(data2)
    cursor.close()
	#make a query
	#WHERE depart_date < CURDATE() + INTERVAL 30 DAY and CURDATE() < depart_date'
    '''
    query = 'SELECT airline_name FROM Staff WHERE username=%s'
    cursor.execute(query, (email))
	#stores the results in a variable
    data2 = cursor.fetchone()
    print(data2)
    cursor.close()
    cursor = conn.cursor()
    query = 'SELECT flight_number,ratings,comments FROM Feedback WHERE airline_name=%s'
    cursor.execute(query, (data2['airline_name']))
	#stores the results in a variable
    data3 = cursor.fetchone()
    print(data2)
	#GROUP BY (flight_number,depart_date,depart_time)
    query = 'SELECT avg(ratings) FROM Feedback WHERE airline_name=%s group by flight_number'
    cursor.execute(query, (data2['airline_name']))
	#stores the results in a variable
    data4 = cursor.fetchone()
    print(data2)
    cursor.close()
    return render_template()

#View Booking agents
@app.route('/ViewBookingAgents', methods=['GET', 'POST'])
def ViewBookingAgents():
    cursor = conn.cursor()
	#WHERE   create_date BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE()
	#where month(order_date)=month(now())-1;
    query = 'SELECT count(ticket_ID) FROM Ticket NATURAL JOIN Purchase_by_BA WHERE purchase_date > CURDATE() - INTERVAL 30 DAY AND CURDATE() > purchase_date group by BA_email ORDER BY count(ticket_ID) DESC LIMIT 5'
    cursor.execute(query, (data2))
	#stores the results in a variable
    data2 = cursor.fetchall()
    print(data2)
    cursor.close()
    cursor = conn.cursor()
	#WHERE   create_date BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE()
	#where month(order_date)=month(now())-1;
    query = 'SELECT count(ticket_ID) FROM Ticket NATURAL JOIN Purchase_by_BA WHERE purchase_date > CURDATE() - INTERVAL 1 YEAR AND CURDATE() > purchase_date group by BA_email ORDER BY count(ticket_ID) DESC LIMIT 5'
    cursor.execute(query, (data2))
	#stores the results in a variable
    data3 = cursor.fetchall()
    print(data2)
    cursor.close()
    return render_template
    	
#/frequentCustomers
@app.route('/frequentCustomers', methods=['GET', 'POST'])
def frequentCustomers():
    	
    return render_template

@app.route('/createNewFlights', methods=['GET','POST'])
def createNewFlights():
    	
	email=session['email']
	cursor = conn.cursor()
	#make a query
	#WHERE depart_date < CURDATE() + INTERVAL 30 DAY and CURDATE() < depart_date'
	query = 'SELECT airline_name FROM Staff WHERE username=%s'
	email=session['email']
	cursor.execute(query, (email))
	#stores the results in a variable
	data2 = cursor.fetchone()
	print(data2['airline_name'])
	cursor.close()
	airplaneID=request.form['airplaneID']
	flightNum=request.form['flightNum']
	departTime=request.form['departTime']
	departDate=request.form['departDate']
	arrivalTime=request.form['arrivalTime']
	arrivalDate=request.form['arrivalDate']
	basePrice=request.form['basePrice']
	airportNameArr=request.form['airportNameArr']
	airportNameDep=request.form['airportNameDep']
	statusF=request.form['statusF']
	print(airplaneID,'airplane ID')
	cursor = conn.cursor()
	#make a query
	#WHERE depart_date < CURDATE() + INTERVAL 30 DAY and CURDATE() < depart_date'
	query = 'INSERT into Flight (airline_name,airplane_ID,flight_number,depart_time,depart_date,arrival_date,arrival_time,base_price,airport_name_arrival,airport_name_depart,status_F)\
		values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
	email=session['email']
	cursor.execute(query, (data2['airline_name'],airplaneID,flightNum,departTime,departDate,arrivalDate,arrivalTime,basePrice,airportNameArr,airportNameDep,statusF))
	#stores the results in a variable
	conn.commit()
	cursor.close()
	return render_template('airline_staff.html')
    
@app.route('/createNewAirplane',methods=['GET','POST'])
def createNewAirplane():
    
	email=session['email']
	cursor=conn.cursor()
	query = 'SELECT airline_name FROM Staff WHERE username=%s'
	cursor.execute(query, (email))
	#stores the results in a variable
	data2 = cursor.fetchone()
	print(data2)
	cursor.close()
	cursor=conn.cursor()
	airplaneID=request.form['airplaneID']
	seats=request.form['seats']
	query = 'INSERT into Flight (airplane_ID,flight_number,airline_name)values (%s,%s,%s)'
	cursor.execute(query, (airplaneID,seats,data2['airline_name']))
	#stores the results in a variable
	conn.commit()
	cursor.close()
	return render_template('airline_staff.html')

@app.route('/createNewAirport',methods=['GET','POST'])
def createNewAirport():
    	
	email=session['email']
	cursor=conn.cursor()
	query = 'SELECT airline_name FROM Staff WHERE username=%s'
	cursor.execute(query, (email))
	#stores the results in a variable
	data2 = cursor.fetchone()
	print(data2)
	cursor.close()
	cursor=conn.cursor()
	city=request.form['city']
	query = 'INSERT into Flight (airplane_ID,flight_number,airline_name)values (%s,%s,%s)'
	cursor.execute(query, (airplaneID,seats,data2['airline_name']))
	#stores the results in a variable
	conn.commit()
	cursor.close()
	return render_template('airline_staff.html')
@app.route('/defaultFlights',methods=['GET','POST'])
def defaultFlights():
    	
	cursor = conn.cursor()
	#make a query
	#WHERE depart_date < CURDATE() + INTERVAL 30 DAY and CURDATE() < depart_date'
	query = 'SELECT * FROM Staff Natural Join Flight WHERE username=%s and depart_date < CURDATE() + INTERVAL 30 DAY and CURDATE() < depart_date'
	email=session['email']
	cursor.execute(query, (email))
	#stores the results in a variable
	data = cursor.fetchall()
	print(data)
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	return render_template('airline_staff.html',flights=data)
    
#this one is airline staff
@app.route('/viewFlights', methods=['GET', 'POST'])
def viewFlights():
    #if one of them is empty 
	#else they are both empty which means their is no flight
	fromCiorAirport = request.form['fromCiorAirport']
	toCiorAirport = request.form['toCiorAirport']
	departDate = request.form['departDate']
	returnDate = request.form['returnDate']
	email=session['email']
	#need a default arg
	cursor = conn.cursor()
	#make a query
	query = 'SELECT * FROM Staff Natural Join Flight WHERE username=%s and airport_name_arrival = %s and airport_name_depart = %s and depart_date = %s and arrival_date=%s'
	cursor.execute(query, (email,airlineName,flightNum,departDate,returnDate))
	#stores the results in a variable
	data = cursor.fetchall()
	print(data)
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	return render_template('airline_staff.html',data2=data,airline_n=airlineName,departD=departDate,flightN=flightNum)
    
#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
	#grabs information from the forms
	email = request.form['email']
	password = request.form['password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Customer WHERE email = %s and password = %s'
	cursor.execute(query, (email, password))
	#stores the results in a variable
	cust = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Booking_Agent WHERE email = %s and passwrd = %s'
	cursor.execute(query, (email, password))
	#stores the results in a variable
	BA = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Staff WHERE username = %s and password = %s'
	cursor.execute(query, (email, password))
	#stores the results in a variable
	staff = cursor.fetchone()
	print(staff)
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(cust):
		
		session['email']=email
		return redirect(url_for('defaultFlightsCus',email=email))
	elif(BA):
    		
		session['email'] = email
		return redirect(url_for('defaultFlightsBA',email=email))
	elif(staff):
    		
		session['email'] = email
		print(email,'looooooogginnn')
		return redirect(url_for('defaultFlights',email=email))
	else:
    	
		error = 'Invalid login or username'
		return render_template('login.html',error=error)



#View top customers



#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
	#grabs information from the forms
    email = request.form['email']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    DOB = request.form['DOB']
    phone_number = request.form['phone_number']
    value=request.form['opt']
	#cursor used to send queries
    cursor = conn.cursor()
#executes query
    if(value=='1'):
        query = 'SELECT * FROM Customer WHERE email = %s'
        cursor.execute(query, (email))
    elif(value=='2'):
        query = 'SELECT * FROM Booking_Agent WHERE email = %s'
        cursor.execute(query, (email))
    elif(value=='3'):
        query = 'SELECT * FROM Staff WHERE email = %s'
        cursor.execute(query, (email))
#stores the results in a variable
    data = cursor.fetchone()
#use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
	#If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error = error)
    else:
        if(value=='1'):
            #query = 'SELECT * FROM Customer WHERE email = %s'
            ins = 'INSERT into Customer (email,password,first_name,last_name,phone_number,DOB) values(%s, %s, %s, %s, %s, %s)'
            cursor.execute(ins, (email))
        elif(value=='2'):
            #query = 'SELECT * FROM Booking_Agent WHERE email = %s'
            ins = 'INSERT into Booking_Agent (email, password) values(%s, %s)'
            cursor.execute(ins, (email))
        elif(value=='3'):
            #query = 'SELECT * FROM Staff WHERE email = %s'
            ins = 'INSERT into Staff (email,password,first_name,last_name,DOB) values(%s, %s, %s, %s, %s)'
            cursor.execute(ins, (email))
        #ins = 'INSERT INTO user (email,passwrd) VALUES(%s, %s)'
        cursor.execute(ins, (username, password))
        conn.commit()
        cursor.close()
        return render_template('index.html')


		


@app.route('/logout')
def logout():
	session.pop('email')
	return redirect('/')
		
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
