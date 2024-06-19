from src.base_classes.thread_timer import BackgroundTimer
from src.libraries import util_library
from src.libraries import ascii_library
from src.menus.question_widget_displayer import QuestionDisplay
from src.base_classes.level import Level


import random

class Difficulty(Level):
    difficulty = "No difficulty selected"
    question_display_inst = None
    player_points = 0
    finished_questions = []
    timer_inst = None
    time_left = 0
    previous_question_index = 0
    
    #index, ASCII_Index, HintArray, PossibleAnswerArray, CorrectAnswerIndex
    question_data = [["0", ascii_library.ascii_list[0], ["Yellow", "A fruit", "Filled with Pottatium"], ["Banana", "Apple", "Yellow Mango"], 0],
                     ["1", ascii_library.ascii_list[1], ["Found in Ocean", "A mammal in water", "Their Group are called Pod"], ["Shark", "Nemo", "Dolphins"], 2],
                     ["2", ascii_library.ascii_list[2], ["Has Feathers", "Quacks", "Swims"], ["Bird", "Duck", "Dog"], 1],
                     ["3", ascii_library.ascii_list[3], ["Found at Night", "Natural light in the dark", "Neil Armstrong"], ["Moon", "Sun", "Earth"], 0],
                     ["4", ascii_library.ascii_list[4], ["Has 2 Wheels", "Pedal to Move", "Used for Riding"], ["Shoes", "Bicycle", "Car"], 1],
                     ["5", ascii_library.ascii_list[5], ["Grows on Trees", "Keeps the Doctor Away", "Red or Green"], ["Orange", "Apple", "Banana"], 1],
                     ["6", ascii_library.ascii_list[6], ["Insects", "Pollinate Flowers", "Produce Honey"], ["Ant", "Butterfly", "Bee"], 2],
                     ["7", ascii_library.ascii_list[7], ["Has Big Ears", "Lives in Burrows", "Hops"], ["Kangaroo", "Rabbit", "Squirrel"], 1],
                     ["8", ascii_library.ascii_list[8], ["Toy that Flies", "Controlled with Strings", "Often Seen in Parks"], ["Bird", "Plane", "Kite"], 2],
                     ["9", ascii_library.ascii_list[9], ["Has Feathers", "Can't Fly", "Largest Bird"], ["Penguin", "Ostrich", "Parrot"], 1],
                     ["10", ascii_library.ascii_list[10], ["Used for Telling Time", "Has Numbers", "Has Hands"], ["Clock", "Ruler", "Compass"], 0],
                     ["11", ascii_library.ascii_list[11], ["Sweet Desert", "Comes in Many Flavors", "Often Frozen"], ["Cake", "Ice Cream", "Cookies"], 1],
                     ["12", ascii_library.ascii_list[12], ["Part of the Body", "Used for Hearing", "Comes in Pairs"], ["Eyes", "Ears", "Nose"], 1],
                     ["13", ascii_library.ascii_list[13], ["Used for School", "Writes with Ink", "Has a Cap"], ["Pen", "Pencil", "Crayon"], 0],
                     ["14", ascii_library.ascii_list[14], ["Lives in Water", "Has Scales", "Breathes with Gills"], ["Octopus", "Shark", "Fish"], 2],
                     ["15", ascii_library.ascii_list[15], ["Small and Orange", "Good Source of Vitamin C", "Often Peeled"], ["Grapefruit", "Tangerine", "Kiwi"], 1],
                     ["16", ascii_library.ascii_list[16], ["Large Fruit", "Has Stripes", "Juicy and Sweet"], ["Watermelon", "Strawberry", "Grapes"], 0],
                     ["17", ascii_library.ascii_list[17], ["Raisins", "Produce Wine", "Small fruit"], ["Peas", "Mango", "Grapes"], 2],
                     ["18", ascii_library.ascii_list[18], ["Black and white", "Bird", "Lives in cold climates"], ["Penguin", "Maya", "Seal"], 0],
                     ["19", ascii_library.ascii_list[19], ["Hard shell covering its body", "Moves slowly on land", "Reptile"], ["Clown Fish", "Turtle", "Squirtel"], 1],
                     ["20", ascii_library.ascii_list[20], ["Filled with helium or air", "For Decoration", "Kids Toy"], ["Ball", "Kite", "Balloon"], 2],
                    ]
    
    def __init__(self, owner):
        super().__init__(owner)
        self.create_question_displayer()
        self.start_questioning()
    
    def get_raw_time_left(self):
        return self.time_left
    
    def get_time_left(self):
        timeleft = self.time_left
        mins, secs = divmod(timeleft, 60)
        time_formated = '{:02d}:{:02d}'.format(mins, secs)
        return time_formated
    
    def get_player_points(self):
        return self.player_points
        
    #Not really used since the changing of initial time is handled in the child class
    def get_initial_time(self):
        return 60 if self.difficulty == "easy" else 30
    
    def start_questioning(self):
        self.timer_inst = BackgroundTimer(self.time_left, self)
        self.display_new_question()
        
    def run_timer_task(self, raw_time_left):
        self.time_left = raw_time_left
        self.refresh_question_display()
        
    def create_question_displayer(self):
        self.question_display_inst = QuestionDisplay(self)
        
    def display_new_question(self):
        self.clear_console()

        if len(self.question_data) == 1:
            current_question_index = 0
        else:
            current_question_index = random.randrange(len(self.question_data))
            while current_question_index == self.previous_question_index:
                current_question_index = random.randrange(len(self.question_data))

        self.question_display_inst.display_new_question(self.difficulty, self.question_data[current_question_index])
        self.previous_question_index = current_question_index
        
    def player_got_correct_answer(self, points, question_index):
        self.player_points += points
        self.finished_questions.append(question_index) 
        self.display_new_question()  
    
    def player_failed_to_answer(self, question_index):
        self.finished_questions.append(question_index) 
        self.display_new_question()
        
    def refresh_question_display(self):
        self.question_display_inst.refresh_display_question()
        
    def player_wants_to_stop(self):
        self.stop_timer()

    def stop_timer(self):
        self.timer_inst.stop_timer()
    
    def times_up(self):
        self.clear_console()
        self.owner.add_points(self.player_points)
        self.question_display_inst.display_loading_animation()
        self.owner.display_main_menu()    
    