#!/usr/bin/python3
"""Defining the class Base"""
import json
import os
import csv
import turtle


class Base:
    """This is the class base

       Args:
           __nb_objects (int): private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This function will initialize the class Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function takes a list of ictionaries
           and returns the json representation

           Args:
               list_dictionaries (list): list of dictionaries

           Returns:
               json represenation
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function write the json representation of list_obj
           to file

           Args:
               list_objs (list): the list of instances
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                new_list = []
                for i in list_objs:
                    new_list.append(i.to_dictionary())
                f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """This function returns the list of json representation
           in json_string

           Args:
               json_string (str): string representation of list of
               dictionaries

           Returns:
               list of json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This function returns an instance with all attributes already set.

           Args:
               dictionary (dict): double pointer to dictionary

           Returns:
               returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            instance = cls(2, 3)
        if cls.__name__ == "Square":
            instance = cls(2)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """This file returns list of instance depending on the class"""

        file_name = cls.__name__ + ".json"
        if os.path.isfile(file_name):
            with open(file_name, "r", encoding='utf-8') as f:
                list_of_dict = cls.from_json_string(f.read())
                new_list = []
                for i in list_of_dict:
                    new_list.append(cls.create(**i))
            return new_list
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This function saves list of objects to a csv file.

        Args:
            list_objs (list): list of instances
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w") as f:
            if cls.__name__ == "Rectangle":
                field_names = ['id', 'width', 'height', 'x', 'y']
            if cls.__name__ == "Square":
                field_names = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(f, fieldnames=field_names)
            csv_writer.writeheader()
            if list_objs is None:
                csv_writer.writerow()
            else:
                for i in list_objs:
                    csv_writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This function returns the list of instance depending on the class

           Returns:
               list of instance
        """
        file_name = cls.__name__ + ".csv"
        if os.path.isfile(file_name):
            with open(file_name, "r") as f:
                new_list = []
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    new_list.append({k: int(v) for k, v in row.items()})
                list_of_dict = []
                for i in new_list:
                    list_of_dict.append(cls.create(**i))
            return list_of_dict
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This function is gonna use the turtle graphics to draw.

           Args:
               list_rectangles (list): list of rectangle
               list_square (list): list of squares
        """
        my_turtle = turtle.Turtle()
        my_turtle.bgcolor("grey")
        my_turtle.shape("turtle")
        my_turtle.pencolor("green")
        my_turle.pensize(10)

        for rec in list_rectangles:
            if rec.x > 0 and rec.y > 0:
                my_turtle.penup()
                my_turtle.goto(rec.x, rec.y)
                my_turtle.pendown()
            else:
                my_turtle.penup()
                my_turtle.home()
                my_turtle.pendown()
            my_turtle.fillcolor("green")
            my_turtle.begin_fill()
            for i in range(2):
                my_turtle.fd(rec.width)
                my_turtle.rt(90)
                my_turtle.fd(rec.height)
                my_turtle.rt(90)
            my_turtle.end_fill()
        for s in list_squares:
            if s.x > 0 and s.y > 0:
                my_turtle.penup()
                my_turtle.goto(s.x, s.y)
                my_turtle.pendown()
            else:
                my_turtle.penup()
                my_turtle.home()
                my_turtle.pendown()
            my_turtle.fillcolor("yellow")
            my_turtle.begin_fill()
            for i in range(4):
                my_turtle.fd(s.size)
                my_turtle.rt(90)
            my_turtle.end_fill()
