import random
from fpdf import FPDF
comp_set = ["stone","paper","scissor"]

#main function
def main():
    print("####################################")
    print("Welcome to stone paper scissors game.......")
    print("Lets see the rules for playing")
    print("There are three choice given here for play : Stone, paper, scissor")
    comp_choice = random.choice(comp_set)
    user_choice = input("Enter your choice : ")
    print("Computer choice : "+comp_choice)
    if user_choice.lower() =="stone":
        if check_for_stone(comp_choice):
            if comp_choice ==user_choice :
                print("Tie")
            else:
                print("You won")
                generate_certificate()
                print("shirtificate congratulations.....")
                print("################# The End #################")
        else:
            print("You lose")
    elif user_choice.lower() =="paper":
        if check_for_paper(comp_choice):
            if comp_choice == user_choice:
                print("Tie")
            else:
                print("You won")
                generate_certificate()
                print("shirtificate generated congratulations.....")
                print("################# The End #################")


        else:
            print("You lose")
    elif user_choice.lower() =="scissor":
        if check_for_scissor(comp_choice):
            if comp_choice == user_choice:
                print("Tie")
            else:
                print("You won")
                generate_certificate()
                print("shirtificate generated congratulations.....")
                print("################# The End #################")
        else:
            print("You lose")
    else:
        print("Invalid input")


#check for stone
def check_for_stone(comp_choice):
    #conditions : stone and stone tie, stone paper : lose , stone , scissors : win
    if comp_choice == "stone":
        return True
    elif comp_choice =="scissor":
        return True
    else:
        return False

#check for paper
def check_for_paper(comp_choice):
    #conditions: paper and paper tie, paper and scissors: lose, paper and stone :  win
    if comp_choice == "paper":
        return True
    elif comp_choice =="stone":
        return True
    else:
        return False

#check for scissor
def check_for_scissor(comp_choice):
    #conditions: scissors and scissors tie, scissors and stone : lose, scissors and paper : win
    if comp_choice == "scissor":
        return True
    elif comp_choice =="paper":
        return True
    else:
        return False

#generare shirtificate for user won
def generate_certificate():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica","B",45)
    pdf.cell(0,60, "Winning shirtificate", align = "C")
    pdf.image("/workspaces/110348050/project/assets/shirtificate.png",x=0, y=70)
    pdf.set_font_size(30)
    pdf.set_text_color(255,255,255)
    pdf.text(x=45, y=150, txt=f"{name} won game")
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()


