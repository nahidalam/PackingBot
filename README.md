##Packing Robot Body

Given volume of a suitcase in http://pkit.wopr.c2x.io:8000/suitcases/rolly

Given information on robot body parts  http://pkit.wopr.c2x.io:8000/robots/8871bd6c89a842f9b5c9be7e0eecda92/parts

Find a solution to maximize the value of the parts in the suitace that fits

#### Sample json output 

{
    "part_ids": ["part-1", "part-2"],
    "value": 123123
}


#### To Run the program

python packBot.py http://pkit.wopr.c2x.io:8000/suitcases/rolly http://pkit.wopr.c2x.io:8000/robots/8871bd6c89a842f9b5c9be7e0eecda92/parts
