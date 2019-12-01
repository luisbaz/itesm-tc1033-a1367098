class Attendant_r():
    def lectura():
        with open ("attendants.csv", "r") as a1:
            lineas=a1.readlines()
            info_attendants={}
            for x in lineas:
                string=x.split(",")
                passport=string[0]
                forename=string[1]
                surname=string[2]
                birth=string[3]
                country=string[4]
                gender=string[5]
                m_status=string[6]
                attendant_object=Attendant(self,_passport,_forename,_surname,_birth,_country,_gender,_marital)
                info_attendants[passport]=attendant_object

class Flight_r():
    def lectura():
        with open ("flights.csv", "r") as f1:
            lineas=f1.readlines()
            info_flights={}
            for x in lineas:
                string=x.split(",")
                _id=string[0]
                plate=string[1]
                origin=string[2]
                destiny=string[3]
                departure=string[4]
                arriving=string[5]
                status=string[6]
                d_gate=string[7]
                to_gate=string[8]
                a_gate=string[9]
                landing_t=string[10]
                pilot=string[11]
                copilot=string[12]
                attendants=string[13]
                flight_object=Flight(self,_plate,_origin,_destiny,_departure,_arriving,_status,_d_gate,_to_gate,_a_gate,_landing,_pilot,_copilot,_attendants)
                info_flight[departure]=flight_object
                

    
class Passenger_r():
    def lecutra():
        with open ("passengers.csv", "r") as pgr:
            lineas=pgr.readlines()
            info_passengers={}
            for x in lineas:
                string=x.split(",")
                flight=string[0]
                passport=string[1]
                clase=string[2]
                seat=string[3]
                location=string[4]
                passenger_object=Passenger(self,_flight,_passport,_clase,_seat,_location)
                info_passengers[passport]=passenger_object

class Pilot_r():
    def lectura():
        with open ("pilots.csv", "r") as plt:
            lineas=plt.readlines()
            info_pilots={}
            for x in lineas:
                string=x.split(",")
                passport=string[0]
                forename=string[1]
                surname=string[2]
                birth=string=[3]
                country=string[4]
                gender=string[5]
                m_status=string[6]
                pilot_object=Pilot(self,_passport,_forename,_surname,_birth,_country,_gender,_marital)
                info_pilots[passport]=pilot_object
class Plane_r():
    def lectura():
        with open ("planes.csv", "r") as pln:
            lineas=pln.readlines()
            info_planes={}
            for x in lineas:
                string=x.split(",")
                plate=string[0]
                manufacturer=string[1]
                model=string[2]
                pgr_capacity=string[3]
                lgg_capacity=string[4]
                max_speed=string[5]
                plane_object=Plane(self,_plate,_manufacturer,_model,_pgr_capacity,_lgg_capacity,_max_speed)
                info_planes[model]=plane_object

class Traveller_r():
    def lectura():
        with open ("travellers.csv", "r") as tvlr:
            lineas=tvlr.readlines()
            info_travellers={}
            for x in lineas:
                string=x.split(",")
                passport=string[0]
                forename=string[1]
                surname=string[2]
                birth=string=[3]
                country=string[4]
                gender=string[5]
                m_status=string[6]
                traveller_object=Traveller(self,_passport,_forename,_surname,_birth,_country,_gender,_marital)
                info_travellers[passport]=traveller_object


