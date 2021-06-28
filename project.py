# Project 1 : Basic School Administration Tool
import csv


def write_csv(info_list):
    with open('project.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact No.","Email-ID"])
        writer.writerow(info_list)


if __name__ == '__main__':
    con = True
    student_num = 1

    while con:
        student_info = input("\nEnter Student Information for student #{} in Format (Name Age Contact_No Email_ID) : ".
            format(student_num))

        student_info_list = student_info.split(' ')

        print("\n Entered Information : \nName : {}\nAge: {}\nContact No. : {}\nEmail-ID : {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        ch = input("Is the entered information correct?(yes/no)")

        if ch == "yes":
            write_csv(student_info_list)

            con_check = input("\nEnter (yes/no) if you want to enter more information of students : ")
            if con_check == "yes":
                con = True
                student_num = student_num + 1
            elif con_check == "no":
                con = False

        elif ch == "no":
            print("\n Re-Enter the information")