class binusMaya:
    def __init__(self, lec_dict):
        self.lec = lec_dict #look for dictionary at the bottom / after all define functions
        self.classes = ['L1AC', 'L1BC', 'L1CC', 'B1AC', 'B1BC', 'B1CC']
        self.schedule = []
    
    def addLec(self, subject, name, id):
        for lecturer in self.lec:
            if lecturer['subject'] == subject:
                print(f'Error: A lecturer for {subject} already exists')
                return

        new_lec = {
            'name': name,
            'subject': subject,
            'id': id
        }
        self.lec.append(new_lec)
        print(f'Lecturer for {subject} has been added')

    def removeLec(self, id):
        for lecturer in self.lec:
            if lecturer['id'] == id:
                self.lec.remove(lecturer)
                print(f'Lecturer with ID {id} has been removed')
                return
            
        print(f'Error: There is no lecturer with ID {id}')

    def addClass(self, classcode):
        if classcode in self.classes:
            print(f'Error: A class with class code {classcode} already exists')
            return
        
        self.classes.append(classcode)
        print(f'Class {classcode} has been added')

    def removeClass(self, classcode):
        if classcode in self.classes:
            self.classes.remove(classcode)
            print(f'Class {classcode} has been removed')
            return
        
        print(f'Error: There is no class with classcode {classcode}')

    def addSchedule(self, subject, time, classcode):
        for lecturer in self.lec:
            if lecturer['subject'] == subject:
                new_schedule = (time, classcode, lecturer['subject'], lecturer['name'])
                self.schedule.append(new_schedule)
                print(f'Schedule of class {classcode} for {subject} at {time} has been added')
                return
        
        print(f'Error: No lecturer found for {subject}')

    #I MADE EXTRA CAUSE IT FELT WEIRD THAT THERE WASNT ANY REMOVE / CANCEL SCHEDULE
    def removeSchedule(self, subject, classcode):
        for schedules in self.schedule:
            if schedules[1] == classcode and schedules[2] == subject:
                self.schedule.remove(schedules)
                print(f'Schedule of class {classcode} for {subject} has been removed / canceled')
                return
        
        print(f'Error: No schedule found in class {classcode} for {subject}')

lec_dict = [
    {'name': 'Alexander Legolas', 'subject': 'AlgoProg-Lab', 'id': 'A2188'},
    {'name': 'Ruixin Huang', 'subject': 'HCI-Lab', 'id': 'A2190'},
    {'name': 'Jude Martinez', 'subject': 'AlgoProg-Lec', 'id': 'D4017'},
    {'name': 'Kartika Yulianti', 'subject': 'Pancasila-Lec', 'id': 'D6436'},
    {'name': 'Fergyanto Gunawan', 'subject': 'DiscreteMaths-Lec', 'id': 'D3776'},
    {'name': 'Ida Bagus', 'subject': 'HCI-Lec', 'id': 'D5757'},
    {'name': 'Satrio Pradono', 'subject': 'ProgDesignMethods-Lec', 'id': 'D4106'},
    {'name': 'Zhandos Yessenbayev', 'subject': 'SciComp-Lec', 'id': 'D6933'}
]

#example:
test = binusMaya(lec_dict)

test.addLec('Comedy-Lec', 'Tom Jerry', 'B2145') #add new lecturer
test.addLec('HCI-Lab', 'Mary Rose', 'A1267') #fails

test.removeLec('A2188') #removes Legolas >:) dw i dont hate you
test.removeLec('F7893') #fails

test.addClass('L1DC') #should work
test.addClass('B1AC') #fails

test.removeClass('L1BC') #removes class
test.removeClass('B2YC') #fails

test.addSchedule('SciComp-Lec', '14:00', 'L1AC') #new schedule
test.addSchedule('Mixology-Lab', '09:00', 'B1CC') #fail

#EXTRA YOU CAN SKIP
test.removeSchedule('SciComp-Lec', 'L1AC') #works
test.removeSchedule('Communications-Lec', 'D3HJ') #doesnt work