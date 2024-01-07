class Quiz:
    def __init__(self):
        self.questions = [
            {'question': 'Mikor kezdődött az ipari forradalom?', 'options': ['A) 16. század', 'B) 18. század', 'C) 20. század'], 'correct_answer': 'B'},
            {'question': 'Mi volt az első ipari forradalom kiemelkedő találmánya?', 'options': ['A) Gőzgép', 'B) Telefon', 'C) Számítógép'], 'correct_answer': 'A'},
            {'question': 'Hol indult el az ipari forradalom?', 'options': ['A) Egyesült Királyság', 'B) Franciaország', 'C) Németország'], 'correct_answer': 'A'},
            {'question': 'Mi volt a szén szerepe az ipari forradalomban?', 'options': ['A) Építőanyagként használták', 'B) Energiahordozóként szolgált', 'C) Gyógyszerként alkalmazták'], 'correct_answer': 'B'},
            {'question': 'Ki volt az ipari forradalom "átokának" nevezett könyv szerzője?', 'options': ['A) Karl Marx', 'B) Adam Smith', 'C) Thomas Malthus'], 'correct_answer': 'C'}
        ]
        self.score = 0

    def run_quiz(self):
        print("Üdvözöllek az ipari forradalom kvízben!")
        for i, question in enumerate(self.questions, 1):
            print(f"\n{i}. kérdés: {question['question']}")
            for option in question['options']:
                print(option)
            user_answer = input("Válasz (A/B/C): ").upper()
            if user_answer == question['correct_answer']:
                print("Helyes válasz!\n")
                self.score += 1
            else:
                print(f"Sajnálom, helytelen válasz. A helyes válasz: {question['correct_answer']}\n")
        print(f"A kvíz véget ért! Pontszám: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
