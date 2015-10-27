class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    @property
    def car(self):
        return {"year": self.year, "make": self.make, "model": self.model}

    def import_cars(self, csv_file):
        # logger.error("This has not been implemented yet.")
            """Read csv file and add each car to database"""
        with open(file) as fileHandler:
            # Discard header line
            fileHandler.readline()
            """Add each line (car) to the database"""
            for car_line in fileHandler:
                #car information = [year, make, model]
                car_information = car_line.strip().split(",")
                self.cursor.execute('', car_information)

    def update_car(self, current_car, new_car):
        # logger.error("This has not been implemented yet.")

        def update(self, current_car, new_car):
            cars_info = [new_car.car["year"], 
                            new_car.car["make"], 
                            new_car.car["model"], 
                            current_car.car["year"], 
                            current_car.car["make"], 
                            current_car.car["model"]]

            self.cursor.execute(cars_info)
            self.con.commit()


    def delete_car():
        request.method == 'DELETE':
            car.delete()
            return HttpResponse(status=204)
        # logger.error("This has not been implemented yet.")

