def arithmetic_arranger(problems = [" ", " ", " ", " "], show_answers = False): 
    if len(problems) > 4:
        print("Error: too many problems!")
        return
    
    if all(problem.isdigit() or problem in ["+", "-"] for problem in problems):
        print('Error: Numbers must only contain digits.')
        return
 


    #searate the problems
    if len(problems) == 1:
        first_problem = problems[0]
        parts_1 = first_problem.split()
        left_1 = parts_1[0]
        operator_1 = parts_1[1]
        right_1 = parts_1[2]
        if operator_1 == '+':
            answer_1 = int(left_1) + int(right_1)
        elif operator_1 == '-':
            answer_1 = int(left_1) - int(right_1)
        if operator_1 == '*' or operator_1 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if len(left_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        width_1 = max(len(left_1), len(right_1)) + 2
        width_5 = len(str(answer_1)) + 2
        line_1 = left_1.rjust(width_1)
        line_2 = operator_1 + right_1.rjust(width_1 - 1)
        line_3 = "-" * width_1
        line_4 = str(answer_1).rjust(width_5)
        print(line_1)
        print(line_2)
        print(line_3)
        if show_answers == True:
            print(line_4)
        
    
    if len(problems) == 2:
        first_problem = problems[0]
        second_problem = problems[1]
        parts_1 = first_problem.split()
        parts_2 = second_problem.split()
        left_1 = parts_1[0]
        operator_1 = parts_1[1]
        right_1 = parts_1[2]
        left_2 = parts_2[0]
        operator_2 = parts_2[1]
        right_2 = parts_2[2]
        if operator_1 == '+':
            answer_1 = int(left_1) + int(right_1)
        elif operator_1 == '-':
            answer_1 = int(left_1) - int(right_1)
        if operator_2 == '+':
            answer_2 = int(left_2) + int(right_2)
        elif operator_2 == '-':
            answer_2 = int(left_2) - int(right_2)
        if operator_1 == '*' or operator_1 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if operator_2 == '*' or operator_2 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if len(left_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(left_2) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_2) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        width_1 = max(len(left_1), len(right_1)) + 2
        width_2 = max(len(left_2), len(right_2)) + 2
        width_5 = len(str(answer_1)) + 2
        width_6 = len(str(answer_2)) + 2
        line_1 = left_1.rjust(width_1) + "    " + left_2.rjust(width_2)
        line_2 = operator_1 + right_1.rjust(width_1 - 1) + "    " + operator_2 + right_2.rjust(width_2 - 1)
        line_3 = "-" * width_1 + "    " + "-" * width_2
        line_4 = str(answer_1).rjust(width_5) + "    " + str(answer_2).rjust(width_6)
        print(line_1)
        print(line_2)
        print(line_3)
        if show_answers == True:
            print(line_4)


    if len(problems) == 3:
        first_problem = problems[0]
        second_problem = problems[1]
        third_problem = problems[2]
        parts_1 = first_problem.split()
        parts_2 = second_problem.split()
        parts_3 = third_problem.split()
        left_1 = parts_1[0]
        operator_1 = parts_1[1]
        right_1 = parts_1[2]
        left_2 = parts_2[0]
        operator_2 = parts_2[1]
        right_2 = parts_2[2]
        left_3 = parts_3[0]
        operator_3 = parts_3[1]
        right_3 = parts_3[2]
        if operator_1 == '+':
            answer_1 = int(left_1) + int(right_1)
        elif operator_1 == '-':
            answer_1 = int(left_1) - int(right_1)
        if operator_2 == '+':
            answer_2 = int(left_2) + int(right_2)
        elif operator_2 == '-':
            answer_2 = int(left_2) - int(right_2)
        if operator_3 == '+':
            answer_3 = int(left_3) + int(right_3)
        elif operator_3 == '-':
            answer_3 = int(left_3) - int(right_3)
        if operator_1 == '*' or operator_1 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if operator_2 == '*' or operator_2 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if operator_3 == '*' or operator_3 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if len(left_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(left_2) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_2) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(left_3) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_3) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        width_1 = max(len(left_1), len(right_1)) + 2
        width_2 = max(len(left_2), len(right_2)) + 2
        width_3 = max(len(left_3), len(right_3)) + 2
        width_5 = len(str(answer_1)) + 2
        width_6 = len(str(answer_2)) + 2
        width_7 = len(str(answer_3)) + 2
        line_1 = left_1.rjust(width_1) + "    " + left_2.rjust(width_2) + "    " + left_3.rjust(width_3)
        line_2 = operator_1 + right_1.rjust(width_1 - 1) + "    " + operator_2 + right_2.rjust(width_2 - 1) + "    " + operator_3 + right_3.rjust(width_3 - 1)
        line_3 = "-" * width_1 + "    " + "-" * width_2 + "    " + "-" * width_3
        line_4 = str(answer_1).rjust(width_5) + "    " + str(answer_2).rjust(width_6) + "    " + str(answer_3).rjust(width_7)
        print(line_1)
        print(line_2)
        print(line_3)
        if show_answers == True:
            print(line_4)    
    


    if len(problems) == 4:
        first_problem = problems[0]
        second_problem = problems[1]
        third_problem = problems[2]
        fourth_problem = problems[3]
        parts_1 = first_problem.split()
        parts_2 = second_problem.split()
        parts_3 = third_problem.split()
        parts_4 = fourth_problem.split()
        left_1 = parts_1[0]
        operator_1 = parts_1[1]
        right_1 = parts_1[2]
        left_2 = parts_2[0]
        operator_2 = parts_2[1]
        right_2 = parts_2[2]
        left_3 = parts_3[0]
        operator_3 = parts_3[1]
        right_3 = parts_3[2]
        left_4 = parts_4[0]
        operator_4 = parts_4[1]
        right_4 = parts_4[2]
        if operator_1 == '+':
            answer_1 = int(left_1) + int(right_1)
        elif operator_1 == '-':
            answer_1 = int(left_1) - int(right_1)
        if operator_2 == '+':
            answer_2 = int(left_2) + int(right_2)
        elif operator_2 == '-':
            answer_2 = int(left_2) - int(right_2)
        if operator_3 == '+':
            answer_3 = int(left_3) + int(right_3)
        elif operator_3 == '-':
            answer_3 = int(left_3) - int(right_3)
        if operator_4 == '+':
            answer_4 = int(left_4) + int(right_4)
        elif operator_4 == '-':
            answer_4 = int(left_4) - int(right_4)
        if operator_1 == '*' or operator_1 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if operator_2 == '*' or operator_2 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if operator_3 == '*' or operator_3 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if operator_4 == '*' or operator_4 == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        if len(left_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_1) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(left_2) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_2) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(left_3) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_3) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(left_4) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        if len(right_4) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        width_1 = max(len(left_1), len(right_1)) + 2
        width_2 = max(len(left_2), len(right_2)) + 2
        width_3 = max(len(left_3), len(right_3)) + 2
        width_4 = max(len(left_4), len(right_4)) + 2
        width_5 = len(str(answer_1)) + 2
        width_6 = len(str(answer_2)) + 2
        width_7 = len(str(answer_3)) + 2
        width_8 = len(str(answer_4)) + 2
        line_1 = left_1.rjust(width_1) + "    " + left_2.rjust(width_2) + "    " + left_3.rjust(width_3) + "    " + left_4.rjust(width_4)
        line_2 = operator_1 + right_1.rjust(width_1 - 1) + "    " + operator_2 + right_2.rjust(width_2 - 1) + "    " + operator_3 + right_3.rjust(width_3 - 1) + "    " + operator_4 + right_4.rjust(width_4 - 1)
        line_3 = "-" * width_1 + "    " + "-" * width_2 + "    " + "-" * width_3 + "    " + "-" * width_4
        line_4 = str(answer_1).rjust(width_5) + "    " + str(answer_2).rjust(width_6) + "    " + str(answer_3).rjust(width_7) + "    " + str(answer_4).rjust(width_8)
    
        print(line_1)
        print(line_2)
        print(line_3)
        if show_answers == True:
            print(line_4)
    
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])

   
    
    
        
        
    

    
    




    

